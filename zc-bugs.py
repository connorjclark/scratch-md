from datetime import datetime, timedelta
from types import SimpleNamespace
import re
import sys
import discord
from discord.ext import commands

# ask for people's github accounts
# do the github api side, test import into new repo
# do a minimal clean up on discord first. Only manually look at the most recent 10% 'unknown' threads
# double-check not exposing any toxic arguments
# when done, lock all the issue channels and post a link to the github page in the thread

ZC_GUILD_ID = 876899628556091432
BUGS_THREAD_ID = 876906434829353071
COMPAT_BUGS_THREAD_ID = 932919361415577661
FEATURES_THREAD_ID = 876906577825763328

starting_gh_issue_num = 797
thread_ids_to_gh_num = {}

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot('.', intents=intents)

def trim_string(s: str, limit: int, ellipsis='…') -> str:
    s = s.strip()
    if len(s) > limit:
        return s[:limit-1].strip() + ellipsis
    return s


async def collect_channel_threads(channel):
    threads = []
    threads.extend(channel.threads)
    async for thread in channel.archived_threads(limit=None):
        threads.append(thread)
    return threads


def determine_status(thread):
    status = 'unknown'
    if '🔒' in thread.name or thread.locked:
        if '✅' in thread.name:
            status = 'fixed'
        elif '❌' in thread.name:
            status = 'wont-fix'
        else:
            status = 'closed'
    elif '🔓' in thread.name:
        if '💊' in thread.name:
            status = 'needs-testing'
        else:
            status = 'open'
    else:
        # Often the locks aren't present...
        if thread.parent.id == FEATURES_THREAD_ID:
            # Just assume that features are still valid.
            status = 'open'
        elif '✅' in thread.name:
            status = 'fixed'
        elif '❌' in thread.name:
            status = 'wont-fix'
        elif '💊' in thread.name:
            status = 'needs-testing'
        elif '❓' in thread.name:
            status = 'closed'
    
    return status


@bot.event
async def on_ready():
    guild = bot.get_guild(ZC_GUILD_ID)

    all_threads = []
    all_threads.extend(await collect_channel_threads(guild.get_channel(BUGS_THREAD_ID)))
    all_threads.extend(await collect_channel_threads(guild.get_channel(COMPAT_BUGS_THREAD_ID)))
    all_threads.extend(await collect_channel_threads(guild.get_channel(FEATURES_THREAD_ID)))
    all_threads = sorted(all_threads, key=lambda thread: thread.id)

    # all_threads = [x for x in all_threads if x.id == 1012975336801181737]

    print(f'found {len(all_threads)} threads\n\n')

    PRINT_UNKNOWN_THREADS = False
    if PRINT_UNKNOWN_THREADS:
        unknown_status_threads = [t for t in all_threads if determine_status(t) == 'unknown']
        print(f'found {len(unknown_status_threads)} unknown status threads\n\n')
        for thread in unknown_status_threads:
            print(f'{thread.created_at} {thread.name} https://discord.com/channels/{ZC_GUILD_ID}/{thread.id}')
        await bot.close()
        return
    
    for i, thread in enumerate(all_threads):
        thread_ids_to_gh_num[thread.id] = starting_gh_issue_num + i
    
    converted_threads = []

    for thread in all_threads:
        print(f'{thread.id} {thread.created_at} {thread.name}', file=sys.stderr)
        
        lines = []
        messages = [x async for x in thread.history(limit=None)]
        messages.reverse()
        
        previous_message = None
        for message in messages:
            if previous_message == None or previous_message.author.id != message.author.id or message.created_at - previous_message.created_at > timedelta(minutes=1):
                gh_username = get_author_github_name(message.author)
                timestamp = message.created_at.strftime("%m/%d/%Y %H:%M")
                lines.append(f'\n=== {gh_username} {timestamp}\n')
            previous_message = message

            if message.type == discord.MessageType.default:
                lines.append(message.content)
            elif message.type == discord.MessageType.thread_starter_message:
                starter = await thread.parent.fetch_message(message.reference.message_id)
                lines.append(starter.content)
                # I think this is always blank, but just in case it isn't...
                if message.content:
                    lines.append(message.content)
            elif message.type == discord.MessageType.reply:
                try:
                    replying_to = await thread.fetch_message(message.reference.message_id)    
                    replying_prefix = f'(replying to {get_author_github_name(replying_to.author)} "{trim_string(replying_to.content, 30)}"):'
                    lines.append(f'{replying_prefix} {message.content}')
                except:
                    replying_prefix = f'(replying to deleted comment):'
                    lines.append(f'{replying_prefix} {message.content}')
            elif message.type == discord.MessageType.channel_name_change:
                lines.append(f'(meta) thread name was changed: {message.content}')
            else:
                lines.append(f'(meta, {message.type}) {message.content}')

            for attachment in message.attachments:
                if attachment.width != None:
                    lines.append(f'![image]({attachment.url})')
                else:
                    lines.append(attachment.url)

        def replace_id_tags(m):
            if m.group(1) == '@' or m.group(1) == '@!':
                user_id = int(m.group(2))
                user = bot.get_user(user_id)
                if user == None:
                    return f'@ DeletedUser'
                return get_author_github_name(user)
            elif m.group(1) == '#':
                channel_id = int(m.group(2))
                if channel_id in thread_ids_to_gh_num:
                    return f'#{thread_ids_to_gh_num[channel_id]}'

                # Not a link to a bug thread, so let's link to the discord channel.
                the_channel = bot.get_channel(channel_id)
                if the_channel:
                    return f'[#{the_channel.name}](https://discord.com/channels/{the_channel.guild.id}/{the_channel.id})'
                else:
                    return '#deleted-channel'
            elif m.group(1) == '@&':
                role_id = int(m.group(2))
                role = guild.get_role(role_id)
                return f'@<role: {role.name}>'
            else:
                return m.group(0)


        chat_log = '\n'.join(lines)
        chat_log = re.sub(r'<(@|#|@!|@&)(\d+)>', replace_id_tags, chat_log).strip()

        labels = []
        if thread.parent.id == BUGS_THREAD_ID:
            labels.append('bug')
        elif thread.parent.id == COMPAT_BUGS_THREAD_ID:
            labels.append('bug')
            labels.append('compat')
        elif thread.parent.id == FEATURES_THREAD_ID:
            labels.append('feature')
        
        if '💊' in thread.name:
            labels.append('needs-testing')
        
        # For threads that are too toxic to make public.
        threads_to_elide_chat_log = [
            877733602668970015,
        ]
        if thread.id in threads_to_elide_chat_log:
            chat_log = 'chat log not migrated'

        converted_threads.append(SimpleNamespace(
            discord_thread_id=thread.id,
            title=thread.name,
            created_at=thread.created_at if thread.created_at else messages[0].created_at,
            gh_id=thread_ids_to_gh_num[thread.id],
            gh_author=get_author_github_name(messages[0].author),
            chat_log=chat_log,
            status=determine_status(thread),
            labels=labels,
        ))
    
    for thread in converted_threads:
        timestamp = thread.created_at.strftime("%m/%d/%Y")
        print(f'## {thread.title} (#{thread.gh_id})')
        print(f'{thread.gh_author} opened this issue on {timestamp}\n')
        print(f'Status: {thread.status}\n')
        print(f'Labels: {thread.labels}\n')
        print(f'Source: https://discord.com/channels/{ZC_GUILD_ID}/{thread.discord_thread_id}\n')
        print('\n')
        print(thread.chat_log)

    await bot.close()

# Return a fake handle like `@ FakeAccount` if there is not a known Github account.
def get_author_github_name(author):
    mapping = {
        121155061551202304: '', # Orithan
        121184671777161216: 'TheBlueTophat', # Coolgamer012345
        122462879923437570: '', # Lejes
        127232294145622016: 'arceusplayer11', # Deedee
        152983098500448257: '', # Ether
        187300000135512064: '', # Moosh
        188418153741549568: '', # Changeling
        200811601522196480: '', # FireSeraphim
        206596786331058176: '', # jman2050
        226163329352204288: 'connorjclark', # connorclark
        226885367767236608: '', # InfinityD4
        237743531375067138: '', # naturesucks
        242422436262313986: 'EmilyV99', # EmilyV
        250486281988079618: '', # NightmareJames
        259076371584647171: '', # Tabletpillow
        278342629643517952: '', # Russ
        347808146456313858: '', # Deathrider
        387478496924008448: '', # HeroOfFireZC
        397733275906342915: '', # tacochopper
        424317852947054595: '', # xenomicx
        458089188563353603: '', # P-Tux7
        470443062909468672: '', # Majora
        492893092605853697: '', # cbailey78
        920852345091407934: '', # cbailey78
        505116196828348417: '', # Bagel Meister
        546824565985247253: '', # SkyLizardGirl
        638889207766712330: '', # bigjoe
        701625420277350412: '', # Kirbsblue
        738890034870222898: '', # vlamart
        740387675990786058: '', # carnch
        82603692557078528: '', # Lunaria
        914153766620626945: '', # Lost Attempt
        988168758369607710: '', # C1
        877305063679352917: '', # Saffith
        208727646530437120: '', # 4matsy
        716343681317077002: '', # Alucard648
        277877023966494721: '', # Anthus
        121027900123119616: '', # Einsiety
        160816622767046658: '', # Jared
        896784355375058944: '', # TwilightKnight
        715280883980173364: '', # Guinevere
        225341954018246656: '', # Mitsukara
        126960520812036096: '', # Rambly
        316187823403171840: 'ZoriaRPG', # Timelord
        307150586145669120: '', # Architect Abdiel
        798282693896700004: '', # Bagu
        342451330238906391: '', # Lincolnpepper
        172116882671796225: '', # mitchfork
        275474251111464961: '', # OmegaX
        409803372288409610: '', # bleugriffon2
        154294750248173569: '', # DarkMatt
        852311758982348811: '', # Kampy
        233553576620851200: '', # likelike on fire
        121281283958505472: '', # Rekiron
        116958200351293446: '', # Shane
        249795502864990210: '', # Zaidyer
        456226577798135808: '', # Deleted User
        120939230393401347: '', # Runa 💜🌸
        167018008596840448: '', # aslion
        153057871485992960: '', # Zeo
        180412467673825280: '', # Matthew
        799102708119896094: '', # Chadward Chaddington the 143rd
        161644093359783938: '', # Dr00g
        227563151174926336: '', # Falco
        95557856325021696: '', # HammerGuy
        580163813882724372: '', # Jennette ❣
        192109626911752192: '', # Jigglysaint
        159985870458322944: '', # MEE6
        198922967327965184: '', # Phosphor
        79284655978713088: '', # RetroNutcase
        121099506946146304: '', # Stephen
    }

    if author.id not in mapping:
        print(f'unknown author: {author.name} {author.id}', file=sys.stderr)
    elif mapping[author.id]:
        # Some names are very similar across github/discord. For ones that are not,
        # also show the discord username.
        # if mapping[author.id] in ['connorjclark', 'EmilyV99']:
        #     return f'@{mapping[author.id]}'
        # else:
        return f'@{mapping[author.id]} (discord: {author.display_name})'

    return f'@ {author.display_name}'

bot.run(sys.argv[1])
