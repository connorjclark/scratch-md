## Universal locked doors (#797)
@ Jigglysaint opened this issue on 08/17/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/876906616904101929



=== @ Jigglysaint 08/17/2021 22:45

Create a new thread to request a feature!

=== @ Jigglysaint 08/17/2021 22:48

Or at the very least, have it so that combos such as lock blocks can work like regular locked doors in that they set the unlocked door status for the screen in the approprate dicretion.  It could be done through scripts, but it would be easier to add as a combo.

=== @ Mitsukara 08/20/2021 22:35

I am a little unclear what universal locked doors means

=== @ Mitsukara 08/20/2021 22:36

Are we talking about a lockblock combo you can place anywhere that just unlocks that one combo, permanently? That sounds useful but also maybe a bit tough to implement
## ✅🔒Bug Report String 65 Being Played In Mystical Harps (#798)
@ bigjoe opened this issue on 08/17/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/877180070580604928



=== @ bigjoe 08/17/2021 13:25

Bug Report: In Mystical Harps, the following three screens have a LOT in common, and they all throw a very big error. Picking up any item on them will cause string 65 to be played. They all have the same shop, same string, (possibly) same guy, and two of the same flags set Item Falls From Ceiling, and Hold Up Item.

![image](https://cdn.discordapp.com/attachments/877180070580604928/877181361620934686/unknown.png)

![image](https://cdn.discordapp.com/attachments/877180070580604928/877181397645811722/unknown.png)

![image](https://cdn.discordapp.com/attachments/877180070580604928/877181424720039966/unknown.png)

=== @ P-Tux7 08/17/2021 16:01

non-scripted items, right?

=== @ bigjoe 08/17/2021 16:10

yes, one of the items to which this situation responded did not have any scripts on it, even the janky ass old pickup timer scripts. I had both scripts cleared and this still happened. It happens on these screens. Something about all these screens triggers it, and I TraceS()ed every instance of Screen->Message in the global script

=== @EmilyV99 (discord: Emily) 08/17/2021 16:11

@arceusplayer11 (discord: Deedee) ? Any ideas?

=== @ bigjoe 08/17/2021 16:14

i have a zillion that arent readily apparent, including checking and unchecking every rule that says string in it,  digging into the secondary files, and so on, and ill get to that, but i was thinking since these screens had so much in common something had to be the case

=== @ bigjoe 08/17/2021 16:16

it could be any number of things referencing any number of things 🥵

=== @ P-Tux7 08/17/2021 18:27

check your global script

=== @ SkyLizardGirl 08/18/2021 01:33


![image](https://cdn.discordapp.com/attachments/877180070580604928/877364524020297748/unknown.png)
This is also a map a bug string is on

![image](https://cdn.discordapp.com/attachments/877180070580604928/877364840245633035/unknown.png)

=== @ SkyLizardGirl 08/18/2021 01:44

and a string bug here

![image](https://cdn.discordapp.com/attachments/877180070580604928/877367229686095962/unknown.png)

=== @ SkyLizardGirl 09/04/2021 06:20

Don’t forget other strings were showing also, not just 65

=== @EmilyV99 (discord: Emily) 09/04/2021 06:48

this is fixed
(meta) thread name was changed: 💊🔓Bug Report String 65 Being Played In Mystical Harps

=== @EmilyV99 (discord: Emily) 09/04/2021 08:56

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594) @ SkyLizardGirl

=== @EmilyV99 (discord: Emily) 09/05/2021 10:12

(meta) thread name was changed: ✅🔒Bug Report String 65 Being Played In Mystical Harps
## ⏱🔒Soundfont Support! (#799)
@ RetroNutcase opened this issue on 08/17/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/877316502909509662



=== @ RetroNutcase 08/17/2021 22:22

What it says on the tin. Support soundfonts so we can not be subjected to the awful Windows midi soundfont.

=== @ HammerGuy 08/17/2021 22:42

You can do this through means of a third party program like VirtualMIDISynth.

=== @ RetroNutcase 08/18/2021 01:29

You can, but it's not nearly as convenient. Also, from what I recall, that option isn't without issues, like alt-tab causing all instruments to suddenly become pianos.
Which in turn results in very, VERY unpleasant amounts of ear rape.

=== @EmilyV99 (discord: Emily) 08/20/2021 21:58

Probably not worthwhile to touch this before the rewrite

=== @EmilyV99 (discord: Emily) 08/20/2021 21:59

(meta) thread name was changed: ⏱🔒Soundfont Support!
## Blackout Fade options for specific warps (#800)
@ Mitsukara opened this issue on 08/18/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/877400009706967150



=== @ Mitsukara 08/18/2021 03:54

Currently ZC supports multiple types of black opening wipe (also used by Entrance/Exit combos). These include rectangles from the sides (Z1), Circle, Oval (LTTP), spinning Triangle, and Super Mario All-Stars (tiles).

However, they're set up to work quest-wide with quest rules. It would be neat to be able to set each specific warp to use a specific type of fade. (also to be able to do it without relying on entrance/exit combo warps specifically would be nice, since those mess with continue points). Perhaps a fade in / fade out option on each warp combo somehow? Whatever works.

=== @EmilyV99 (discord: Emily) 08/18/2021 03:58

^sfx too

=== @ Mitsukara 08/18/2021 04:04

ooooh yes, a sfx that doesn't get interrupted by the warp would be awesome

=== @ Mitsukara 11/19/2021 09:03

Reviving this one to add some additional ideas.

- The "static"-y effect from the darkness dithering which clears the screen
- A black rectangle that covers the screen from left to right.

also I didn't clarify this before, but it would be really neat to be able to manually set a fade-in for arriving at a warp, so that you can have it fade out when you leave, then reliably fade in when you arrive (currently this only works on certain kinds of warps, I think maybe Entrance/Exit warps or caves?).
## Clock - Split time stopping and invincibility into separate attributes. (#801)
@ Alucard648 opened this issue on 08/18/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/877423215234928731



=== @ Alucard648 08/18/2021 05:26

As for current ZC version, Clock item cannot stop time without rendering Link invincible at the same time, unlike Castlevania. Here is the link to ancient PureZC forum thread about my futile attempts to do proper time stopping item script.
https://www.purezc.net/forums/index.php?showtopic=62768

=== @ P-Tux7 08/18/2021 06:13

while we're at it
can we make the clock attributes script-writable
link's invincibility and the time stopping (both with args for how much, 0 being "infinite until further notice")
so that if you want a "inventory clock" item you don't have to spawn a literal clock on top of link

=== @ Alucard648 08/18/2021 07:17

(replying to @ P-Tux7 "while we're at it"): 1. Already possible in 2.55 a92
2. I like idea of separate durations.
3. As for Stopwatch, it could keep as is (spawning clocks on top of Link). And add function to check if time id stopped or running.
## ❌🔒Crystal Switch Sparkles (#802)
@ bigjoe opened this issue on 08/18/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/877612587574001726



=== @ bigjoe 08/18/2021 17:59

Crystal Switch - Place LW_SPARKLE Randomly flag. When checked, Crystal Switches will place a random sparkle every 24 frames similarly to how they do in LTTP

=== @ bigjoe 08/18/2021 18:05

eh i guess this can be done with a script

=== @ P-Tux7 08/18/2021 19:17

i was just gonna make a layer overlay

=== @ Mitsukara 08/20/2021 02:52

It would be kind of a neat option. Link's sword also generates sparkles with charging / spinning in LTTP, but I'm not sure I should make a feature request for that, just thought I'd mention it here.

=== @ Dr00g 08/20/2021 20:31

i think the idea of Crystal Switches that affect a combo in a whole Dmap is kinda cool without the use of a bunch of Secret flags,  So like a combo is Crstal A and B and then Crystal block A, B C and D for diffrent colors raised and lowered

=== @EmilyV99 (discord: Emily) 08/20/2021 21:52

You could just have an animated combo for the sparkles
either have the switch combo itself have them, or have a switch block combo on a layer above the switch (switch block so it changes color of sparkle based on the switch state)

=== @EmilyV99 (discord: Emily) 08/20/2021 21:54

the problem being, we don't know exactly what your switch combo will look like, so it wouldn't look the best without a number of ways to configure it... which then clutters up the combo options for one visual feature

=== @ bigjoe 08/20/2021 21:55

ive already solved it with a script, so you can mark this as "better off with a script" I guess. I was just thinking with future LTTP designers in mind

=== @EmilyV99 (discord: Emily) 08/20/2021 21:55

@ Mitsukara for the sword, that probably would be doable, just similarly to arrow sparkles, on a flag, using a weapon sprite from the sprite list. Make a separate thread for that?
(replying to @ bigjoe "ive already solved it with a…"): My point being you don't even need a script, just an animated combo

=== @ Mitsukara 08/20/2021 21:56

That depends on how far off to the sides of the switch the sparkles go, but yeah. Seems low priority in any case

=== @EmilyV99 (discord: Emily) 08/20/2021 21:56

(meta) thread name was changed: ❌🔒Crystal Switch Sparkles

=== @ Mitsukara 08/20/2021 21:56

I wasn't planning to make a request but I will since you asked

=== @EmilyV99 (discord: Emily) 08/20/2021 21:57

worthwhile to have, especially given an 8-bit sword can't flash to show charging
so that would solve that problem
## ✅🔒2-5-0-0 spike compatibility (#803)
@ P-Tux7 opened this issue on 08/18/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/877675906880143460



=== @ P-Tux7 08/18/2021 22:10

https://www.purezc.net/index.php?page=quests&id=536
so what's he on about with the spikes act differently in 2.50.0
(i presume these are normal damage combos in sideview)

=== @ P-Tux7 10/18/2021 17:58

ah, fixed already it would seem, there's a QR for it

=== @arceusplayer11 (discord: Deedee) 10/26/2021 16:07

(meta) thread name was changed: ✅🔒2-5-0-0 spike compatibility
## 💊🔓[2 55] 2.53 emulation menu to automatic rules (#804)
@ P-Tux7 opened this issue on 08/19/2021

Status: needs-testing

Labels: ['bug', 'needs-testing']

Source: https://discord.com/channels/876899628556091432/877733602668970015



chat log not migrated
## (QR Request) Disable Sword and Item Jynx on Respawn (#805)
@ Haylee opened this issue on 08/20/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878102838750892052



=== @ Haylee 08/20/2021 02:27

Discussed in VC already, but I think the name of the thread speaks for itself: The work around for this for years has just been putting Blue Bubbles at the beginning of a dungeon, but this seems like a good idea for a QoL Quest Rule option.
## Slot Machine Enemies from LA Tail Cave (#806)
@ SkyLizardGirl opened this issue on 08/20/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878372545940844565



=== @ SkyLizardGirl 08/20/2021 20:18

Match three enemies up and a secret trigger activates. These are based on the enemies seen in Tail Cave Links Awakening.

=== @EmilyV99 (discord: Emily) 08/20/2021 20:24

This should be a script. Not happening in-engine.

=== @arceusplayer11 (discord: Deedee) 08/23/2021 06:26

hmm... I could see this happening maybe. No promises though.

=== @EmilyV99 (discord: Emily) 08/23/2021 18:46

No new enemy types in engine.
@arceusplayer11 (discord: Deedee)
not happening until rewrite
just fuck no
I fucked with enemies enough
to learn that it just is NOT fucking happening

=== @arceusplayer11 (discord: Deedee) 08/24/2021 06:45

I took a look at it, in hindsight this is a terrible idea for us to do right now
Though, I could write up an npc script that does this at some point.

=== @EmilyV99 (discord: Emily) 08/24/2021 06:50

A script for this would be not that bad
I'd probably make it so you place a single npc, and it spawns 2 "children", doing code to link them

=== @ SkyLizardGirl 08/24/2021 10:32


![image](https://cdn.discordapp.com/attachments/878372545940844565/879674496997527592/image0.png)

=== @ Alucard648 08/27/2021 07:38

Imagine those enemies, but symblos change very fast, like in real slot machine. And getting mismatched combination lesults in Link getting struck by lightning for full heart in damage.
## Kill enemies in order as seen in LA Level-2 (#807)
@ SkyLizardGirl opened this issue on 08/20/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878373410047164426



=== @ SkyLizardGirl 08/20/2021 20:22

Kill enemies in certain order. As seen in Bottle Grotto in Link's Awakening Level-2 as you have to kill a bat, then a Pol, then a skeleton to get the Boss Master Key.

=== @ SkyLizardGirl 08/20/2021 20:23

You should be able to make various 3 monsters be fought in a chosen order. So i am thinking this could be a new kind of Maze room program thing.

=== @EmilyV99 (discord: Emily) 08/20/2021 20:25

This should be a script. Not happening in-engine.

=== @arceusplayer11 (discord: Deedee) 08/23/2021 06:13

(replying to @EmilyV99 (discord: Emily) "This should be a script. Not…"): Hold on there, this seems easy enough to add and I can see cool stuff being made with this.

=== @EmilyV99 (discord: Emily) 08/23/2021 18:46

`easy enough`? 🤢 🤮
## ⏱🔒Screen Scrolling and setting Scroll via Dmap (#808)
@ Dr00g opened this issue on 08/20/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878373813304320051



=== @ Dr00g 08/20/2021 20:23

So asking for ALTTP style Screen Scrolling  is nothing new. but I had this concept of setting in the Dmap simialr to drawing the Dungeon map where you can connect screens and those screens has the LTTP Screen Scrolling while other Screens have the Zelda 1 style

=== @EmilyV99 (discord: Emily) 08/20/2021 20:25

Not happening until the full rewrite, at which point it's already planned.

=== @EmilyV99 (discord: Emily) 09/21/2021 01:39

(meta) thread name was changed: ⏱🔒Screen Scrolling and setting Scroll via Dmap
## ❌🔒Horse Knight Head Puzzles built in From LA Level-6 (#809)
@ SkyLizardGirl opened this issue on 08/20/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878374373554270268



=== @ SkyLizardGirl 08/20/2021 20:26

The Knight horse heads are tiles that need to be struck to match up with the other tiles, much like the slot machine enemies do 2 or 3 or 4 will do at max. These Can be found in Level-6 Link's awakening. Idea is for a built in system like this.

=== @EmilyV99 (discord: Emily) 08/20/2021 20:26

This should be a script. Not happening in-engine.

=== @arceusplayer11 (discord: Deedee) 08/23/2021 06:26

Yeah probably not happening, way too complex

=== @EmilyV99 (discord: Emily) 08/23/2021 18:46

(meta) thread name was changed: ❌🔒Horse Knight Head Puzzles built in From LA Level-6
## Sword sparkles option (#810)
@ Mitsukara opened this issue on 08/20/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878397763476406404



=== @ Mitsukara 08/20/2021 21:59

In LTTP, Link's sword creatse sparkles (basically LW_SPARKLE) which move up the tip of Link's sword while charging / sit in front of the tip when charged, and then his spin attack also creates sparkles around the sword. 

Some approximation of this, creation LW_SPARKLES on the LW_SWORD during LA_CHARGING and LA_SPINNING, would be a neat option in-engine (though it's not that hard to do with scripts, so low priority).

=== @EmilyV99 (discord: Emily) 08/20/2021 22:00

^ More priority to this, because it resolves a major issue of 8-bit sword sprites not being able to display charge progress

=== @ Mitsukara 08/20/2021 22:01

In LTTP, Link's sword creates sparkles which move up the tip as he charges, then appear near the front of the tip when charged, and then continues to make sparkles around the sword during the spin attack.

Something similar could be achieved by creating LW_SPARKLEs on the LA_SWORD during LA_CHARGING and then during LA_SPINNING, which would be neat. (Although this can be mostly handled by scripts, scripts have no way of telling how far along the charge progress is so you can't really do the move-forward-on-the-blade effect). Alternatively you could wait for the sparkles to appear at all until charging is done.

=== @EmilyV99 (discord: Emily) 08/20/2021 22:01

would use an item flag to enable, and a `Sprites[]` sprite for the sparkle

=== @ Mitsukara 08/20/2021 22:02

Ah, whatever works
it is worth noting the position of the sparkles shifts a bit. The ones on the tip seem to move from side to side a bit.

=== @EmilyV99 (discord: Emily) 08/20/2021 22:02

^ Review LTTP before implementation
## Fade All CSets on Side Warp (#811)
@ mitchfork opened this issue on 08/21/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878696152533467206



=== @ mitchfork 08/21/2021 17:44

When you change DMap palettes via side-warp, the level CSets fade to black and fade back in on the next screen.  Requesting a QR to apply this to all CSets (except 6)
this prevents the following from happening with combos in sprite CSets:

![image](https://cdn.discordapp.com/attachments/878696152533467206/878696277225922560/daughters_05.mp4)
Where the NPC/campfire appear before everything else

=== @ Shane 08/21/2021 18:14

Yes. please.

=== @ P-Tux7 08/21/2021 20:44

this should only apply for interpolated fading since of course manual dark room palettes don't have enough room to store all 11 csets' worth of fade palettes
## Option to have Items that Change NPC Sprite or Player Csets (#812)
@ Dr00g opened this issue on 08/21/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878737159480287282



=== @ Dr00g 08/21/2021 20:27

Example: an "Ice Wand" Item where the Beam of the wand Stuns an enemy and changes them to a light blue  or a Enemy covers the player in Ink turning them black color

=== @EmilyV99 (discord: Emily) 08/21/2021 20:29

Ice weapon type and freeze status effect are already planned

=== @ P-Tux7 08/21/2021 20:42

is link's ESP cset writable?

=== @EmilyV99 (discord: Emily) 08/21/2021 20:51

the freeze effect will have some mechanic for changing palette

=== @EmilyV99 (discord: Emily) 08/23/2021 18:54

(Keep in mind, that this needs to wait until FFC/NPC *solidity* is done)
## Ability to set how many enemies an Arrow can pierce (#813)
@ Jennette ❣ opened this issue on 08/22/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878975836563316776



=== @ Jennette ❣ 08/22/2021 12:16

What it says on the tin. Being able to set this would be nice for weapon balancing reasons.

=== @EmilyV99 (discord: Emily) 08/23/2021 18:53

The main thing that I see being problematic here is how to store how many it's already pierced
will need to find an open variable for that, or add a new var to all weapons
....but that's not that bad. And the item editor setup would just be an attribute.
## arrows through torch combo effect (#814)
@ Jennette ❣ opened this issue on 08/22/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/878979827967856710



=== @ Jennette ❣ 08/22/2021 12:32

This could have several behaviors that are seen in official Zelda games.

For starters:

Shooting through it with an arrow could give it fire properties

As well, if a torch combo is on screen it could make a screen count as "lighted" in the context of dark rooms. This could be helpful for a variety of reasons, such as if people don't want the candle itself to provide light, if they want temporary light from lit torches or if they want a screen where you have to light torches to permanently light it up.

=== @EmilyV99 (discord: Emily) 08/22/2021 13:56

Nooope, not touching this until rewrite.

=== @ P-Tux7 08/22/2021 18:50

didn't you make them for mm2d
also lit torches are extremely screwy in zc as-is

=== @EmilyV99 (discord: Emily) 08/22/2021 18:50

that's a script
this is feature requests channel, so, for engine

=== @ P-Tux7 08/22/2021 18:51

oh well

=== @EmilyV99 (discord: Emily) 08/22/2021 18:51

also, it's a bad script

=== @ P-Tux7 08/22/2021 18:51

so the issue with lightable torches would be that every combo animation timer runs on the same cycle
so let's say you light up one torch
the next torch you light up would either extend the animation of the first torch, should the combo be set to restart animation upon being cycled to
or it would extinguish when the first torch extinguishes, if the combo is NOT set to do that
you'd have to make each unlit and lit torch a separate combo

=== @EmilyV99 (discord: Emily) 08/22/2021 18:53

^not necessarily
you could make a bunch of combos, each of which lasts for 1 frame before cycling to the next
then they'd effectively run on their own timers

=== @ P-Tux7 08/22/2021 18:54

neat also that's viscerally disgusting

=== @EmilyV99 (discord: Emily) 08/22/2021 18:54

yep
but yeah, this should wait for full rewrite
I think in the rewrite we'll probably have real fucking darkness
like, with circles of light, ala lttp
because having that in engine would be nice

=== @EmilyV99 (discord: Emily) 08/22/2021 22:04

(meta) thread name was changed: ⏱🔒Torch combo

=== @EmilyV99 (discord: Emily) 02/02/2022 04:47

@arceusplayer11 (discord: Deedee) did you do something with arrows through torches, or was that just an idea?

=== @arceusplayer11 (discord: Deedee) 02/02/2022 04:56

It's the next major feature I was planning to touch
I've just been focusing on bugfixes

=== @EmilyV99 (discord: Emily) 02/02/2022 05:00

(meta) thread name was changed: arrows through torch combo effect
this thread is horrendously outdated lol
was just digging through archived reqs

=== @ P-Tux7 02/02/2022 14:55

so animated arrows are part of the 4 way weapon fix right
## ✅🔒Damage Ring (#815)
@EmilyV99 (discord: Emily) opened this issue on 08/22/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879069779443474502



=== @EmilyV99 (discord: Emily) 08/22/2021 18:29

So, whimsical ring gives you a chance to crit on attacks. Why not add a damage ring, to give a bonus and/or multiplier to damage *always*, similarly to the basic ring's defense for Link?

=== @EmilyV99 (discord: Emily) 08/22/2021 20:57


![image](https://cdn.discordapp.com/attachments/879069779443474502/879107045914185798/unknown.png)

![image](https://cdn.discordapp.com/attachments/879069779443474502/879107081549013002/unknown.png)
(based on:
![image](https://cdn.discordapp.com/attachments/879069779443474502/879107179859296336/unknown.png)
....this was way too fucking easy to add.

=== @EmilyV99 (discord: Emily) 08/22/2021 22:04

(meta) thread name was changed: ✅🔒Damage Ring
## Auto-Label InitD[] (#816)
@EmilyV99 (discord: Emily) opened this issue on 08/22/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879080001889267794



=== @EmilyV99 (discord: Emily) 08/22/2021 19:10

Add a QR to autofill InitD[] labels from ZASM metadata for the selected script

=== @EmilyV99 (discord: Emily) 08/22/2021 19:11

(If enabled, InitD labels will stop being editable, and will auto-populate from whatever script is assigned)
(Item scripts, and Active/Passive Subscreen Scripts, will pull from the `Action`/`Active` script metadata)

=== @ Alucard648 08/22/2021 20:57

Fantastic! This will save some headache for quest designers so you don`t have to check script setup instructions to remember which D input which setting defines, especially for complex scripts.
## ✅🔒InitData Stuff (#817)
@EmilyV99 (discord: Emily) opened this issue on 08/22/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879126246724870224



=== @EmilyV99 (discord: Emily) 08/22/2021 22:13

Fuck me
https://cdn.discordapp.com/attachments/704505093428478013/879125057228668938/unknown.png
working on this
because, needs doing

=== @EmilyV99 (discord: Emily) 08/23/2021 04:22

done
(meta) thread name was changed: ✅🔒InitData Stuff
## ❌🔒Baked in FFC Scrpits? (#818)
@ Dr00g opened this issue on 08/23/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879155184289349663



=== @ Dr00g 08/23/2021 00:08

I've been mostly thinking about how useful the Newbie Boss and Item Scripts are while not hard to just add in though perhaps adding more diversity to the Enemy and Item editor would be better then having to make new enemy's and items from scratch.

=== @EmilyV99 (discord: Emily) 08/23/2021 18:53

err, so what's the feature request?

=== @ Dr00g 08/23/2021 19:47

Sorry I got off track the Orignal idea was to update the Enemy and Item editors to be more like those Scripts allowing more complex ememies and bosses and Items

=== @EmilyV99 (discord: Emily) 08/23/2021 19:48

so, uh, no
not before the full rewrite
(meta) thread name was changed: ❌🔒Baked in FFC Scrpits?
## EW_BOMBSTATIONARY (#819)
@ Mitsukara opened this issue on 08/23/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879156022781046835



=== @ Mitsukara 08/23/2021 00:12

It would be neat to have an eweapon bomb that behaved like Link's bomb, sitting in place and then exploding after a few moments. This is basically the Sluggula bombs from A Link to the Past (in Misery Mire). 

But I know there's a lot of dev stuff to do and not sure how hard adding new eweapon types/behaviors is, so no worries.

=== @ Dr00g 08/23/2021 00:14

It would be interesting to see more enemies use player like weapons.

=== @EmilyV99 (discord: Emily) 08/23/2021 18:52

Weapon types aren't that bad afaik
could be worthwhile
## ✅🔒Script counter InitD (#820)
@EmilyV99 (discord: Emily) opened this issue on 08/24/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879580318036820028



=== @EmilyV99 (discord: Emily) 08/24/2021 04:18

Allow setting starting/max counters for script counters in InitD. Long fucking overdue.....

=== @ Moosh 08/24/2021 04:38

If this ends up being a thing can they also be added to the cheat menu?

=== @EmilyV99 (discord: Emily) 08/24/2021 04:41

I want to say those are actually the same dialog
so, that should be automatic

=== @EmilyV99 (discord: Emily) 09/28/2021 15:17

(meta) thread name was changed: ✅🔒Script counter InitD
## ✅🔒clocks permanent with cheats on (#821)
@EmilyV99 (discord: Emily) opened this issue on 08/25/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/879908764696862771



=== @EmilyV99 (discord: Emily) 08/25/2021 02:03

https://www.purezc.net/forums/index.php?showtopic=77154#entry1065195

=== @EmilyV99 (discord: Emily) 09/21/2021 01:38

I think I fixed this months ago and forgot to mark it... whoops
(meta) thread name was changed: ✅🔒clocks permanent with cheats on
## Allow customizing SFX for ZScript compilation outcome. (#822)
@ Alucard648 opened this issue on 08/25/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879918730371551294



=== @ Alucard648 08/25/2021 02:42

Not everyone likes to hear poor Link die every time ZScript fails to compile. An option to replace that horrible sound with different one, like explosion SFX, would be great.

=== @ mitchfork 08/25/2021 02:52

this is actually already possible

=== @EmilyV99 (discord: Emily) 08/25/2021 02:52

check zquest.cfg

=== @ mitchfork 08/25/2021 02:52

it's at the top of zquest.cfg
ye
the numbers for all the samples are just SFX ID's for the quest file
and you can set the volume too

=== @ Alucard648 08/25/2021 02:58

Tried to change SFX, but it resets to default every time ZQuest is restarted.

=== @EmilyV99 (discord: Emily) 08/25/2021 02:58

Oh?
let me check on that

=== @EmilyV99 (discord: Emily) 08/25/2021 03:12

I don't see any reason why changing `compile_error_sample` wouldn't be changing the error sound

=== @ Alucard648 08/25/2021 03:14

Tried again. Now it worked, all of the sudden. Perharps, sound options should be available in compiler settings of ZQuest editor, especially as compiler options dialog is almost empty in 2.53.x .
## ⏱🔒Sideview slopes and stairs (#823)
@ Alucard648 opened this issue on 08/25/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/879934130299744276



=== @ Alucard648 08/25/2021 03:44

Something like in Link stuck in Castlevania.
Hoping it does not require complete rewriting.

![image](https://cdn.discordapp.com/attachments/879934130299744276/879934189632360468/zc_screen00010.png)

=== @EmilyV99 (discord: Emily) 08/25/2021 03:44

Not happening until the rewrite, in-engine
just, by god, painful code
BUT

=== @ bigjoe 08/25/2021 03:45

much love for this idea though

=== @EmilyV99 (discord: Emily) 08/25/2021 03:45

@TheBlueTophat (discord: Coolgamer012345) made a ramps script recently that works fucking beautifully

=== @ bigjoe 08/25/2021 03:46

you know ive often wondered... what if trick scripts could be implemented into the engine and at a user level, it would seem like functional engine stuff

=== @EmilyV99 (discord: Emily) 08/25/2021 03:49

not without rewriting everything
what you are describing is called a sane system
which zc is not

=== @TheBlueTophat (discord: Coolgamer012345) 08/25/2021 04:20

Yeah I still uhhh
need to finish it technically
however
most of it works
could be rigged up to work in a quest with most functionality.

=== @TheBlueTophat (discord: Coolgamer012345) 08/25/2021 04:23

I should post the latest code when I get the chance to.

=== @ Alucard648 08/25/2021 04:50

(replying to @TheBlueTophat (discord: Coolgamer012345) "I should post the latest code…"): Feel free to post this in purezc.net forum under Sripting discussion section.

=== @arceusplayer11 (discord: Deedee) 08/28/2021 23:54

Actually... I think a QR that lets Link step up small steps in sideview would be dead simple
I'll give this a look once I'm done with Sideview Swimming (which is still pain btw!)

=== @EmilyV99 (discord: Emily) 08/28/2021 23:57

(replying to @EmilyV99 (discord: Emily) "Not happening until the rewri…"): ^
(meta) thread name was changed: ⏱🔒Sideview slopes and stairs
## ❌🔒PlayOgg bugs (#824)
@arceusplayer11 (discord: Deedee) opened this issue on 08/25/2021

Status: wont-fix

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/880199477015744512



=== @arceusplayer11 (discord: Deedee) 08/25/2021 21:18

PlayOGG and GetPos/SetPos are bugged currently. I think GetPos was the issue, but one of the two just outright crashes
@EmilyV99 (discord: EmilyV) could you possibly give this a glance to see if there's anything obviously wrong? If not, I might have to give this a more in depth look, cause it worked at some point

=== @EmilyV99 (discord: Emily) 08/25/2021 21:20

I just traced GetPos and found no issues down to the call to `alogg_get_pos_msecs_ogg`

=== @arceusplayer11 (discord: Deedee) 08/25/2021 21:21

Does GetPos crash when used with PlayOgg?

=== @EmilyV99 (discord: Emily) 08/25/2021 21:21

that function is being called, and passed a non-null `ALOGG_OGG` object
unsure
you said you thought it was the issue so I traced it
don't have a test quest or test files

=== @EmilyV99 (discord: Emily) 08/25/2021 21:25

SetPos seems identically set up

=== @ Ether 08/25/2021 21:26

Is it possible that the OGG glitch I was experiencing in 253.1 is related to this? It's Yuurand, soooooooo I don't know how helpful it would be compared to something more isolated for this, but.

=== @EmilyV99 (discord: Emily) 08/25/2021 21:26

no
this is a new 2.55 feature

=== @ Ether 08/25/2021 21:26

Got it.

=== @EmilyV99 (discord: Emily) 08/25/2021 21:26

for zscript managing oggs

=== @arceusplayer11 (discord: Deedee) 08/25/2021 21:32

(replying to @EmilyV99 (discord: Emily) "don't have a test quest or te…"): I went to dig up a test quest but my organization is bad and I think onedrive ate it\
*sigh*

=== @EmilyV99 (discord: Emily) 08/25/2021 21:32

fun
I don't see anything immediately wrong
so, probably gonna take digging

=== @arceusplayer11 (discord: Deedee) 08/25/2021 21:32

lovely.
Gonna be pissed if it ends up being a zoriaism

=== @arceusplayer11 (discord: Deedee) 10/12/2021 00:50

SetPos is the issue
but I don't know what the hell it even is
that's why using obscure libraries is bad v.v

=== @arceusplayer11 (discord: Deedee) 10/12/2021 20:39

(meta) thread name was changed: ❌🔒PlayOgg bugs
## Separate int Weapon Properties (#825)
@ Guinevere opened this issue on 08/26/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880512585793929267



=== @ Guinevere 08/26/2021 18:02

To add a speck of more customization to the Weapon Tab on the Item Editor.
Maybe have it to where triggering properties and enemy defenses are separate.
For example, being able to get the properties of the sword without applying its enemy defense.
Maybe as an item/rule flag that says "Lweapons On Items Don't Affect Defenses".
## ✅🔒book damage bug (#826)
@EmilyV99 (discord: Emily) opened this issue on 08/26/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/880554702096437308



=== @EmilyV99 (discord: Emily) 08/26/2021 20:50

https://www.purezc.net/forums/index.php?showtopic=77135#entry1065255

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:47

Fixed!
(meta) thread name was changed: ✅🔒book damage bug
## 🔓Messagestring shadows (#827)
@EmilyV99 (discord: Emily) opened this issue on 08/27/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880750852841807902



=== @EmilyV99 (discord: Emily) 08/27/2021 09:49

Shadows ala subscreen editor / DrawString, but, in the string editor per-string
@ Mitsukara

=== @ Mitsukara 08/27/2021 09:49

Nice! Thank you

=== @EmilyV99 (discord: Emily) 09/05/2021 00:01

(meta) thread name was changed: 🔓Messagestring shadows

=== @EmilyV99 (discord: Emily) 09/05/2021 05:03

@ Mitsukara
![image](https://cdn.discordapp.com/attachments/880750852841807902/883940448559845416/unknown.png)

=== @EmilyV99 (discord: Emily) 09/05/2021 05:08

still needs script access!

=== @ Mitsukara 09/05/2021 05:38

Like for Screen->DrawString?

=== @EmilyV99 (discord: Emily) 09/05/2021 05:39

that already has shadow options
has for like, 1.5 years IIRC?
more, `messagedata->ShadowType`, `messagedata->ShadowColor`
for editing the string editor strings

=== @ Mitsukara 09/05/2021 05:40

oh, nice
I didn't realize
## non-sideview sideview ladders (#828)
@EmilyV99 (discord: Emily) opened this issue on 08/27/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880918639031771198



=== @EmilyV99 (discord: Emily) 08/27/2021 20:56

https://www.purezc.net/forums/index.php?showtopic=77164#entry1065295
## ✅🔒Solid Damage Combo Active Effect Bug (#829)
@ Guinevere opened this issue on 08/27/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/880923904066060358



=== @ Guinevere 08/27/2021 21:17

When i make a solid damage combo that is where the effect is only on 3 or less areas, the hitbox seems to only register in specific spots instead of the whole section where the effect is active.

![image](https://cdn.discordapp.com/attachments/880923904066060358/880923960315904020/Screenshot_2021-08-27_141525.png)

![image](https://cdn.discordapp.com/attachments/880923904066060358/880924062673686608/2021-08-27-14-16-20.mp4)

=== @EmilyV99 (discord: Emily) 08/27/2021 21:17

@arceusplayer11 (discord: Deedee)

=== @arceusplayer11 (discord: Deedee) 08/27/2021 21:21

that... seems very consistent with what I know of solid damage combos
solid damage combos are not well designed

=== @ Guinevere 08/27/2021 21:23

i see

=== @arceusplayer11 (discord: Deedee) 08/27/2021 21:25

ill give it a look

=== @ Guinevere 08/27/2021 21:26

thank ya kindly
<:catpat:732463715579985953>

=== @arceusplayer11 (discord: Deedee) 10/11/2021 20:00

Fixed, I think!

=== @arceusplayer11 (discord: Deedee) 10/11/2021 20:11

(meta) thread name was changed: ✅🔒Solid Damage Combo Active Effect Bug

=== @arceusplayer11 (discord: Deedee) 10/11/2021 20:20

@ Guinevere expect next alpha to have a fix for this (hopefully)
## SCC for Game-Generic (#830)
@EmilyV99 (discord: Emily) opened this issue on 08/27/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880924358212747355



=== @EmilyV99 (discord: Emily) 08/27/2021 21:18

Add "Goto if generic" SCC, similar to "Goto if screen register". Useful for Heart Piece strings.
## more level palette csets (#831)
@EmilyV99 (discord: Emily) opened this issue on 08/27/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880931900330508360



=== @EmilyV99 (discord: Emily) 08/27/2021 21:48

https://www.purezc.net/forums/index.php?showtopic=77093
```
P-Marx7 — 08/08/2021
okay so amend that to csets 0-13 since zoria said he enabled using them for combos in the newest alphas
one or both of them get overwritten by the boss palette for enemies that use an extra sprite palette, but that shouldn't be a problem if one just never uses that option
Emily — 08/08/2021
This'll be a tremendous amount of work
So, I'll get around to attempting it when I have the requisite energy
P-Marx7 — 08/08/2021
Dimi's done great work so far. Is she up to it?
Emily — 08/08/2021
Maybe, but IDK how much experience with palette stuff she has
Meanwhile the literal second thing I did in ZC was tint
P-Marx7 — 08/09/2021
@Timelord i should mention we also could use this for outlands module, the NES equivalent of csets 7 and 8 are different in dungeons on the NES version
P-Marx7 — 08/09/2021
@tiny little shark ?
tiny little shark — 08/09/2021
Im at work now but ill look into later
P-Marx7 — 08/15/2021
Okay so as for the Z3 tileset, let's compare how the palette changes outside Link's house and inside his house in the original game
Outside

Inside

That appears to be six tile CSets that change per-area, and about one CSet's worth of sprite CSets that change (though given that they seem to be for "things that look like tiles that are actually sprites", such as lifted pots, rocks, and bushes, they might be able to be conflated into 6 per-level CSets. Still, at least 6 per area)
P-Marx7 — 08/15/2021
@Timelord you want a z3 tileset here's something for you to do
the secrets->nextcombo flag that emily added without your permission and the triggers secrets combo trigger attribute dimi added without your permission is also doing wonders for that tileset too by the way
now i can just make a 2x2 rock alias, set it to be bomb-triggerable, and have the ->next combos be the staircase, so the zquest user can place all that in one click without needing to place flags or set the screen's secret combos
that's why i made #lttp-rips and have been updating it the past few days
even set up a goriya enemy's big enemy tiles and screenshotted the correct enemy size parameters if you want a preview of what the tileset will be like once the more csets thing is sorted out```
https://cdn.discordapp.com/attachments/871580485304877067/876600358829453322/unknown.png
https://cdn.discordapp.com/attachments/871580485304877067/876600418413719562/unknown.png
@ P-Tux7

=== @ P-Tux7 08/27/2021 21:50

```okay so amend that to csets 0-13 since zoria said he enabled using them for combos in the newest alphas```
Yeah this is out of date since apparently it's just back to csets 0-11 now

=== @EmilyV99 (discord: Emily) 08/27/2021 21:51

aye, that was an error on zoria's part
csets above 11 are used for hardcoded shit
and should never be available for combos

=== @ P-Tux7 08/28/2021 02:38

i should also mention that don't feel compelled to do this any time soon
given that once i get over covid my attention will be drawn to a custom tileset which doesn't need this

=== @ P-Tux7 10/04/2021 16:14

i should mention that due to this taking up 12 csets in each DPal
this will necessarily disable manual dark rooms, interpolated fading only
## No Link Jump flag (#832)
@ Mitsukara opened this issue on 08/28/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/880992709710585878



=== @ Mitsukara 08/28/2021 01:50

A combo flag which prevents Roc Items from initiating a jump if Link is standing on the flag.
(meta) thread name was changed: No Link Jump flag

=== @EmilyV99 (discord: Emily) 08/28/2021 02:09

....that sounds STUPIDLY simple. Question: How sensitive do you think it should be?

=== @ Mitsukara 08/28/2021 02:19

Hmm. I think a good range is about 4 pixels onto the flag, but some people might want more, or less, hard to say without fiddling with it

=== @EmilyV99 (discord: Emily) 08/28/2021 02:21

4 pixels is the standard for standing on a platform in sideview, so makes sense
and I think it's also the amount for the little side-push thing
## ✅🔒Sword charging stops during scrolling (#833)
@ Mitsukara opened this issue on 08/28/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/881003756475523172



=== @ Mitsukara 08/28/2021 02:34

In official Zelda games, Link's sword charge is maintained when he scrolls to another screen. In ZC, the sword charge stops and he has to attack and start over on the next screen.
If fixed, it might be good to have some kind of backwards compatability/QR/item flag/etc for the old behavior, in case someone wanted that for some reason. (Although it kinda sucks and makes the charge way less useful)
Not sure if having slash enabled would be relevant when fixing this either, because I know you have a slightly different spin attack when you don't know slash (it moves 4 ways instead of 8, which is really cool)

=== @ P-Tux7 08/28/2021 02:36

yeah this is slightly bs when the spin attack or hurricane spin cost magic to use

=== @EmilyV99 (discord: Emily) 08/28/2021 02:38

there has to be a qr, of course
otherwise old quests would be broken

=== @EmilyV99 (discord: Emily) 02/07/2022 09:48

The problem here is probably that the sword sprite dies during the scrolling
....that might require some interesting workarounds.

=== @ P-Tux7 02/07/2022 10:11

i presume it would check the charge timer like how nayru's love regenerates itself and checks the time left after scrolling
if the sword charge timer and state aren't global like the nayru's love time left timer is... eep
i guess that would need to be changed

=== @EmilyV99 (discord: Emily) 02/07/2022 10:13

My thing is, I don't immediately see why it would be being cleared in the first place, aside from the sword weapon being killed during scrolling

=== @EmilyV99 (discord: Emily) 02/07/2022 10:16

ah no, a couple clocks are cleared in `resetflags()`
the weapon would still be a problem though I think

=== @EmilyV99 (discord: Emily) 02/07/2022 10:29


![image](https://cdn.discordapp.com/attachments/881003756475523172/940192644397662218/unknown.png)
....surprisingly, the weapon exists on the new screen just fine
but uhh
it gets a bit stuck
wherever you scrolled
and doesn't move with you
hmmmm

=== @arceusplayer11 (discord: Deedee) 02/07/2022 10:36

(replying to @EmilyV99 (discord: Emily) "and doesn't move with you"): there was a similar issues involving setting Link's direction
I forget exactly what the cause was though

=== @EmilyV99 (discord: Emily) 02/07/2022 10:47

pffft
`action` is being cleared
he's walking around with `LA_NONE`

=== @EmilyV99 (discord: Emily) 02/07/2022 10:51

@ Mitsukara
https://cdn.discordapp.com/attachments/881003756475523172/940198077053173780/buildpack.zip
(meta) thread name was changed: ✅🔒Sword charging stops during scrolling

=== @EmilyV99 (discord: Emily) 02/09/2022 15:19

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
## ✅🔒Scrolling Crash Bug? (#834)
@ Guinevere opened this issue on 08/28/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/881030279479820299



=== @ Guinevere 08/28/2021 04:19

Okay. so...I have no idea what's causing this, the areas where it happens are inconsistent between quests, but are consistent in where they happen. At first I thought it was a gollab bug since the screen scrolling was tied to a scripted warp pad so i just thought that it was just not applicable to 2.55.
But apparently some quests if the screen scrolls in specific areas, ZC crashes. They don't even need to be scripted quests.
And I know that it's not just a backwards compatibility bug because it also happens in my project as well.

=== @ Guinevere 08/28/2021 04:21

<:nekosweat:694455509423751239>

=== @EmilyV99 (discord: Emily) 08/28/2021 04:31

2.53? 2.55? Both?
@arceusplayer11 (discord: Deedee) ?
Is smart scrolling enabled in the quest? Is Smarter Smart Scrolling enabled, if in 2.55?

=== @ Guinevere 08/28/2021 04:32

2.55

=== @ P-Tux7 08/28/2021 04:34

what's smarter screen scrolling

=== @ Guinevere 08/28/2021 04:35

umm idk about the other quests
but "fixed smart scrolling" is disabled in my quest

=== @EmilyV99 (discord: Emily) 08/28/2021 04:35

k, so isn't that
given @arceusplayer11 (discord: Deedee)'s work with scrolling shit, feel like she is probably more qualified to look at this

=== @ Guinevere 08/28/2021 04:36

i'm removing my zc.sav to see if it's just a save corruption

=== @ Guinevere 08/28/2021 04:39

nope it's not just a save corruption

=== @ Mitsukara 08/28/2021 05:42

I totally forgot to report it, but I know that in 2.50.2 or 2.53 I was trying some random quest off the database that had no scripts, but used the Smart Scrolling feature, and trying to scroll onto a solid combo while swimming crashed ZC I think
so that may be relaetd

=== @ Guinevere 08/28/2021 05:47

i see.

=== @EmilyV99 (discord: Emily) 08/28/2021 06:04

oh????

=== @ Guinevere 08/28/2021 06:04

(meta) thread name was changed: Smart Screen Scrolling hardcoded to be enabled

=== @EmilyV99 (discord: Emily) 08/28/2021 06:04

@arceusplayer11 (discord: Deedee) wtf

=== @arceusplayer11 (discord: Deedee) 08/28/2021 13:18

??????

=== @EmilyV99 (discord: Emily) 08/28/2021 13:37

(replying to deleted comment): what is this screenshot intended to show?

=== @ Guinevere 08/28/2021 16:34

................
wait
no?
*HUH*?

=== @ Guinevere 08/28/2021 16:46

(meta) thread name was changed: Scrolling Crash Bug?

=== @ Guinevere 08/28/2021 16:47

Forget everything i just said, for it's foobar, i have no idea what's causing zc to crash when the player scrolls
<:nekobleh:749523485373497375>
*wait*
AHAH!

=== @ Guinevere 08/28/2021 16:59

when fixed screen scrolling is enabled;
if there are solid combos at one edge of the screen,  and nothing on the opposite edge, it blocks link from scrolling that way where the solid combos would be like if they were on the next screen in the same position.
![image](https://cdn.discordapp.com/attachments/881030279479820299/881221514903580712/2021-08-28-09-56-44.mp4)

=== @ Guinevere 08/28/2021 17:01

@EmilyV99 (discord: EmilyV) @arceusplayer11 (discord: Deedee)

=== @arceusplayer11 (discord: Deedee) 08/28/2021 17:07

Wtf

=== @ Guinevere 08/28/2021 17:07

ye idk either

=== @arceusplayer11 (discord: Deedee) 08/28/2021 17:08

(replying to @ Mitsukara "I totally forgot to report it…"): Oh goddamnit i know what that is
I saw a weird check where swimming seemed to ignire dmart scrolling
Dmart scrolling. Where you scroll to a d mart

=== @ Guinevere 08/28/2021 17:09

<:teehee:620404816769843200>

=== @ Guinevere 08/28/2021 19:00

Idk if this is the thing causing zc to crash in some quests when you scroll in specific areas, but the possibility is there.

=== @ Guinevere 08/31/2021 03:19

Here's also an example of a quest crashing when trying to scroll the screen. To my knowledge First Quest Layered (the quest being played) isn't scripted at all.
![image](https://cdn.discordapp.com/attachments/881030279479820299/882102390738813028/2021-08-30-20-17-28.mp4)

=== @ Guinevere 08/31/2021 04:06

idk why but sometimes it takes a couple times to scroll, but other times it only takes one attempt to crash

=== @EmilyV99 (discord: Emily) 08/31/2021 04:09

does it consistently do it on a specific transition?
if so, could you send a copy of the quest where you spawn in the room in question?
(Crashes are easier to debug than less serious bugs, because if I run it in the debugger, it will literally tell me what line of code crashed)
(but, need to do that in a debug build, attached to the dev chain, so gotta do it myself

=== @ Guinevere 08/31/2021 04:13

uhh, how do i set a spawn in someone else's quest?

=== @EmilyV99 (discord: Emily) 08/31/2021 04:13

oh is it passworded?

=== @ Guinevere 08/31/2021 04:13

ye

=== @EmilyV99 (discord: Emily) 08/31/2021 04:13

just send it then
I can bypass passwords

=== @ Guinevere 08/31/2021 04:14

oh okie

https://cdn.discordapp.com/attachments/881030279479820299/882116153718214707/First_Quest_Layered.qst
here ya go

=== @EmilyV99 (discord: Emily) 08/31/2021 04:56


![image](https://cdn.discordapp.com/attachments/881030279479820299/882126605168807946/unknown.png)
love when the actual crash line it gives me is inside a C++ class, so it doesn't tell me where the call is that crashed....
but, at least I recreated it
so I can debug from there

=== @ Guinevere 08/31/2021 04:56

i see

=== @EmilyV99 (discord: Emily) 08/31/2021 05:12

It's not the scrolling code
the scrolling code isn't even fucking running
it's crashing before it gets there

=== @ Guinevere 08/31/2021 05:12

i see
that makes sense
since you don't even see the screen scroll once it crashes
but surprised that the code has nothing to do with it

=== @EmilyV99 (discord: Emily) 08/31/2021 05:19

....it's fucking related to SWITCH BLOCKS
WHAT THE FUCK

=== @ Guinevere 08/31/2021 05:19

>.>
wut?

=== @ Guinevere 08/31/2021 05:21

I don't even wanna ask *how* that works

=== @EmilyV99 (discord: Emily) 08/31/2021 05:22

Some of the switchblock code
is referencing something out of bounds
because of the X/Y position of Link being offscreen

=== @ Guinevere 08/31/2021 05:22

uh huh

=== @EmilyV99 (discord: Emily) 08/31/2021 05:26

fixed

=== @ Guinevere 08/31/2021 05:26

<:nekopog:835231816620965948>
You are a life saver
way to go

=== @arceusplayer11 (discord: Deedee) 08/31/2021 20:01

(replying to @EmilyV99 (discord: Emily) "....it's fucking related to S…"): Is it the exact same crash that you fixed for me the other day?

=== @EmilyV99 (discord: Emily) 08/31/2021 21:01

?

=== @arceusplayer11 (discord: Deedee) 08/31/2021 23:07

you know, the bomb wall switch block crash
I don't think that fix ever got pushed

=== @EmilyV99 (discord: Emily) 08/31/2021 23:12

I don't recall that
but that sounds like this
and it wasn't that a fix didn't get pushed
it wasn't fixed
until now

=== @arceusplayer11 (discord: Deedee) 08/31/2021 23:14

No, I mean you sent me code that fixed it
But I haven't pushed anything since I started sideview swimming

=== @EmilyV99 (discord: Emily) 08/31/2021 23:16

oh, I did?
well, merge conflict on your end probably then

=== @ Guinevere 09/01/2021 02:32

(replying to @ Guinevere "when fixed screen scrolling i…"): There's still this bug with the fixed smart scrolling, should I make a seperate thread for this or just keep it here?

=== @EmilyV99 (discord: Emily) 09/01/2021 02:37

separate thread

=== @ Guinevere 09/01/2021 02:38

Okie

=== @EmilyV99 (discord: Emily) 09/01/2021 03:22

(meta) thread name was changed: ✅🔒Scrolling Crash Bug?
## Generic disassembled item piece (#835)
@ Alucard648 opened this issue on 08/28/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/881136987275407360



=== @ Alucard648 08/28/2021 11:23

This should comply requests for various disassembled items, like Magic Container peces, Boss Key pieces (hello Twilight Princess) etc.

=== @EmilyV99 (discord: Emily) 08/28/2021 11:38

this.... would take quite a lot of work
boss key is an *entirely* different premise to a container
and uh
this would probably best be scripted

=== @ Alucard648 08/28/2021 15:45

Written in 1 hour:
```
//Generic Disassembled item piece. Link must collect enough items to assemble whole item. 2.53.x
//1. Set aside 1 screen in a DMap, like unused space in a dungeon.
//2. Set up as many consecutive strings to track item assembly progress, like 1/4, 2/4, 3/4 etc.
//3. Create item in Item editor, assign script into Pickup script slot.
// D0 - Item to assemble.
// D1 - Number of pieces to form whole item.
// D2 - First string of the sequence from step 2.
// D3 - Dmap from step 1, needed to track item assembly progress.
// D4 - Dmap Screen from step 1, needed to track item assembly progress.
// D5 - Dmap Screen D register from step 1, needed to track item assembly progress.

item script ItemPiece{
    void run (int Item, int Numpieces, int string, int DMapD, int ScreenD, int ScreenDReg){
        int D = Game->GetDMapScreenD(DMapD, ScreenD, ScreenDReg);
        if (string>0) Screen->Message(string+D);
        D++;
        if (D >= Numpieces){
            item coll = Screen->CreateItem(Item);
            coll->X = Link->X;
            coll->Y = Link->Y;
            D = 0;
        }
        Game->SetDMapScreenD(DMapD, ScreenD, ScreenDReg, D);
    }
}```
https://cdn.discordapp.com/attachments/881136987275407360/881202797155090492/bug3.qst

=== @ P-Tux7 08/28/2021 21:54

does this handle the subscreen?

=== @ Alucard648 08/29/2021 02:14

(replying to @ P-Tux7 "does this handle the subscree…"): Unfortunately, unless you script subscreen entirely, this not handle. And as for current version docs, subscreen scripts are not implemented.

=== @ P-Tux7 08/29/2021 02:20

yeah that's been an issue with like
2.50 magic container pieces
## scrolling combo or door (forced direction) (#836)
@arceusplayer11 (discord: Deedee) opened this issue on 08/28/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/881325057337610261



=== @arceusplayer11 (discord: Deedee) 08/28/2021 23:51

A warp combo that acts as a scrolling warp when you step on it, but with a defined direction. Specific use case would be doors that are away from the screen edges
Having worked with a script that does this (very jankily), I can say that this transforms how you handle dungeon design in more GB-oriented sets for the better

=== @arceusplayer11 (discord: Deedee) 08/28/2021 23:53

Of course, for it to be fully feature complete, it'd need to put you on a return combo on the other side

=== @EmilyV99 (discord: Emily) 08/28/2021 23:56

so, a fancy version of a scrolling warp

=== @arceusplayer11 (discord: Deedee) 08/28/2021 23:57

yup
Scrolling warp has a problem in that it doesn't force your direction
so you could walk into a left door facing up, and you'll scroll the screen in the up direction

=== @ P-Tux7 08/29/2021 00:29

(replying to @arceusplayer11 (discord: Deedee) "Of course, for it to be fully…"): yeah i was gonna ask where do you *appear* on the second screen
also can't you use this to make mario esque pipes

=== @arceusplayer11 (discord: Deedee) 08/29/2021 00:30

Absolutely yeah, though they couldn't turn like some pipes in SMW (at least, not without some clever hacking of features like conveyors and switchblocks)

=== @ P-Tux7 08/29/2021 00:38

that's mario 3, mario world is infamous for not having any sort of scrolling pipes at all
it's just either inert pipes or "fade out, go to another room" pipes
(replying to @arceusplayer11 (discord: Deedee) "Absolutely yeah, though they…"): ~~or the raft~~

=== @ Tsunami Tommy Reload the Shotty 08/29/2021 00:50

Maybe it could be two combos:

1)  Side Warp Trigger - With selectors for North/East/South/West, and Screen and Dmap coordinates, as well as a numerical identifier that would be paired with the combo below.

2)  Side Warp Arrival - Mostly just acts are a receiver for the above.  Its one property is the numerical identifier.

The numerical identifier acts as a warp coordinate receiver.  So a side warp trigger combo with ID 3 would send it to a Side Warp Arrival ID 3 on that screen.

Not sure how it would handle going between two such combos though in the case of a door that goes between two combos, like most traditional north/south doors.

=== @ Tsunami Tommy Reload the Shotty 08/29/2021 01:17

---
Or would it just make more sense to keep the X or Y positioning (and Z, probably.) and just go to the next available side-warp arrival combo in that direction you're already traveling in from the first screen.

=== @arceusplayer11 (discord: Deedee) 08/29/2021 01:54

(replying to @ Tsunami Tommy Reload the Shotty "---
Or would it just make mor…"): this would make far more sense

=== @ P-Tux7 08/29/2021 02:06

ehh
i can see the use cases for manual arrival combos

=== @ Alucard648 08/29/2021 02:16

Simething like this?|https://www.youtube.com/watch?v=ZSAEYBmX58Y

=== @ Tsunami Tommy Reload the Shotty 08/29/2021 02:19

Show-off. 😛   But nah, it might be a combo that triggers the screen-scroll effect earlier, closer to the middle of the screen than being right on the very edge, and can probably even dump you somewhere not on the edge of the next screen too.

=== @arceusplayer11 (discord: Deedee) 08/29/2021 02:20

(replying to @ Tsunami Tommy Reload the Shotty "Show-off. 😛   But nah, it mig…"): basically this

=== @ P-Tux7 08/29/2021 02:21

yeah like again
mario/turtle rock pipes

=== @arceusplayer11 (discord: Deedee) 08/29/2021 02:21

Yeah
Though rafting would make more sense for same-screen pipes

=== @ Alucard648 08/29/2021 02:45

(replying to @ Tsunami Tommy Reload the Shotty "Show-off. 😛   But nah, it mig…"): I found this script when digging through source code of Link Stuck in Castlevania. Setup instructions are inside script file.
https://cdn.discordapp.com/attachments/881325057337610261/881368978759504002/CVDoorTransition.z
## liquid features (#837)
@ P-Tux7 opened this issue on 08/29/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/881366996103606313



=== @ P-Tux7 08/29/2021 02:37

1. ignore health modifier if flipper level is (x) or above
this is basically where if you give the player level 1 flippers, they can still swim but the counter drain is in play. getting the right level of flippers removes it. also, maybe a setting of 0 (or -1?) means that no flippers will stop the effect
2. (rule) disable liquid drain while holding up an item
3. i'm unsure about how to implement this elegantly, but perhaps a drain rate for the liquid that can be divided, instead of it being a binary on or off?
what can liquids even drain right now? is it only health or is it all the counters?

=== @EmilyV99 (discord: Emily) 08/29/2021 02:38

1. you can do that already
but you can use any itemclass, not just flippers

=== @ P-Tux7 08/29/2021 02:39

oh goddamnit
sorry this hasn't been a good week

=== @EmilyV99 (discord: Emily) 08/29/2021 02:40

2. probably should fix that
3. that'd be rough
it's only health

=== @ P-Tux7 08/29/2021 02:41

oh yeah hmm
i was thinking that using magic (stamina) or a script counter could be used to have an oxygen meter
though, considering it only needs to detect link, a combo script might still be usable for that

=== @arceusplayer11 (discord: Deedee) 08/29/2021 03:47

The big barrier to adding more stuff to this was a lack of combo arguments, and that has since been fixed
This might happen after the dev break
(division and etc)
## ✅🔒Tiny Quest Gold  Upgrading - Crash in Heart Container Room (#838)
@ NightmareJames opened this issue on 08/29/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/881623496113913857



=== @ NightmareJames 08/29/2021 19:37

@EmilyV99 (discord: EmilyV) Was testing out Tiny Quest:  Gold on stream in some spare time, and I upgraded Tiny Quest Gold from A 39 to A 85 to A 92, then ran it in the latest nightly.  What I ended up with is a crash in the Heart Container Room.  Video and quest file incoming when I package them
https://youtu.be/RERTrX1MzNc  Video

=== @ NightmareJames 08/29/2021 19:38

Shadowblazer Tiny Quest Gold file I was updating from A39
https://cdn.discordapp.com/attachments/881623496113913857/881623960029122640/Shadowblazer-Tiny-Gold.zip
If you need any more information @ me

=== @EmilyV99 (discord: Emily) 08/29/2021 23:44

#834 feel like this is just the same issue

=== @ NightmareJames 08/30/2021 00:18

@arceusplayer11 (discord: Deedee) ?  You'd know better

=== @ NightmareJames 08/30/2021 00:19

But if this is the case, the original Tiny Quest probably has to be tested in 2.53 as well

=== @ NightmareJames 08/31/2021 09:55

Fixed
@<role: Developer>

=== @EmilyV99 (discord: Emily) 09/01/2021 03:22

(meta) thread name was changed: ✅🔒Tiny Quest Gold  Upgrading - Crash in Heart Container Room
## More then 1 Item or Chest per Screen (#839)
@ Dr00g opened this issue on 08/29/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/881647317348921366



=== @ Dr00g 08/29/2021 21:11

What is says on the tin Id love to be able to make Alttp stlyed Chest rooms

=== @EmilyV99 (discord: Emily) 08/29/2021 23:43

@arceusplayer11 (discord: Deedee)

=== @arceusplayer11 (discord: Deedee) 08/29/2021 23:47

Planned, it's on my todo list
## 💊🔓Bomb Weapon Tab Shenanigans (#840)
@ Guinevere opened this issue on 08/30/2021

Status: needs-testing

Labels: ['bug', 'needs-testing']

Source: https://discord.com/channels/876899628556091432/881803390584246272



=== @ Guinevere 08/30/2021 07:31

Changing the bomb's weapon type affects both the bomb and it's blast

=== @ P-Tux7 08/30/2021 07:44

i don't see this as an issue

=== @ Guinevere 08/30/2021 07:44

<:nekoshrug:694456306060492800>
Emily told me to

=== @ P-Tux7 08/30/2021 07:45

the problem that i see is the lit bomb being able to trigger defenses but that's not what you wrote

=== @ Guinevere 08/30/2021 07:46

i mean i'm sure it gets the point across, i don't think the bomb itself should have a hitbox once a weapon type is added on to the item
seems a lil silly
<:teehee:620404816769843200>

=== @EmilyV99 (discord: Emily) 08/30/2021 07:47

the weapon type effect should not apply to the bomb
it should still behave as a bomb

=== @ Guinevere 08/30/2021 07:48

and if the lit bomb comes into contact with an enemy, it kills the item and hurts the enemy like a normal lweapon

=== @arceusplayer11 (discord: Deedee) 02/13/2022 17:24

(meta) thread name was changed: 💊🔓Bomb Weapon Tab Shenanigans
Fixed

=== @EmilyV99 (discord: Emily) 02/13/2022 17:25

Ooh, nice

=== @arceusplayer11 (discord: Deedee) 02/13/2022 17:26

also did a similar thing with defenses too
(the "use defense" thing)

=== @ P-Tux7 02/13/2022 17:33

super bombs too?

=== @arceusplayer11 (discord: Deedee) 02/13/2022 17:36

yup
though I initially was confused because I thought wBomb was LW_BOMB, but no, it's LW_BOMBBLAST

=== @arceusplayer11 (discord: Deedee) 02/16/2022 04:05

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
## ❌🔒[2.53] Parser will truncate ints and floats early (#841)
@ mitchfork opened this issue on 08/30/2021

Status: wont-fix

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/881906459691077682



=== @ mitchfork 08/30/2021 14:21

`int` has a legal range of "-214748.3648, 214748.3647".  However, the parser will enforce a range of "-214747.9999, 214747.9999" and truncate legal values
this is... an incredibly small bug

=== @EmilyV99 (discord: Emily) 08/30/2021 20:42

not a bug
intended behavior
and changed in *2.55*, with compiler options
https://cdn.discordapp.com/attachments/878114935396257852/882002144692166677/unknown.png
2.53's legal range is `-214747.9999` to `214747.9999`
(meta) thread name was changed: ❌🔒[2.53] Parser will truncate ints and floats early
## ZQuest 2.55 tanking in FPS even more than 2.53 did. (#842)
@ Haylee opened this issue on 08/31/2021

Status: unknown

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/882190179262144542



=== @ Haylee 08/31/2021 09:08

So when I used 2.53, there would be this issue where the program would run at 30 FPS consistently, but when I would run a background process (A Discord VC, OBS, Steam, etc.) it would actually go _up_ to 60 for some reason. It's even worse here though, where the FPS is now locked at roughly 20 FPS when I'm not in other calls, but will not only move up to 45-50 FPS with a background process. While I have no clue what's causing the program to run better, it doesn't change that for some reason, there's a massive dip in FPS for 2.55 over 2.53.

![image](https://cdn.discordapp.com/attachments/882190179262144542/882190196999876618/unknown.png)

=== @EmilyV99 (discord: Emily) 08/31/2021 09:09

are you using the built-in fps counter?

=== @ Haylee 08/31/2021 09:09


![image](https://cdn.discordapp.com/attachments/882190179262144542/882190339165790239/unknown.png)
ye

=== @EmilyV99 (discord: Emily) 08/31/2021 09:09

does it flicker like the one in ZC does?
or is it a solid draw?

=== @ Haylee 08/31/2021 09:09

solid draw

=== @EmilyV99 (discord: Emily) 08/31/2021 09:09

that being on may well be tanking your fps

=== @ Haylee 08/31/2021 09:09

wut
Any way to change that?

=== @EmilyV99 (discord: Emily) 08/31/2021 09:10

that's why the zc one flickers, to fix that problem
I'd recommend turning off the fps counter and seeing if it feels any better?

=== @ Haylee 08/31/2021 09:10

Nah, that's defo still 21 rn
yeesh

=== @ Haylee 08/31/2021 09:12

It's an issue I had for a while that I figured was just an issue with me using Windows 10 (I recall some dev discussion about it a long time ago), but since it's tanking even more it has me confused.

=== @EmilyV99 (discord: Emily) 08/31/2021 09:12

does `frame_rest_suggest` do anything in zquest.cfg?
trying 0/1/2?

=== @ Haylee 08/31/2021 09:13

lemme check

=== @ Haylee 08/31/2021 09:15

nothin

=== @ Guinevere 08/31/2021 09:21

oh yeah
i also noticed this

=== @EmilyV99 (discord: Emily) 08/31/2021 09:23

and frankly, I'd expect 2.55 to be worse than 2.53, as more is going on

=== @ Haylee 08/31/2021 09:23

wait hold on

=== @EmilyV99 (discord: Emily) 08/31/2021 09:23

once you're dipping below 60, it's not a stretch for it to dip further

=== @ Haylee 08/31/2021 09:23

something weird

=== @ Guinevere 08/31/2021 09:24

it's been a thing for a *while*
tbh i didn't report it bcuz a couple years ago i had a crappy laptop where everything ran slow on it. guess i was still used to the slow framerate. lol

=== @ Haylee 08/31/2021 09:25

Weeeird, so I moved up in versions (since hehe hard to keep up), but uh
![image](https://cdn.discordapp.com/attachments/882190179262144542/882194260001185812/unknown.png)
We're not at 21 anymore
so
intriguing

=== @EmilyV99 (discord: Emily) 08/31/2021 09:25

????

=== @ Haylee 08/31/2021 09:25

it's still not _60_
but
weird

=== @EmilyV99 (discord: Emily) 08/31/2021 09:25

you updated 2.55 build?

=== @ Haylee 08/31/2021 09:25

I was like
a few days outdated

=== @EmilyV99 (discord: Emily) 08/31/2021 09:25

that should not have changed a damn thing

=== @ Haylee 08/31/2021 09:25

No clue

=== @EmilyV99 (discord: Emily) 08/31/2021 09:26

nothing changed in at least a month should have much effect on fps

=== @ Haylee 08/31/2021 09:26

a few days meaning a couple weeks

=== @ Guinevere 08/31/2021 09:26

mine always sits around 30fps

=== @ Haylee 08/31/2021 09:26

in this case
yeah idk what's happening

=== @EmilyV99 (discord: Emily) 08/31/2021 09:26

could be random video driver garbage

=== @ Haylee 08/31/2021 09:26

maybe

=== @EmilyV99 (discord: Emily) 08/31/2021 09:26

which, would put it out of our possible control

=== @ Haylee 08/31/2021 09:27

also does the frameskip function work or what

=== @ Guinevere 08/31/2021 09:27

a lil weird that zc player can run buttery smoof but zquest can't keep up the pace, lol

=== @EmilyV99 (discord: Emily) 08/31/2021 09:28

I mean
check the .exe sizes
ZQ is like twice as big an exe

=== @ Guinevere 08/31/2021 09:28

true

=== @ Haylee 08/31/2021 09:28

fair

=== @ Haylee 08/31/2021 09:30

~~unfortunately it's now consistently around 51 instead of increasing when I have background processes but hey, 51 means I can _somewhat_ do my funky frame data stuff I wanna do in ZC better~~
I'll let ya know if more weirdness happens

=== @EmilyV99 (discord: Emily) 08/31/2021 09:30

Apparently mine sits around 30

=== @ Guinevere 08/31/2021 09:31

ayy
30 buddies

=== @ Haylee 08/31/2021 12:13

welp the FPS thing was a fluke
good to know
we're back to bad fps

=== @ 4matsy 09/01/2021 04:55

Ayy, more 30 buddies. :p
Yeah I'm still on alpha 92 since Mom and I's internet was out for a few weeks - let me go and download the latest nightly alpha and I'll see how that one compares. :o
## Secret--Undercombo flag (#843)
@ Mani Kanina opened this issue on 08/31/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/882312888025485363



=== @ Mani Kanina 08/31/2021 17:16

I don't know if this is a feature already since I haven't kept up with development, but I got the idea so I figured I should post it:

A secret flag similar to flag 16-31, but instead of changing the combo to a defined secret combo, it instead takes the screens undercombo.

=== @EmilyV99 (discord: Emily) 09/04/2021 04:27

`Secret->Undercombo`, interesting idea. I added `Secret->Next` recently, so it could be implemented just as that is.

=== @EmilyV99 (discord: Emily) 09/04/2021 08:57

(meta) thread name was changed: Secret--Undercombo flag
## ✅🔒Smart Screen Scrolling Bug (#844)
@ Guinevere opened this issue on 09/01/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/882455341898543164



=== @ Guinevere 09/01/2021 02:42

when smart screen scrolling and fixed smart scrolling are enabled;
if there are solid combos at one edge of the screen, it blocks link from scrolling that way where the solid combos would be like if they were on the next screen in the same position.

![image](https://cdn.discordapp.com/attachments/882455341898543164/882455493526827028/2021-08-28-09-56-44.mp4)

=== @ P-Tux7 09/01/2021 02:44

are we getting fixed fixed smart scrolling now

=== @ Guinevere 09/01/2021 02:44

lol
could be
<:teehee:620404816769843200>

=== @EmilyV99 (discord: Emily) 09/01/2021 03:22

@arceusplayer11 (discord: Deedee)

=== @arceusplayer11 (discord: Deedee) 10/09/2021 16:34

(meta) thread name was changed: ✅🔒Smart Screen Scrolling Bug
Fixed I think
I think this is the same issue as FireSeraphim's bug and I just fixed that one
(and I didn't notice this behavior once I fixed that)
## ❌🔒Ability to change map numbers or Ability to Sort Dmaps (#845)
@ SkyLizardGirl opened this issue on 09/02/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/882804630063566960



=== @ SkyLizardGirl 09/02/2021 01:50

My first idea is some kind of ability to rearrange Dmap numbers, if you create your Overworld on map 4 for example, this ability would let you toggle Map 4 back to being map 1 again, without deleting and re-pasting maps in order to achieve this. All exits and stairs created won't becomes mixed up or erased while doing this.  Notice:  >   If this is not possible, i would like the ability to rearrange Dmaps without Exits and Stairs getting mixed up or messed up by trying to sort around my Dmaps by copying and re-pasting them. The idea would be a toggle option so transport destinations don't get ruined.

=== @ SkyLizardGirl 09/02/2021 01:52

This is one thing that has always bugged me.

=== @EmilyV99 (discord: Emily) 09/02/2021 01:59

this is really painful
and could be avoided by careful planning

=== @ SkyLizardGirl 09/04/2021 06:22

Ok then, just a sort button for Dmaps then maybe?
But the data is unchanged, it just appears different in the editor

=== @EmilyV99 (discord: Emily) 09/04/2021 06:49

gonna go with no
(meta) thread name was changed: ❌🔒Ability to change map numbers or Ability to Sort Dmaps
## ✅🔒Ability to sort Message strings by number using a toggle (#846)
@ SkyLizardGirl opened this issue on 09/02/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/882805826035785768



=== @ SkyLizardGirl 09/02/2021 01:55

The ability to sort string messages by order of number from 1 to etc. Using a toggle option, you can sort your strings better without messages getting messed up in your game from trying to arrange them.

=== @EmilyV99 (discord: Emily) 09/04/2021 04:27

A simple "sort" button should be simple enough to add

=== @ SkyLizardGirl 09/04/2021 06:21

\0~^ Awesome

=== @EmilyV99 (discord: Emily) 02/02/2022 05:34

(meta) thread name was changed: ✅🔒Ability to sort Message strings by number using a toggle
https://cdn.discordapp.com/attachments/494693243750187008/938305649413062656/unknown.png
https://cdn.discordapp.com/attachments/494693243750187008/938305686452965386/unknown.png
## 💊🔓Panoply of Calatia in 2.55 (#847)
@ Guinevere opened this issue on 09/02/2021

Status: needs-testing

Labels: ['bug', 'needs-testing']

Source: https://discord.com/channels/876899628556091432/882862231509954580



=== @ Guinevere 09/02/2021 05:39

I've only been playing it for a couple minutes and ran into a couple things, then i added items with cheats to see what else was up...
-shield doesn't push urchin enemies
✅ -on certain screens, certian strings play when you pick up items, and since some strings are tied to items(specifically trading sequence items), the player also gets the item (Fixed)
-some sprite errors (sword beam break effect, ball and chain's chain)
-the candelabra only shoots two flames instead of three

=== @ Guinevere 09/02/2021 05:41


https://cdn.discordapp.com/attachments/882862231509954580/882862759082098748/Link_and_Zelda_-_Panoply_of_Calatia.qst

=== @ Guinevere 09/02/2021 05:42

these are all the ones i found so far.

=== @ P-Tux7 09/02/2021 06:36

```-on certain screens, certian strings play when you pick up items, and since some strings are tied to items(specifically trading sequence items), the player also gets the item```
wait slg had that issue in mystical harps (which was also a 2.50.2 quest converted to 2.55)

=== @ Guinevere 09/02/2021 06:38

i see
good to know

=== @ Guinevere 09/03/2021 00:09

-bubbles after they finish their spawn animation stop moving/bouncing

=== @ P-Tux7 09/03/2021 00:13

are these diagonal bubbles?

=== @ Guinevere 09/03/2021 00:27

ye

=== @ Guinevere 09/03/2021 00:28

-guma's sometimes shoot straight projectiles with no set sprite instead of their "bolas"

=== @ Guinevere 09/07/2021 05:00

-coppies copy the direction the player is facing but not the movements

=== @EmilyV99 (discord: Emily) 10/11/2021 20:17

(replying to @ Guinevere "I've only been playing it for…"): hover boots in this quest?
Looking through the quest file and script file, I don't see any hover boots item given to the player at any point ever

=== @ Guinevere 10/11/2021 20:18

yeah i forgot to remove them

=== @EmilyV99 (discord: Emily) 10/11/2021 20:19

> -if you hold the jump button on the second jump with the roc's cape, and have the hover boots, you fly up higher than you're supposed to

=== @ Guinevere 10/11/2021 20:20

yeah that's my bad

=== @ Guinevere 10/11/2021 20:21

i cheated in all the items (i thought) were in but i forgot the boots weren't an item in the quest.

=== @EmilyV99 (discord: Emily) 10/11/2021 20:24

`-the candelabra only shoots two flames instead of three`
Are you sure it's not spawning 3, but 2 of them are overlapping?
(If you have `Log Game Events to allegro.log` enabled, the console will show every time a script creates a weapon)
`-on certain screens, certian strings play when you pick up items, and since some strings are tied to items(specifically trading sequence items), the player also gets the item` This should have been fixed a while ago, was reported in other quests

=== @EmilyV99 (discord: Emily) 10/11/2021 20:30

What's wrong with sword beams? I don't see any issue

=== @EmilyV99 (discord: Emily) 10/11/2021 20:35

the urchins.... definitely are broken, and I don't see why at all
ffs

=== @ Guinevere 10/11/2021 20:42

I know that the item pickup bug was fixed
the sword beams screw up only when link is auto firing
and it could be that the candelabra is shooting three shots but two shots stop right away and the third trails off normally

=== @ZoriaRPG (discord: Timelord) 11/03/2021 15:37

(replying to @ Guinevere "-coppies copy the direction t…"): new player movement or zfix related perhaps?

=== @ZoriaRPG (discord: Timelord) 11/03/2021 15:38

(replying to @ P-Tux7 "are these diagonal bubbles?"): this could be similar
worth testing in builds prior ro adding these feats

=== @ZoriaRPG (discord: Timelord) 11/03/2021 15:40

http://timelord.insomnia247.nl/zc-dev/2.55/
i tried to mae change backtracking easy by archiving every build

=== @EmilyV99 (discord: Emily) 11/03/2021 15:41

(replying to @ZoriaRPG (discord: Timelord) "new player movement or zfix r…"): definitely not new movement, as that would require the quest be edited to enable a previously nonexisting qr

=== @ZoriaRPG (discord: Timelord) 11/03/2021 15:44

use cheats, try it in old builds th work forward
coud be soe wrie zfix thing
coud be anything
itested it in a build 2 years ago
never noticed those specific issues
also
please list open isues and not ied issues
would help
if you get a st saved to where it is eas to test thes bugs sain a20 then yo can repeately test each build thereater an chec changes

=== @ZoriaRPG (discord: Timelord) 11/03/2021 15:49

i advise jups o 5 builds to expedite narrowing the build range where te bug occurs
My apologises in advance i I did something awful

=== @ Mitsukara 11/05/2021 21:16

(replying to @EmilyV99 (discord: Emily) "Looking through the quest fil…"): They're not hover boots, although they are called such in-game.  They're a custom scripted item (I _think_ in one of the Custom Item Classes?) that prevents the player from falling into hole combos (and gives them protection from stepping on spikes with a regular "boots" item).

=== @ Mitsukara 11/05/2021 21:18

my apologies for not actually participating in 2.55 testing myself, rendering LaZPoC halfway into the realm of abandonware (neglectware?)
but if anyone has further questions on this subject I'd be happy to at least attempt to help answer
at some future time when I have more of a windows 10 setup (or if a new 2.55-or-above Linux version comes out) I'll try to actually test the quest myself

=== @EmilyV99 (discord: Emily) 11/05/2021 21:23

@ Saffith can probably compile a linux build for you to test with, though it won't have any sound (that's currently the main linux issue)

=== @ Mitsukara 11/05/2021 21:27

oh? Well, no pressure if it'd be difficult, but that could be neat if it's easy to do

=== @EmilyV99 (discord: Emily) 11/05/2021 21:33

as far as I know compiling it (without sound) should be as easy as compiling a build for windows... just, saff is the only one with the linux build setup, considering you need a linux machine
well, or a VM, but we don't have that set up

=== @ Mitsukara 11/05/2021 21:35

hmm, I wonder if you can compile from within a flash drive boot of Linux, without needing to make a permanent installation

=== @ Mitsukara 11/05/2021 21:37

(the way Mint and most other versions of Linux work, you just format a USB flash drive to act as a boot device, and you can run Linux from that even without a permanent installation to a hard drive. I opted to install on my hard drive as well, but you don't have to do that to run Linux)
(it was pretty fast and simple)

=== @EmilyV99 (discord: Emily) 11/05/2021 21:41

I mean, I don't see why not
the main issue just being "bleh, needing to set things up? Lazy..."

=== @arceusplayer11 (discord: Deedee) 11/05/2021 21:52

The issue for me and getting linux is that i only have 5gb of space left on my main drive and im too lazy to vlean some of it out

=== @ Saffith 11/06/2021 03:33

Yeah, I can get something together. There are a couple of crashes I've been putting off dealing with; I should really do that first.
Sorry, been pretty lazy lately.

=== @EmilyV99 (discord: Emily) 11/06/2021 04:03

No problem <a:hugheart:884673091878391828>

=== @ Mitsukara 11/06/2021 04:10

(replying to @arceusplayer11 (discord: Deedee) "The issue for me and getting…"): that's part of the beauty of having a boot stick. No hard drive space needed, just a USB flash drive
also that's totally fine, I appreciate that you're working on stuff at all

=== @arceusplayer11 (discord: Deedee) 11/06/2021 11:32

(replying to @ Saffith "Sorry, been pretty lazy latel…"): Youve been a godsend recently, theres no pressure!

=== @arceusplayer11 (discord: Deedee) 01/29/2022 21:41

```-shield doesn't push urchin enemies``` Fixed

=== @ P-Tux7 01/29/2022 22:04

i dunno if you wanna detail it in the thread but i'd be interested to hear what the problem was in DM

=== @ P-Tux7 01/29/2022 22:07

Also, another quest worth looking into would be her 6th quest, since it uses much of the same ZScript functions. If it has bugs, fixing one there might fix it in Panoply. It can definitely clear your mind and make you realize a solution if you have two projects you can go back and forth between instead of focusing only on Panoply.

=== @arceusplayer11 (discord: Deedee) 01/29/2022 23:33

```-some sprite errors (sword beam break effect, ball and chain's chain)``` Fixed, Zoria was a dumbass and hardcoded default weapon sprites when the weapon creation code handled them based on item ownership and etc

=== @arceusplayer11 (discord: Deedee) 01/30/2022 15:08

``//step = (type<2)?.5:0;`` Okay so see this
```-the candelabra only shoots two flames instead of three```
The thing that sets the default step for fire weapons is commented out
So script created fire weapons got changed to default to 0 step instead of 0.5 step, without regard for what this would break
thanks Zoria

=== @arceusplayer11 (discord: Deedee) 01/30/2022 15:35

I'm unsure if this is  abug or intended; autofire damage seems *really* low
lemme boot it up in 2,53

=== @arceusplayer11 (discord: Deedee) 01/30/2022 15:42

Okay, no, it seems intentional
I mean, they are level 1 stats

=== @arceusplayer11 (discord: Deedee) 01/30/2022 22:11

It's really annoying trying to debug issues introduced in early 2.53

=== @arceusplayer11 (discord: Deedee) 02/01/2022 19:26

```-guma's sometimes shoot straight projectiles with no set sprite instead of their "bolas"```
Fixed this; o_tile was for some reason changed to not be correctly initialized with script weapons, which would cause o_tile to either be the value of a previous weapon or random values, which tricked scripts into thinking that the weapon had been dealt with and made into a bola when in fact it hadn't

=== @arceusplayer11 (discord: Deedee) 02/01/2022 19:28

```-shield doesn't push urchin enemies```
```-bubbles after they finish their spawn animation stop moving/bouncing```
```-coppies copy the direction the player is facing but not the movements```
all of these are fixed, as they were the same underlying issue
and both```-the candelabra only shoots two flames instead of three```and ```-some sprite errors (sword beam break effect, ball and chain's chain)``` were fixed, as detailed above
granted, I have not yet checked the ball and chain

=== @arceusplayer11 (discord: Deedee) 02/01/2022 19:31

I'm going through the entire game and fixing stuff as I go

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:05

god, it's a pain to search through quest strings
I wish there were a way to force sort them by their number

=== @EmilyV99 (discord: Emily) 02/01/2022 20:11

...give me like 5 minutes.
and I can give you that in 2.55

=== @EmilyV99 (discord: Emily) 02/01/2022 20:42

@arceusplayer11 (discord: Deedee) pushed
that took a little more than 5 minutes, but, it's pretty cleanly implemented

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:42

ooooh
thank you

=== @EmilyV99 (discord: Emily) 02/01/2022 20:42


![image](https://cdn.discordapp.com/attachments/882862231509954580/938172497373851708/unknown.png)
`Sort` will sort everything numerically
and when you sort, it takes a copy of the order it was in previously; and makes `unsort` pressable. `Unsort` will restore the previous order.

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:43

It's purely visual, right? It won't fuck with the actual order?

=== @EmilyV99 (discord: Emily) 02/01/2022 20:43

It does fuck with the actual order
there isn't a way to do it visuallyu
without completely rewriting how it works
but, `unsort` will put it back in the order it was in before you `sort`ed

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:43

will it still save the order even if you go into a message string and then go out?

=== @EmilyV99 (discord: Emily) 02/01/2022 20:43

yes, but not if you close the dialog

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:44

alright

=== @EmilyV99 (discord: Emily) 02/01/2022 20:44

...actually could probably make it stay even through that easily enough
hmm
one moment
oh wait
no
because that would persist even if you changed quests
bleh
yeah, so just be careful not to close the dialog if you intend to unsort

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:46

So, uh
I'm running into a very weird pickup issue
```int32_t shop_pstr = 0;
            switch(tmpscr[tmp].room)
            {
                case rSHOP:
                    shop_pstr = QMisc.shop[tmpscr[tmp].catchall].str[PriceIndex];
                    break;
                case rBOTTLESHOP:
                    shop_pstr = QMisc.bottle_shop_types[tmpscr[tmp].catchall].str[PriceIndex];
                    break;
            }
            if ( (pstr > 0 && pstr < msg_count) || (shop_pstr > 0 && shop_pstr < msg_count) )
            {
                if ( (pstr > 0 && pstr < msg_count) && ( ( ( pstr_flags&itemdataPSTRING_ALWAYS || pstr_flags&itemdataPSTRING_NOMARK || pstr_flags&itemdataPSTRING_IP_HOLDUP || (!(FFCore.GetItemMessagePlayed(id2)))  ) ) ) )
                {
                    if ( (!(pstr_flags&itemdataPSTRING_NOMARK)) ) FFCore.SetItemMessagePlayed(id2);
                }
                else pstr = 0;
                if(shop_pstr)
                {
                    donewmsg(shop_pstr);
                    enqueued_str = pstr;
                }
                else if(pstr)
                {
                    donewmsg(pstr);
                }
            }``` I'm picking up an item on a screen with a screen 80 shop (but not in the shop itself)
And it's displaying string 200
this is the shopdata of the shop in question
![image](https://cdn.discordapp.com/attachments/882862231509954580/938173859931254794/unknown.png)

=== @EmilyV99 (discord: Emily) 02/01/2022 20:48

oh uhh
I see what's wrong
`PriceIndex` is `-1`
so it's reading `[-1]`, out of bounds
probably grabbing the price of the 3rd item

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:48

ahhhh

=== @EmilyV99 (discord: Emily) 02/01/2022 20:48

the entire `switch(tmpscr[tmp].room)` needs to be inside an `if(PriceIndex > -1)`

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:49

```if (PriceIndex >= 0 && PriceIndex < 3) ```?

=== @EmilyV99 (discord: Emily) 02/01/2022 20:49

`>-1` should be sufficient
it will only ever be -1, 0, 1, 2
#1163
that'll be fixed by this

=== @ P-Tux7 02/01/2022 20:53

oh is that what slg was reporting

=== @arceusplayer11 (discord: Deedee) 02/01/2022 20:57

Well, she did respond with "random items" instead of "shop items"
but I need a clarification

=== @ Mitsukara 02/04/2022 00:50

so hey, sorry I haven't been keeping an eye on all this. Feel free to ping me if there's questions in here that I miss

=== @ Mitsukara 02/04/2022 01:00

(replying to @arceusplayer11 (discord: Deedee) "```-some sprite errors (sword…"): ...this reminds me of a more general weirdness I noticed a time or two, in 2.50.2, which I never checked if it's still in newer versions or how best to prevent it, but, sometimes when you created a LW_SCRIPT(number) weapon, it would, for one frame, have weapon sprite 1 (wooden sword) pointing north, before the graphic was set? Not sure if that's still a thing, or something I was doing wrong, it's been a long time since I poked at any of this
to the point where I'm not confident trying to post a bug report, but it might be an issue that existed, or exists

=== @ Mitsukara 02/04/2022 01:02

(replying to @arceusplayer11 (discord: Deedee) "I'm unsure if this is  abug o…"): ...I might've been incompetent somewhere, I don't think it was supposed to be level 1 damage at all times? I mean... _maybe_ that made sense but it sounds kinda weird. I would think if I was nerfing it I would've gone for half-damage, or like, one level behind or something, like literally like, a flat level 1 damage no matter how much you levelled up.
Then again I defaulted to liking things tanky so I might not've even noticed and thought about it

=== @arceusplayer11 (discord: Deedee) 02/04/2022 01:03

(replying to @ Mitsukara "...I might've been incompeten…"): I was at level 1 at the time; it just seemed like Link was doing half the damage Zelda was doing as a partner

=== @ Mitsukara 02/04/2022 01:03

OH
okay, I think Link might have weaker swordbeams that match Zelda's arrows when he's a partner, yeah
I think that might've been part of the attempt to make Link suck less since there was a general consensus it was always better to play as Zelda
so that the actual sword does more damage when you're using it directly

=== @arceusplayer11 (discord: Deedee) 02/04/2022 01:04

(replying to @ Mitsukara "I think that might've been pa…"): wow, you should have gone the opposite approach
should have given them a gust jar so they could suck *more*

=== @ Mitsukara 02/04/2022 01:05

Make Link completely useless?
![image](https://cdn.discordapp.com/attachments/882862231509954580/938963448686071868/iu.png)

=== @arceusplayer11 (discord: Deedee) 02/04/2022 01:05

😎

=== @ Mitsukara 02/04/2022 01:05

I do wish I'd had a gust jar item kinda thing actually
Maybe in a future project XD

=== @ Mitsukara 02/04/2022 01:07

(replying to @arceusplayer11 (discord: Deedee) "god, it's a pain to search th…"): Sorry about this. I share your pain, and regretted a thousand times that I had changed the order at all
Another really, REALLY good sounding quality of life feature to be able to resort them now, thanks for that!

=== @ Mitsukara 02/04/2022 01:09

also, thank you both more generally for working on all this stuff

=== @arceusplayer11 (discord: Deedee) 02/04/2022 01:58

no problemo
I've gotten a lot of dungeons down with very little issue; only just now ran into an issue with wand fire because I flubbed up another fix

=== @arceusplayer11 (discord: Deedee) 02/11/2022 09:13

So as far as I could tell, Panoply now plays fine in 2.55
(meta) thread name was changed: 💊🔓Panoply of Calatia in 2.55

=== @ P-Tux7 02/11/2022 21:57

Can you test her 6th quest?

=== @EmilyV99 (discord: Emily) 02/13/2022 05:13

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
## Allow moving item spawn position without selecting an item (#848)
@ Moosh opened this issue on 09/02/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/882932541429014538



=== @ Moosh 09/02/2021 10:18

This is the nittiest of nitpicks out there so keep in mind that I realize this. When you click the item square button in ZQuest it auto opens a prompt to select an item. Currently if you select (None) it treats this the same as having hit cancel. And in most cases this makes sense, if you're placing an item you probably want to place an actual item. But there is one exception to this: item cellar screen 80. In that one case, the item spawn position is used for an item set on another screen and no item will normally appear there. Whenever I set up a new screen 80, I'll just place a random item and then go back and set the screen item to (None), but since the cancel button is already a thing it'd be nice to cut out that extra step. Thoughts?

=== @ Moosh 09/02/2021 10:20

I also realize that there's no harm in leaving an item on screen 80. It'll get properly replaced. But it looks better in the editor without. Also the contents of screen 80 can still show up in quest reports, which may or may not be a bug itself

=== @ P-Tux7 09/02/2021 15:37

i'd call items an issue for quest reports, but the screen (or staircase and cave screens) can't be excluded entirely due to it having valid user-placed combos and enemies

=== @EmilyV99 (discord: Emily) 09/04/2021 04:27

this makes sense, though I could see it being annoying for some; can probably make it a ZQ config

=== @ Moosh 09/04/2021 07:07

Sounds good. Either that or a screen 80 specific exception
## Whimsical-Attack Ring Customization (#849)
@ Guinevere opened this issue on 09/03/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/883194006450884669



=== @ Guinevere 09/03/2021 03:37

I'd like them to have seperate flags for letting them only/either affect the sword, hammer, or wand.

=== @ Guinevere 09/03/2021 04:49

(Tbh I want a flag where it only affects the sword but i felt that having one for all 3 would be courteous to others who'd like to choose exactly what it affects.)

=== @EmilyV99 (discord: Emily) 09/04/2021 04:26

this makes sense, will just take a bit of fiddling to make sure the flags are checked by default in qst.cpp

=== @ Guinevere 09/04/2021 04:30

having rings that affect the power of any lweapon and you could mix and match different rings and their flags for easier power upgrades/ring systems in quests instead of wasting tons of item space on a million upgrades to the items would also be neat, but i think that'll be a lil too much
so keeping it simple to just these are a good start.
## ✅🔒Message Strings Displaying Improperly - Alpha 95 Nightly 3 (#850)
@ NightmareJames opened this issue on 09/03/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/883279397518450728



=== @ NightmareJames 09/03/2021 09:17

Message Strings Displaying Improperly - Alpha 95 Nightly 3
https://youtu.be/NdO4NuTDJ-s
Quest that triggered it
https://cdn.discordapp.com/attachments/883279397518450728/883279532088524820/zeldanesremastered_V2_0._PublicGamma3.qst

=== @EmilyV99 (discord: Emily) 09/03/2021 14:02

This seems like #798 and #847

=== @ P-Tux7 09/04/2021 02:54

does this quest have any scripts?

=== @ bigjoe 09/04/2021 02:56

whatever is going on, the fact that its occuring across multiple quests elevates the need to get it looked at

=== @EmilyV99 (discord: Emily) 09/04/2021 02:57

aye

=== @ Saffith 09/04/2021 04:14

I think I see the problem. link.cpp, line 23975:
int shop_pstr = ( tmpscr[tmp].room == rSHOP && QMisc.shop[tmpscr[tmp].catchall].str[PriceIndex] > 0 ) ? QMisc.shop[tmpscr[tmp].catchall].str[PriceIndex] : 0;
PriceIndex is -1.

=== @ Saffith 09/04/2021 04:16

And str[-1] is 10, the string it's showing.

=== @EmilyV99 (discord: Emily) 09/04/2021 04:16

but the room isn't a shop
so that should short-circuit with a false boolean condition
...oh
........oh
......................oh
but
it needs
oh fuck
I would have taken so long to find that
needs to check `&& PriceIndex > -1`, I suppose

=== @EmilyV99 (discord: Emily) 09/04/2021 04:24

(you fixing and PR'ing, or shall I fix?)
@ Saffith

=== @ Saffith 09/04/2021 04:24

Sure, I'll take it.

=== @ Saffith 09/04/2021 04:37

Oh, uh... I accidentally merged it with another pull request? Sorry, haven't actually done this part much.
That one was pretty small, though. Not a problem, hopefully.

=== @EmilyV99 (discord: Emily) 09/04/2021 06:48

merged, fixed
(meta) thread name was changed: 💊🔓Message Strings Displaying Improperly - Alpha 95 Nightly 3

=== @EmilyV99 (discord: Emily) 09/04/2021 08:56

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594) @ NightmareJames

=== @EmilyV99 (discord: Emily) 09/05/2021 10:12

(meta) thread name was changed: ✅🔒Message Strings Displaying Improperly - Alpha 95 Nightly 3
## ✅🔒Enemy Editor Stats Bugged (#851)
@ Architect Abdiel opened this issue on 09/03/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/883402281150713948



=== @ Architect Abdiel 09/03/2021 17:25

I'm having a bug with the enemy editor. I went in to edit stats for enemies, saved the stats. Then when I went back into the enemy editor it had set its turn freq., halt rate, step speed and homing factor to 32767.

I tried this with enemies that had no scripts on them on a screen that also had no scripts on it.

I've edited ghost's shadows a little bit, but haven't touched anything else.

=== @EmilyV99 (discord: Emily) 09/03/2021 18:19

@arceusplayer11 (discord: Deedee) ?

=== @ Architect Abdiel 09/03/2021 18:31

Btw, this could be important. The only script I've added since then is the updated version of Newbie Boss. I don't think it would cause the problem though.
I had the old version and updated to the newest one.

=== @EmilyV99 (discord: Emily) 09/03/2021 18:32

a script literally could not cause a ZQ issue

=== @ Architect Abdiel 09/03/2021 18:33

That said, I've only edited a couple constants in ghost and Newbie Boss, which I can't imagine should have any effect, especially on normal enemies with no scripts on them.

=== @EmilyV99 (discord: Emily) 09/03/2021 18:33

scripts don't run in ZQ
and the code to run scripts isn't even in `zquest.exe`

=== @ Architect Abdiel 09/03/2021 18:34

I didn't think it would. But I figured I'd at least mention the only change I've made since starting.

=== @EmilyV99 (discord: Emily) 09/03/2021 22:06

...so, I edited an enemy, and instantly hit `OK`
Step speed became 1000
so I edited again, and hit `OK`
step speed became 32767, which is `MAX_SHORT`

=== @arceusplayer11 (discord: Deedee) 09/03/2021 23:07

Wtf

=== @ Architect Abdiel 09/03/2021 23:18

Yeah. That's how I felt too.
It wasn't like this 2 or 3 nightlys ago.

=== @EmilyV99 (discord: Emily) 09/03/2021 23:20

Nothing about the code directly surrounding it has been changed
So either random build corruption or some weird bug
But, I have to do a lot of work to build now, because some PRs were merged and broke compile

=== @arceusplayer11 (discord: Deedee) 09/03/2021 23:25

Oof

=== @ Architect Abdiel 09/04/2021 00:03

Hopefully figuring out what's happening isn't too difficult.

=== @EmilyV99 (discord: Emily) 09/04/2021 00:14

aye, should have it fixed tonight or tomorrow, hopefully
this can't be that outlandish, building it in debugger mode should lead me quickly to the issue

=== @ Architect Abdiel 09/04/2021 00:23

Okay. Thankfully there's an easy path like that.

=== @EmilyV99 (discord: Emily) 09/04/2021 01:21

So, I changed how `vbound` was set up internally
and it uh
was acting REALLY fucking weird
and not doing what it should have been at all
so, I re-worked it *again*
and now it is working again

=== @EmilyV99 (discord: Emily) 09/04/2021 02:08

so it was working again until I tried to build it in release instead of debug
and I fucking hate C++ once again

=== @EmilyV99 (discord: Emily) 09/04/2021 02:26

ok, got it fixed for real
fucking pain
will put out another build once I do a couple other things
(want to try to get the external parser working)

=== @ Architect Abdiel 09/04/2021 02:29

Sounds like a pain. Weird how it would work in debug but not release. Would think it would work in both.

=== @EmilyV99 (discord: Emily) 09/04/2021 02:29

some sort of linker error with template functions

=== @arceusplayer11 (discord: Deedee) 09/04/2021 03:36

@EmilyV99 (discord: EmilyV) was this a you error?

=== @EmilyV99 (discord: Emily) 09/04/2021 03:43

aye, certainly was
(meta) thread name was changed: ✅🔒Enemy Editor Stats Bugged
## Forward Bombs pierce enemy shields QR to item settings. (#852)
@ Alucard648 opened this issue on 09/04/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/883616813169127424



=== @ Alucard648 09/04/2021 07:37

Title says almost all. As well as adding Unblockable bool to LWeapons.
## ✅🔒Quest icons dont update when quest is changed (#853)
@ Mitsukara opened this issue on 09/04/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/883629323620343839



=== @ Mitsukara 09/04/2021 08:27

As requested, this is the old system where ZC loads all four quest icons for a quest when the save file's custom quest is first selected, and does not load them again even if the quest is changed in ZQuest.

=== @EmilyV99 (discord: Emily) 09/04/2021 08:28

^ Make togglable with a zc config, default auto-reload enabled (in case it's too laggy a load time for some people)
basically, just, on zc init, when it first loads all the saves, refresh the game icons from the quest file.

=== @EmilyV99 (discord: Emily) 09/04/2021 22:10

....ZCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

=== @EmilyV99 (discord: Emily) 09/04/2021 22:34

I uh
am so confused

=== @EmilyV99 (discord: Emily) 09/04/2021 22:40

so fucking confused
I literally am watching it load the new icon
but then it displays the old icon
what the fuck

=== @EmilyV99 (discord: Emily) 09/04/2021 22:46

oh wait

=== @EmilyV99 (discord: Emily) 09/04/2021 22:51

GAH I HATE THE TITLE SCREEN
BUT I THINK IT WORKS

=== @EmilyV99 (discord: Emily) 09/04/2021 23:12

@ Mitsukara

https://cdn.discordapp.com/attachments/883629323620343839/883852038428045312/zelda.exe

https://cdn.discordapp.com/attachments/883629323620343839/883852065300955176/zquest.exe
(meta) thread name was changed: 💊🔓Quest icons dont update when quest is changed

=== @EmilyV99 (discord: Emily) 09/05/2021 10:12

(meta) thread name was changed: ✅🔒Quest icons dont update when quest is changed

=== @ NightmareJames 09/08/2021 15:50

I had the same issue too, glad it's fixed
Thank you @ Mitsukara
## ❌🔒Scripted|Blank Hero Actions (#854)
@ Alucard648 opened this issue on 09/04/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/883686043629522974



=== @ Alucard648 09/04/2021 12:12

For scripting purposes.

=== @EmilyV99 (discord: Emily) 09/04/2021 21:26

🤢
no
`->Action` is a hack on a hack on a hack on a hack
and is the jankiest jank of all jank
I would say `not until rewrite`
....but `Acton` won't exist in the rewrite, because it's jank as fuck
(meta) thread name was changed: ❌🔒Scripted|Blank Hero Actions
## ❌🔒Command to Spawn Engine Grass and Bush (etc)Clippings (#855)
@ bigjoe opened this issue on 09/04/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/883833609532878878



=== @ bigjoe 09/04/2021 21:59

Self explanatory. Would help a lot with lifting scripts and such

=== @EmilyV99 (discord: Emily) 09/04/2021 21:59

#deleted-channel
duplicate
(meta) thread name was changed: ❌🔒Command to Spawn Engine Grass and Bush (etc)Clippings
## Disable F6 on certain screens (#856)
@ Mitsukara opened this issue on 09/05/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884184499041234964



=== @ Mitsukara 09/05/2021 21:13

Not sure how feasible this is, but it would be neat as a thing in either screen data settings, or with zscript.

=== @ P-Tux7 09/05/2021 22:06

i'd appreciate a method where you can disable f6 but also keep death continuing

=== @ P-Tux7 09/05/2021 22:07

so that in cases like these if you try to continue you don't press start on the "go back to the file selection" prompt because you think you're gonna be able to continue

=== @EmilyV99 (discord: Emily) 09/05/2021 22:28

ZScript can
make an F6 script
and stuff
don't remember exactly how you'd have to set it up at the moment

=== @EmilyV99 (discord: Emily) 09/10/2021 12:26

oh, also, uh
forgot the simpler way
which is `Input->DisableKeys[]`
so for instance
```cpp
bool b = ScreenFlag(some script screen flag or something);
Input->DisableKeys[KEY_F6] = b;```

=== @ P-Tux7 09/10/2021 15:32

zc still has the menu option with the mouse, right?

=== @EmilyV99 (discord: Emily) 09/10/2021 16:02

Oh, true
An F6 script method of handling it would handle that too
## increase compile zscript font (#857)
@arceusplayer11 (discord: Deedee) opened this issue on 09/06/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884578139295080468



=== @arceusplayer11 (discord: Deedee) 09/06/2021 23:17

I've gotten complaints that the text for compiling zscript is too small and hard to read (the window that gives you the errors). Could we bump that up?

=== @EmilyV99 (discord: Emily) 09/06/2021 23:18

You can't just bump font size, so you need to actually change the font to one that is larger
but uh
the external parser is gonna entirely change how compile errors work
...namely, they will be printed to external file, because the parser won't be part of the zquest process.

=== @EmilyV99 (discord: Emily) 09/07/2021 00:30

. . . so now my question is
how does loading external text files for display work
like, how the `Help` button in strings displays `zstrings.txt`
and how the buffer editing works
.....and would there be a way to call that with variable font, to allow different sizes.

=== @ Saffith 09/09/2021 14:19

https://docs.microsoft.com/en-us/windows/win32/procthread/creating-a-child-process-with-redirected-input-and-output?redirectedfrom=MSDN
https://tldp.org/LDP/lpg/node15.html#SECTION00730000000000000000
## ❌🔒Ability to switch subscreen types using an Ex button 4 (#858)
@ SkyLizardGirl opened this issue on 09/07/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884595344674004992



=== @ SkyLizardGirl 09/07/2021 00:26

Ability to switch subscreen types using an Ex button 4 in game.  You could make at least 3 different subscreens that can be used for different things optional for your game, kinda like how Ocarina of time has 3 or 4 different subcreens to switch through, only you could do this in ZC. This would Allow room to put more optional stuff in the game, such as Maps and more items etc.

=== @EmilyV99 (discord: Emily) 09/07/2021 00:26

no
no
no
no
no

=== @ SkyLizardGirl 09/07/2021 00:26

?

=== @EmilyV99 (discord: Emily) 09/07/2021 00:26

the subscreen is not being touched
at all
ever
ever
ever
no
use a scripted subscreen

=== @ SkyLizardGirl 09/07/2021 00:27

Ok

=== @EmilyV99 (discord: Emily) 09/07/2021 00:27

(meta) thread name was changed: ❌🔒Ability to switch subscreen types using an Ex button 4
## ✅🔒dark room color select (#859)
@ aslion opened this issue on 09/07/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884889866096226345



=== @ aslion 09/07/2021 19:56

Hey, I'd love to be able to change the system black & white colors, would be very nice for my quest with a limited color palette and I'm sure there'd be some other good applications for it as well.

=== @EmilyV99 (discord: Emily) 09/07/2021 20:09

I don't really see a good way to do this, system colors are meant to be constant in all quests
they are used for everything from walkflag cheats to showing flags in ZQ to lens marker etc

=== @ P-Tux7 09/07/2021 20:47

can't one just change the colour right before they save the quest and release it

=== @EmilyV99 (discord: Emily) 09/07/2021 20:49

that's not the point whatsoever
requiring the user to be smart in order to not break things is not acceptable
needs to be dumb-proof

=== @ aslion 09/08/2021 00:41

Would it be possible to at least make the screen transitions not always use system black then?
Though that's a pretty different request than this lol

=== @EmilyV99 (discord: Emily) 09/08/2021 00:47

You mean dark rooms, and perhaps

=== @EmilyV99 (discord: Emily) 09/21/2021 01:45

(meta) thread name was changed: dark room color select

=== @ aslion 09/21/2021 01:57

oh that isn't what I meant
but might fulfill the same purpose idk

=== @EmilyV99 (discord: Emily) 09/21/2021 05:24

woo

https://cdn.discordapp.com/attachments/884889866096226345/889743822811197540/zelda.exe

https://cdn.discordapp.com/attachments/884889866096226345/889743921276674068/zquest.exe

=== @EmilyV99 (discord: Emily) 09/21/2021 05:58

(meta) thread name was changed: 💊🔓dark room color select
[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
full nightly posted

=== @ aslion 09/21/2021 14:07

Would it possible to have something like this for the screen transition wipes too? ❤️

=== @ P-Tux7 09/21/2021 16:10

ooh and the lens' black and white

=== @ P-Tux7 09/21/2021 16:11

(no hurry because i'm using black and white so i don't need to change those)

=== @EmilyV99 (discord: Emily) 09/21/2021 16:25

@ aslion @ P-Tux7 make separate requests
(meta) thread name was changed: ✅🔒dark room color select
## Rock-Boulder Enemies (#860)
@ Guinevere opened this issue on 09/08/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884982521169862726



=== @ Guinevere 09/08/2021 02:04

these enemy types are pretty infuriating for the player to deal with, so if it's possible i'd like the data of the enemy affect it in some way
examples being where the random rate can maybe affect it's fall path of going left and right, and 0 would maybe make it only fall one direction and have step speed affect how fast it falls down

=== @ P-Tux7 09/08/2021 02:09

a more elegant solution for your quest might be to add an npc script to be like oot
where if link has a L2 shield or better, and he's facing the rock, it kills itself and produces an effect (probably a LW_SPARKLE made to look like a shattering rock, i don't know if rocks have a normal death effect)

=== @ P-Tux7 09/08/2021 02:12

i like your idea but there IS one issue with it that would prevent it from being executed well
i don't know if rocks respect enemy placement flags 0-9
so a right-down moving rock might spawn on the right-top of the screen. not very effective

=== @ Guinevere 09/08/2021 02:13

well that could also be added maybe
i got no idea how to do npc scripts
and besides i think it would be beneficial for everyone to have a simpler way to make them less frustrating to deal with that everyone has access to
and i feel that what i've suggested doesn't take away the spirit of how the enemy acts
<:nekoshrug:869489800271503400>

=== @ P-Tux7 09/08/2021 02:15

i'm pretty sure you just add a script and you can assign it to the enemy (which also means the script can reference its parent enemy or tell it what to do)

=== @ Guinevere 09/08/2021 02:17

i mean i don't know how to script npcs as in how they work, move, attack, etc;
## ⏱🔒more non Enemy enemy ideas (#861)
@ Dr00g opened this issue on 09/08/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/884989500810465280



=== @ Dr00g 09/08/2021 02:32

So we things like Traps, Rocks and Fireball shooters
Id like to see more stuff like fake doors from Mimish Cap and firebars from Alttp are these enemys just as hard to add as other enemies?

=== @ P-Tux7 09/08/2021 02:33

firebars have been done so far with ffc scripts and can surely be done with npc scripts
and fake doors are just temporary  step -> next + copycats that cycle from non-damaging to damaging then back again
though if you want more than one per screen you might need a script yeah

=== @EmilyV99 (discord: Emily) 09/08/2021 02:36

no new enemies until rewrite

=== @ P-Tux7 09/08/2021 02:52

that sounds like 2 years at minimum. not encouraging

=== @EmilyV99 (discord: Emily) 09/08/2021 02:54

trying to modify enemies just is not happening
because spaghetti mess firy burning destroying the entire engine if we try

=== @ P-Tux7 09/08/2021 03:09

oh i'm dumb
this is engine enemies only
not "engine OR scripted"
that's why i made so much ado of the potential script solutions

=== @EmilyV99 (discord: Emily) 09/08/2021 03:12

(meta) thread name was changed: ⏱🔒more non Enemy enemy ideas
## Priority music playing (#862)
@ Mani Kanina opened this issue on 09/08/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/885162435101728869



=== @ Mani Kanina 09/08/2021 13:59

A way to when you call a music track by script for playback, it will take priority. Meaning that it won't go back to the regular DMap track as soon as you switch screen.

Differenty priority levels on the calls would be nice:
Retain while on the same DMap or canceled by script.
Retain Globally no matter the DMap till canceled by script.
-
where did the message go?
ugh
anyway, guess I'll re type it

=== @ Mani Kanina 09/08/2021 14:01

Priority playback as an option when calling music playback via scripts. So that a track can be maintained and don't switch back to the DMap track as soon as you screen transition.

More than one priorty level would be nice too if you could set it when doing the call:
Retaining while on the same DMap till either you switch DMap or a scripts calls for the priority to be canceled (or new track to be played)

Retaining globally till a script calls for cancel or a script calls a new track.

=== @ mitchfork 09/08/2021 14:11

This would be nice. The current only way to do this is to update the dmapdata music track as well, which you then have to manually "clean up" later - often in a different script scope than you started with
## ❌🔒Displaying Item Strings  New Item Rule (#863)
@ NightmareJames opened this issue on 09/08/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/885223375507689482



=== @ NightmareJames 09/08/2021 18:01

Don't know if this would be simple or not, but this might need to be corrected/streamlined to Always/Once Per Level/One Time Only.  If an example needed @ Moosh and I can give one

=== @EmilyV99 (discord: Emily) 09/08/2021 20:39

I mean

![image](https://cdn.discordapp.com/attachments/885223375507689482/885262980625870928/unknown.png)
there are checkboxes right there
`once per level` isn't a thing, and that would be harder to add

=== @EmilyV99 (discord: Emily) 09/08/2021 20:43

@ NightmareJames

=== @ NightmareJames 09/08/2021 20:46

Hrmmmmmmmmm

=== @EmilyV99 (discord: Emily) 09/08/2021 20:46

`Only Held`, if not obvious, would only play it if you hold up the item
while `Always` determines if it is once-only or not

=== @ NightmareJames 09/08/2021 20:48

I'll review this and get back to you

=== @ NightmareJames 09/08/2021 20:51

I guess with keys and bombs I'd prefer you only get the message either first time or during the level, not after every time, you shut down the game, or run out of bombs

=== @ NightmareJames 09/08/2021 20:52

And bombs are tricky in classic quests because they disappear when you have zero and reappear when you collect another one

=== @EmilyV99 (discord: Emily) 09/08/2021 20:55

well that still wouldn't make it repeat
once-per-level isn't a thing
but once-only would be once-only
literally once it plays the string, it marks it as `read`, and it won't play it again ever

=== @ NightmareJames 09/08/2021 21:00

Yes, some items repeat and you'd definitely want that

=== @EmilyV99 (discord: Emily) 09/08/2021 21:00

it should either repeat every time or never
or only when held up
based on those flags
any other behavior is a bug to report

=== @ NightmareJames 09/08/2021 21:01

OK, I'll check my settings.  If Moosh and I see it again we will report it

=== @ NightmareJames 09/08/2021 21:12

Thank you

=== @EmilyV99 (discord: Emily) 09/21/2021 01:44

(meta) thread name was changed: ❌🔒Displaying Item Strings  New Item Rule
## Secret - Shutters (#864)
@ Alucard648 opened this issue on 09/08/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/885252676529557576



=== @ Alucard648 09/08/2021 19:58

Anyone, who still use NES dungeon Dmap type would want to allow opening NES dungeon shutters on secret trigger, either engine one, or scripted.

=== @EmilyV99 (discord: Emily) 09/08/2021 20:39

@arceusplayer11 (discord: Deedee) didn't you add this? Or were you planning to? seem to recall something

=== @arceusplayer11 (discord: Deedee) 09/08/2021 21:25

I was planning on adding it ye

=== @ FireSeraphim 09/09/2021 02:20

I would love to freaking have this. especially since getting block puzzle doors to actually stay open is a real pain in the ass

=== @ P-Tux7 09/09/2021 15:36

aren't permanent block puzzle secrets a thing now? or does that only apply to secrets and not doors

=== @EmilyV99 (discord: Emily) 09/09/2021 15:37

secrets
shutters are an *ENTIRELY* separate system
## ✅🔒Bomb and Key Messages Displaying More than once even when not checked Always or Held (#865)
@ NightmareJames opened this issue on 09/08/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/885305117329469500



=== @ NightmareJames 09/08/2021 23:26

Was told to report this.  I have indeed checked my settings.  Every time I die or run out, this will indeed reset again and play.  This definitely needs to be fixed.  Providing screen proof to show I do not have held or always checked off on bombs.  Will provide videos later if needed
My proof that nothing's checked off but the string being displayed.
![image](https://cdn.discordapp.com/attachments/885305117329469500/885305348884418590/unknown.png)
@ Moosh @ Mitsukara @EmilyV99 (discord: EmilyV)

=== @ Moosh 09/08/2021 23:28

Does Pick-Up Flags have something to do with it maybe? Also why's that check box hueg big?

=== @EmilyV99 (discord: Emily) 09/08/2021 23:29

... that's not a checkbox

=== @ Moosh 09/08/2021 23:29

Also you already made a report for this didn't you?

=== @EmilyV99 (discord: Emily) 09/08/2021 23:29

No he made a feature req

=== @ Moosh 09/08/2021 23:29


![image](https://cdn.discordapp.com/attachments/885305117329469500/885305920949731418/unknown.png)

![image](https://cdn.discordapp.com/attachments/885305117329469500/885305955552739328/unknown.png)
That sure looks like a check box?

=== @EmilyV99 (discord: Emily) 09/08/2021 23:29

@arceusplayer11 (discord: Deedee) you didn't remove the old pickupflags box
WTF
That used to be a textfield
And it's outdated by the new tab of checkboxes

=== @ Moosh 09/08/2021 23:30

strange

=== @EmilyV99 (discord: Emily) 09/08/2021 23:30

Dimi forgot to remove it... and apparently converted it to a checkbox?
Shouldn't be related

=== @ Moosh 09/08/2021 23:31

Dare I ask what happens if you check that and save?

=== @EmilyV99 (discord: Emily) 09/08/2021 23:31

Probably nothing?
Hopefully nothing?

=== @ Moosh 09/08/2021 23:32

Anyways, the behavior Nightmare's been having difficulty with is that every time the player dies, the bit flagging the string as having played gets reset

=== @EmilyV99 (discord: Emily) 09/08/2021 23:32

Yeah, that's certainly a bug

=== @ Moosh 09/08/2021 23:33

I could see it being an intended behavior depending on the quest
Like if pickup strings only go on non enemy drops, you might want them to refresh on a new play session
but a script can just as easily do that

=== @arceusplayer11 (discord: Deedee) 09/08/2021 23:35

(replying to @EmilyV99 (discord: Emily) "@arceusplayer11 (discord: Deedee) you did…"): ...fuck

=== @arceusplayer11 (discord: Deedee) 09/08/2021 23:37

I don't know how the hell it got turned into a check_proc. Did I sleepwalk to get both high and drunk and then wrote that while sleeping, drunk, and high?

=== @EmilyV99 (discord: Emily) 09/28/2021 15:10

the gui part of this was fixed

=== @arceusplayer11 (discord: Deedee) 10/09/2021 16:18

(meta) thread name was changed: ✅🔒Bomb and Key Messages Displaying More than once even when not checked Always or Held
Fixed

=== @ NightmareJames 10/14/2021 17:13

Confirmed fixed
## 💊🔓ZScript RNG is not predictable after SRand() (#866)
@ Saffith opened this issue on 09/09/2021

Status: closed

Labels: ['bug', 'needs-testing']

Source: https://discord.com/channels/876899628556091432/885611534187917383



=== @ Saffith 09/09/2021 19:44

ZScript needs a dedicated, well-defined RNG, maybe something from boost::random. Because its Rand() and SRand() just call the corresponding C functions, the behavior varies by platform and is affected by ZC's own use of rand().

I ran this on two different systems:
```SRand(0);
for(int i=0; i<10; i++)
    Trace(Rand(1000));```

On Windows:
```Global script 2 (RandTest): 38.0000
Global script 2 (RandTest): 719.0000
Global script 2 (RandTest): 238.0000
Global script 2 (RandTest): 437.0000
Global script 2 (RandTest): 855.0000
Global script 2 (RandTest): 797.0000
Global script 2 (RandTest): 365.0000
Global script 2 (RandTest): 285.0000
Global script 2 (RandTest): 450.0000
Global script 2 (RandTest): 612.0000```

On Linux:
```Global script 2 (RandTest): 383.0000
Global script 2 (RandTest): 886.0000
Global script 2 (RandTest): 777.0000
Global script 2 (RandTest): 915.0000
Global script 2 (RandTest): 793.0000
Global script 2 (RandTest): 335.0000
Global script 2 (RandTest): 386.0000
Global script 2 (RandTest): 492.0000
Global script 2 (RandTest): 649.0000
Global script 2 (RandTest): 421.0000```

=== @EmilyV99 (discord: Emily) 09/09/2021 19:45

I knew something seemed off

=== @EmilyV99 (discord: Emily) 09/19/2021 00:50

What should be done here is, add an `rng` class; maybe `randgenerator`
(to zscript)
and allow creation of multiple generators
each with their own state
and `randgenerator->Rand()`, `randgenerator->SRand()`
using some more deterministic rng on the backend as suggested

=== @EmilyV99 (discord: Emily) 09/21/2021 01:18

@ Saffith Mind testing for cross-platform consistency in the branch `2.55-newrand`?
if it's all good there, I can work on further zscript options, but that should cover the main engine rng being consistent.
(no need for `boost::`, since there's `<random>` in C++11+)

=== @ Saffith 09/22/2021 01:34

Ah, right, forgot about that. Yeah, might take me a day or two, but I'll try it out.

=== @EmilyV99 (discord: Emily) 09/23/2021 07:23

Nevermind, I went to test it and have run into an odd error

![image](https://cdn.discordapp.com/attachments/885611534187917383/890498667423891496/unknown.png)
I fail to decrypt quest files. If I spam a key to make it keep retrying sometimes it suddenly decides to succeed once...
I'm very curious what could be causing this
while the quest reader does use rng for some parts of encoding, it uses its' own function, not anything that I would have touched...

=== @EmilyV99 (discord: Emily) 09/23/2021 19:03

....ah
it's getting invalid temp file names

=== @EmilyV99 (discord: Emily) 09/23/2021 19:10

ah, duh. It doesn't expect negative output, so the call I used as the default can't be the default anymore.

=== @EmilyV99 (discord: Emily) 09/23/2021 21:31

@ Saffith fixed issues

https://cdn.discordapp.com/attachments/885611534187917383/890711992980111370/rng.qst
Build `2.55-randgen`, and run that quest in the built `zelda.exe`. It should print to console whether the RNG is consistent or not.

=== @EmilyV99 (discord: Emily) 09/23/2021 21:38

(also fixed the `unlink` issue for linux compile)

=== @ Saffith 09/25/2021 03:28

Didn't work, I'm afraid...
Damned if I can explain it, but apparently the only consistent function is `LRand` with no arguments.

=== @EmilyV99 (discord: Emily) 09/25/2021 03:28

Hmm

=== @ Saffith 09/25/2021 03:28

(Also, ZScript_Additions.txt says LoadRNG is in FileSystem)

=== @EmilyV99 (discord: Emily) 09/25/2021 03:29

Ah crap
`LRand()` is a straight call of the RNG with no filter
I think
While the rest use ` uniform_int_distribution`

=== @EmilyV99 (discord: Emily) 09/25/2021 03:33

Yeah, that seems right
So something is off with that

=== @ Saffith 09/25/2021 03:46

I'm not sure that's meant to be deterministic. It sounds like the `mt19937` is just used to seed it. I think you just need to call `(*rng)()` and adjust the result.

=== @EmilyV99 (discord: Emily) 09/25/2021 03:48

I need a way to make it uniform, hopefully, though
...time to get writing.

=== @EmilyV99 (discord: Emily) 09/25/2021 04:00

....yeah nope. Low-leaning it is.

=== @EmilyV99 (discord: Emily) 09/25/2021 04:06

@ Saffith Use this
```cpp
int zc_rand(int upper, int lower, zc_randgen* rng)
{
    if(!rng) rng = &default_rng;
    if(lower > upper)
    {
        int t = lower;
        lower = upper;
        upper = t;
    }
    // std::uniform_int_distribution<int> dist(lower,upper);
    // return dist(*rng);
    return signed(unsigned(zc_rand(rng))%unsigned((upper-lower)+1))+lower;
}```
`random.cpp` function update
see if that works

=== @ Saffith 09/25/2021 04:07

Sure. It'll have to wait until tomorrow; Windows has another hour of updates to apply before I can get back in.

=== @EmilyV99 (discord: Emily) 09/25/2021 04:08

ah fun

=== @ Saffith 09/25/2021 19:15

That seems to have done it.
Incidentally, the numbers from your test quest didn't change on Windows, so apparently that's what MSVC's implementation of `uniform_int_distribution` was doing anyway.

=== @EmilyV99 (discord: Emily) 09/25/2021 19:45

...what
that's not fucking uniform though
windooooows

=== @EmilyV99 (discord: Emily) 09/25/2021 23:51

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)

=== @EmilyV99 (discord: Emily) 09/25/2021 23:52

(meta) thread name was changed: 💊🔓ZScript RNG is not predictable after SRand()

=== @arceusplayer11 (discord: Deedee) 10/26/2021 16:05

Is this fixed?

=== @EmilyV99 (discord: Emily) 10/26/2021 16:20

Should be

=== @arceusplayer11 (discord: Deedee) 10/29/2021 05:17

Need someone to test if this is fixed, which... I actually don't think I can test this given how this depends on the OS

=== @EmilyV99 (discord: Emily) 10/29/2021 05:22

(replying to @ Saffith "That seems to have done it."): ^

=== @arceusplayer11 (discord: Deedee) 10/29/2021 05:24

```Emily — 09/25/2021
...what
that's not fucking uniform though
windooooows``` this confused me
But I'm guessing that's more "why didn't a previous fix work" and not "why doesn't the current fix work"?

=== @EmilyV99 (discord: Emily) 10/29/2021 05:26

"Why did the new implementation match the old implementation on windows"
i.e. the new method (which works cross platform, at the cost of not being a uniform distribution)
matched the old method on windows
meaning the windows implementation of `uniform_int_distribution`
....is NOT UNIFORM
but aye, should be fixed

=== @arceusplayer11 (discord: Deedee) 10/29/2021 05:33

Okay, good
## Rule to change NES boss HP distribution? (#867)
@ Moosh opened this issue on 09/10/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886000900525674527



=== @ Moosh 09/10/2021 21:31

Some NES bosses that have multiple NPC components (Patra, Gleeok, Moldorm, Lanmola) appear to have some weird additional HP distribution mechanics that both make setting their HP in the enemy editor unintuitive and can make reading it with scripts awkward. You can see examples of enemies juggling HP values around when used in combination with my Link & Enemy Damage And Healing Numbers script

https://www.purezc.net/index.php?page=scripts&id=364

So basically what I'd propose here is a rule that makes it so the values entering in the enemy editor are consistently treated as the HP values _per hitbox_. A Patra with an HP of 1 would have each eye die in one hit, a Gleeok would have the same HP per head and take damage linearly (instead of having heads break in weird patterns of hits like 5-3-3-3). And the segmented enemies wouldn't do whatever awkward jank they are doing.

Of course I know anything involving enemies is godawful. If this HP distribution stuff isn't something that can be reasonably modified feel free to reject in full or in part.

=== @EmilyV99 (discord: Emily) 09/10/2021 21:31

No chance I'm touching this
I've been burned by enemy code enough already

=== @ Moosh 09/10/2021 21:32

Kinda figured 😦

=== @EmilyV99 (discord: Emily) 09/10/2021 21:32

....if Dimi feels like adding it, I have no problem with that

=== @ Moosh 09/10/2021 21:32

@arceusplayer11 (discord: Deedee) ?

=== @ Moosh 09/10/2021 21:34

Also @ NightmareJames since this damage numbers bug has been a pain in both our sides with Downfall. IDK if there's any way to fix it in the script but I do imagine having these enemy types behave consistently with the rest of the engine would be a good start

=== @arceusplayer11 (discord: Deedee) 09/10/2021 21:36

Yeah I could try that
I have no qualms with touching this, but I need to get off my ass and finish Sideview Swimming

=== @ Moosh 09/10/2021 21:37

Sounds good. I'm in no particular rush on this, just figured it was a point worth raising
The patra and gleeok calcs in particular gave me grief in LQftH2. I had to fix them with a script 😩

=== @arceusplayer11 (discord: Deedee) 09/10/2021 21:39

unsure if I could actually remove the names of attributes based on QR, so might still have redundant "Head HP" setting

=== @ P-Tux7 09/10/2021 21:44

patras can't have just one number
they have different hp for kids and the core

=== @ Moosh 09/10/2021 21:49

It might be possible I made a stupid on that one. Would have to test. The way I remember it, setting HP on both resulted in the enemy not reflecting the values I set

=== @ P-Tux7 09/10/2021 21:49

oh well setting i have no idea
it works this way in z1 and by default in unscripted quest

=== @ Moosh 09/10/2021 21:52

Oh!
What the fuck
I set both HP to 1, removed the outer eyes from a Patra 2, same effect
So the outer eyes will die in one hit, inner eyes do not

=== @ Moosh 09/10/2021 21:57

WHAT THE FUCK
![image](https://cdn.discordapp.com/attachments/886000900525674527/886007531795775530/zc_screen00005.png)
IS THIS A HARDCODE?
WHY IS THIS A HARDCODE?
HOW LONG HAS THIS BEEN A HARDCODE!?
IT IS
![image](https://cdn.discordapp.com/attachments/886000900525674527/886007777917554759/zc_screen00006.png)
PATRA GIVES NO SHITS
/capslock

=== @EmilyV99 (discord: Emily) 09/10/2021 21:59

I've said I hate enemy code before
I should specify
NES bosses
Are about 5000000x worse than normal enemies

=== @ Moosh 09/10/2021 21:59

yup
At least this one shouldn't be hard to fix right? Ctrl+f for 24 in patra code blocks, find the one setting HP, and make it use the same attribute as the outer eyes?

=== @ P-Tux7 09/10/2021 22:10

twenty bucks that's how patra 2/3 were handled way back when
also i could have sworn one of the 2.55 alphas said something about a bugfix for inner patra eyes...?
should be in the notes because it was before 92

=== @ Moosh 09/10/2021 22:18

Well pre-2.5 I'm pretty sure everything was hardcoded
This particular enemy type I suppose just got overlooked in that transitional period

=== @ Saffith 09/11/2021 01:03

(replying to @ Moosh "At least this one shouldn't b…"): Ha, like we'd just write out the number!
`((enemy*)guys.spr(i))->hp=12*DAMAGE_MULTIPLIER;`
I've got patras up next to rewrite, so I'll take a look at them when I get back to that.

=== @ Moosh 09/11/2021 01:05

...damage multiplier is just 2 isn't it? I guess at least someone somewhere was thinking ahead, just not in the right ways

=== @EmilyV99 (discord: Emily) 09/11/2021 11:05

oh
DAMAGE_MULTIPLIER is in init data now
so
## Rocs Feather checkbox to work while swimming (overhead) (#868)
@ Mitsukara opened this issue on 09/10/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886002515622125589



=== @ Mitsukara 09/10/2021 21:37

I remember a long time ago testing if you could set Link->Jump while LA_SWIMMING was happening, and it worked pretty well as far as I could tell. So it'd be neat to have an option on Roc's Feathers where you could jump while you're in water. 

(Ideally this would be a distinct option from sideview swimming; in LA I think you could jump out of the sideview water, but not the overhead.)

=== @ P-Tux7 09/10/2021 21:46

i think there's a bigger issue in that i don't think any items can work while swimming, i know the whistle doesn't
do potions, even?

=== @EmilyV99 (discord: Emily) 09/10/2021 21:46

don't think any items do, aye
because diving

=== @ P-Tux7 09/10/2021 21:47

this would have been more feasible pre-a/ex1/ex2 item usage because a was just for the sword/diving

=== @ Mitsukara 09/10/2021 23:01

I guess the controls are a tricky issue. Maybe the feather could just override the dive command if it's on the same button?
once you _have_ jumped out of the water, you can use other items in midair until you fall in, and I think that worked okay when I tried it
## ❌🔒No-Diving Flippers checkbox (#869)
@ Mitsukara opened this issue on 09/10/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886002943730536488



=== @ Mitsukara 09/10/2021 21:39

For some reason, No Diving is a screen flag (I think? might be a quest rule), but it would be neat to have an option for level 1 flippers that can't dive, and level 2 flippers that can. Similar to the Zora's Scale in OOT.

This might already be in 2.55 (if so I apologize).

=== @EmilyV99 (discord: Emily) 09/10/2021 21:43

this was added to 2.55 approximately 3 years ago
IIRC
(meta) thread name was changed: ❌🔒No-Diving Flippers checkbox
## ❌🔒Modifiable Conveyor Combo Speed? (#870)
@ Anthus opened this issue on 09/11/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886066828923764756



=== @ Anthus 09/11/2021 01:53

Would it be possible to have a setting for conveyor combos to change their speed? Speed as in, how fast they move Link/ Hero? They could even be able to go so fast that they function as one way conveyors, or alternately "one way" could also be a toggle. Thanks for reading!

=== @ P-Tux7 09/11/2021 03:26

it already is possible from dimi
she also added the ability to set both their x and y speeds, meaning that you can have diagonal conveyors of any angle

=== @ Anthus 09/11/2021 03:46

oh shit, nice!
thanku dimi!

=== @ Anthus 09/11/2021 03:47

(this thread can prolly be archived then lol)

=== @EmilyV99 (discord: Emily) 09/11/2021 11:05

(meta) thread name was changed: ❌🔒Modifiable Conveyor Combo Speed?
## ❌🔒Allow playing multiple sounds or music at once. (#871)
@ OmegaX opened this issue on 09/11/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886124915441426442



=== @ OmegaX 09/11/2021 05:44

This would be for useful for example: a cutscene where music, voice acting and occasional sound being played simultaneously. Currently we can only have one music file and one sfx playing at a time.

=== @EmilyV99 (discord: Emily) 09/11/2021 11:06

Err, only 1 sfx?
afaik you can have all 255 sfx playing at once

=== @EmilyV99 (discord: Emily) 09/21/2021 01:43

(meta) thread name was changed: ❌🔒Allow playing multiple sounds or music at once.
## ✅🔒Screen MIDI doesnt work on screen 128-129 (guy caves) (#872)
@ Mitsukara opened this issue on 09/11/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/886307258865164378



=== @ Mitsukara 09/11/2021 17:48

Not sure if this is a "bug" per se or some sort of intended behavior, but when you set the screen midi on guy caves, it still doesn't play. I can't think of any advantage to this behavior; it'd be neat to be able to set music in a guy cave.

...I'm not sure whether it works or not in Item Cellars and Passageways? I forgot to test that before I posted this

=== @EmilyV99 (discord: Emily) 09/11/2021 17:56

Gonna guess it reads from the main screen, not screen 80
Screen 80+ shit is jank as fuck

=== @ Mitsukara 09/11/2021 17:57

ah
For what it's worth, scripts _can_ use Game->PlayMIDI() and Game->PlayEnhancedMusic() on those screens without issue

=== @EmilyV99 (discord: Emily) 09/20/2021 22:41

@ Mitsukara
![image](https://cdn.discordapp.com/attachments/886307258865164378/889642515291054080/unknown.png)

https://cdn.discordapp.com/attachments/886307258865164378/889642566176366642/zelda.exe

https://cdn.discordapp.com/attachments/886307258865164378/889642573503815720/zquest.exe

=== @ Mitsukara 09/20/2021 22:42

Nice!

=== @EmilyV99 (discord: Emily) 09/20/2021 22:42

given, you can't test it, but it seems to work

=== @EmilyV99 (discord: Emily) 09/20/2021 22:44

won't be enabled by default
(meta) thread name was changed: ✅🔒Screen MIDI doesnt work on screen 128-129 (guy caves)
## Zquest -play music from within quest- option (#873)
@ FireSeraphim opened this issue on 09/11/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886308876645957703



=== @ FireSeraphim 09/11/2021 17:55

I would like to suggest an option in the zquest editor under media named "play music from within quest", which as labeled would play the midis already inside the quest file, with the internal loop data that's added. This is so those who want to can listen to their quest's midi soundtrack while editing said quest.
@EmilyV99 (discord: EmilyV) Now I have a proper thread for this.

=== @ FireSeraphim 09/11/2021 17:57

perhaps it should be named "Play Midi from within quest" or something that less of a mouthful. Perhaps "Play Quest MIDI" or something like that

=== @ Alucard648 09/11/2021 18:55

Also supporting this request. Helps choosing music for quests.

=== @ NightmareJames 09/11/2021 23:16

Thirding this
Even if it has to wait a bit for other bugs to be fixed

=== @ FireSeraphim 09/14/2021 23:24

@EmilyV99 (discord: EmilyV) any thoughts on this?

=== @EmilyV99 (discord: Emily) 09/14/2021 23:24

👍

=== @ FireSeraphim 12/01/2021 19:54

any progress on this one?

=== @ FireSeraphim 12/22/2021 21:53

any progress on this one?

=== @EmilyV99 (discord: Emily) 12/23/2021 00:42

Not yet

=== @ FireSeraphim 07/22/2022 09:12

bump

=== @EmilyV99 (discord: Emily) 07/22/2022 09:17

@connorjclark (discord: connorclark)
## ❌🔒Centered Hookshot (#874)
@ Mitsukara opened this issue on 09/11/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/886336178490597447



=== @ Mitsukara 09/11/2021 19:43

A quest or item rule that makes the hookshot centered on Link's position, like in an official Zelda game, instead of "left handed", like the weird janky ZC way.

=== @EmilyV99 (discord: Emily) 09/21/2021 01:58

Err, looking at the hitboxes of the hookshot using the show hitbox cheat, it looks pretty well centered
the tiles in classic are drawn off to one side, though

=== @EmilyV99 (discord: Emily) 09/29/2021 11:15

so there's not much to add here
(meta) thread name was changed: ❌🔒Centered Hookshot
## ✅🔒Janky hookshot chain rendering, when hero`s position is altered by script (#875)
@ Alucard648 opened this issue on 09/12/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/886661984811118662



=== @ Alucard648 09/12/2021 17:18

1. Test quest: https://drive.google.com/file/d/1qVcAgOzrdR5wjVBoazz4dOXhXgC0E1ed/view?usp=sharing
2. Stand on moving platform.
3. Try to hookshot grab combos behind solid block, while riding platforn.

If hookshot head hits solid wall while returning after missed shot, weird things happened with chain rendering.

=== @ Alucard648 09/12/2021 17:32

```ffc script moving{
    void run(){
        while (true){
            if (RectCollision(Link->X+6, Link->Y+6 ,Link->X+11, Link->Y+11, this->X, this->Y, this->X + this->EffectWidth, this->Y + this->EffectHeight)){
                if (Link->Z == 0){
                    Link->X += this->Vx;
                    Link->Y += this->Vy;
                }
            }
            Waitframe();
        }
    }
}```

=== @ Mitsukara 09/13/2021 03:19

I had problems with this back when I was making LaZPoC too. It was so bad I actually made my chain blank and drew a new one, but that's not a great solution
I think just moving the hookshot's position at all screwed up the chain drawing quite a bit
(since I did that to make the screen-wraparound hookshot)

=== @arceusplayer11 (discord: Deedee) 10/10/2021 15:31

Oh god this is a weird one
It... looks like its morphing into a diagonal hookshot?
what the hell...

=== @arceusplayer11 (discord: Deedee) 10/10/2021 16:21

okay, nevermind, figured out why it might bug out
really easy fix

=== @arceusplayer11 (discord: Deedee) 10/10/2021 16:27

(meta) thread name was changed: ✅🔒Janky hookshot chain rendering, when hero`s position is altered by script

=== @arceusplayer11 (discord: Deedee) 10/10/2021 16:30

For those curious: there's a hookshot startx and a hookshot starty variable, and whenever stuff like conveyors move link, it updates those... but it wasn't being updated for the script move functions.

=== @ Alucard648 10/10/2021 16:41

Is it possible to do this fix in 2.53.x branch, or 2.53.1 beta 55 is already final?

=== @arceusplayer11 (discord: Deedee) 10/10/2021 17:07

Possibly, yeah
## ✅🔒CSet 9 from item cellar is retained when exiting cellar (#876)
@ 4matsy opened this issue on 09/14/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/887137611301392444



=== @ 4matsy 09/14/2021 00:48

So NightmareJames just ran into this one in Level 6 of ZNR, in the boss key room, during a stream. Went downstairs to collect a boss key, without killing all of the CSet 9 Keese in the room.
This was a brown dungeon with many dark rooms in an NES-tileset quest, so these Keese were colored black to blend in with the darkness in the room. Upon exiting the item cellar, the Keese in the (upstairs) dungeon room had picked up the CSet 9 from the item cellar's level palette, which was cyan like the Level 1 palette in the classic tileset, making the Keese no longer blend in with the darkness.

=== @ NightmareJames 09/14/2021 03:40

Stream link:  https://youtu.be/KkNMYKjOSDM
Quest in question, Lv. 4 cheat code "test" for this
https://cdn.discordapp.com/attachments/887137611301392444/887181099221016656/zeldanesremastered_V2_1_publicbeta1.zip
This one's been happening for a while, waiting for a second on it though, which @ 4matsy just did

=== @ P-Tux7 09/14/2021 06:00

i think this just needs a qr "cellars copy current dmap palette"
it may apply to staircases as well

=== @arceusplayer11 (discord: Deedee) 10/10/2021 18:52

Okay, looking at it, it seems to happen only if the original screen is a dark screen

=== @arceusplayer11 (discord: Deedee) 10/10/2021 19:09

Fixed

=== @arceusplayer11 (discord: Deedee) 10/10/2021 19:14

(meta) thread name was changed: ✅🔒CSet 9 from item cellar is retained when exiting cellar
## ⏱🔒FFC Freeform Combos Need More Drawover Layers (#877)
@ SkyLizardGirl opened this issue on 09/14/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/887274595663630377



=== @ SkyLizardGirl 09/14/2021 09:52

FFC Freeform Combos Need More Drawover Layers

![image](https://cdn.discordapp.com/attachments/887274595663630377/887274630920962088/unknown.png)
There is only 1 Drawover layer, but i need it some levels higher.

=== @ mitchfork 09/14/2021 12:51

actually would be nice to be able to set FFC layer

=== @EmilyV99 (discord: Emily) 09/14/2021 13:35

not happening until rewrite
adding more flags to ffcs costs too much memory

=== @ mitchfork 09/14/2021 14:03

rip

=== @ P-Tux7 09/14/2021 18:21

...could we make one of the arbitrary FFC arguments used to determine what layer it is?

=== @ P-Tux7 09/14/2021 18:41

It'd be hacky but better than nothing
Maybe a QR that enables an Init Data field which lets you set which of the argument #s determines the layer of the FFC
Or just a QR hardcoding it to the last argument

=== @EmilyV99 (discord: Emily) 09/14/2021 18:59

beyond the ffc stuff, it would take a lot of fucking with draw shit
I'd really rather not until rewrite

=== @ SkyLizardGirl 09/17/2021 04:35

Aww

=== @EmilyV99 (discord: Emily) 09/21/2021 01:41

(meta) thread name was changed: ⏱🔒FFC Freeform Combos Need More Drawover Layers
## ✅🔒Secrets-Next (#878)
@ vlamart opened this issue on 09/14/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/887478689154072598



=== @ vlamart 09/14/2021 23:23

Secrets->Next doesn't seem to react with Enemies->Secrets until you leave the room

=== @EmilyV99 (discord: Emily) 09/20/2021 20:56

.....well
Nothing but `16-31` trigger to `Enemies->Secrets` until you leave the room
.....that seems fun.

=== @EmilyV99 (discord: Emily) 09/20/2021 21:33

Fixed with compat rule
(meta) thread name was changed: ✅🔒Secrets-Next
## More NPC Touch Effect Counters (#879)
@ Mitsukara opened this issue on 09/15/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/887520921324240976



=== @ Mitsukara 09/15/2021 02:11

In the enemy editor, there's a field for "Touch Effects" on the Walking Enemy type. Options include "Drain Rupees" (although a negative number will actually increase the rupees), as well as "Drain Life" and "Drain Magic". Can this be easily expanded to do things like Drain/Increase CR_SCRIPT1, etc?

=== @ Mitsukara 09/15/2021 02:13

Might warrant a separate request, but, it would also be neat if there was a "stun Link" option which just prevented Link movement (like NoAction()) for a certain amount of time, but ideally in a way where Link won't get stunned before he can move again. However, something like that could also be left to scripting.

=== @ Mitsukara 09/15/2021 02:15

Neither of these are high priority, but if it's easy to add it'd be neat.

=== @EmilyV99 (discord: Emily) 09/15/2021 02:20

`Link->Defense[]` has a stun option
although I think that's only partially implemented (i.e. script only) at the moment? ( @arceusplayer11 (discord: Deedee) any info on that? )
more touch drain options would make total sense

=== @arceusplayer11 (discord: Deedee) 09/15/2021 02:30

Link->Defense is implemented in the UI
jman did that
It's under Quest->Player

=== @EmilyV99 (discord: Emily) 09/15/2021 02:33

Ah nice
That's the answer for the stun part, @ Mitsukara

=== @ Mitsukara 09/15/2021 02:35

Cool
Pushing my luck on this general subject... does it sound complicated to make these touch effects be applicable to weapons?

=== @EmilyV99 (discord: Emily) 09/15/2021 02:37

Weapons should frankly be easy... but enemy/item attributes to set the weapons is a chunk more work.
(Neither out of the question; though I'd make a separate thread for that)

=== @ P-Tux7 09/15/2021 03:26

Couldn't one just have two checkboxes for the drain effect to apply to enemy touch, enemy weapon, both, or none?

=== @EmilyV99 (discord: Emily) 09/15/2021 03:29

Firstly, that still needs adding vars. Checkboxes or dropdowns, still adding stuff. 
Secondly, then the next feature request that comes in is "hey I want to be able to have the touch drain X and the weapon drain Y"

=== @ P-Tux7 09/15/2021 03:35

I don't particularly care if it can just be scripted anyways (similar to curse effects on non-walking enemies and eweapons)

=== @ Alucard648 09/15/2021 17:59

What about  also add siilar expansion to eating enemies - Eat(Ccounter XX)?

=== @ P-Tux7 09/15/2021 18:27

hmm can script reads of link's eaten status read WHICH enemy id he is being eaten by?

=== @ Alucard648 09/15/2021 22:12

(replying to @ P-Tux7 "hmm can script reads of link'…"): ```//Returns pointer to NPC that has eaten hero. Otherwise returns invalid pointer.
npc EatenBy(){
    if (Hero->Eaten) return;
    for (int i=1; i< Screen->NumNPCs();i++){
        npc n = Screen->LoadNPC(i);
        if ((n->X == Hero->X)&&(n->Y == Hero->Y)) return n;
    }
    return;
}```

As of 2.55 latest alpha.

=== @EmilyV99 (discord: Emily) 09/15/2021 22:15

is there not a `HasLink` or somesuch readable on enemies?
(There *is* internally, so, would not be difficult to add if it's missing)

=== @ Alucard648 09/15/2021 22:23

(replying to @EmilyV99 (discord: Emily) "is there not a `HasLink` or s…"): No such thing, as of latest alpha.

=== @EmilyV99 (discord: Emily) 09/15/2021 22:23

1. Add more counters to touch effect drain
2. Add `bool npc->HasLink;`, read-only, to zscript
(meta, MessageType.pins_add) 
(your method might fail if multiple enemies are at the exact same x/y, this new addition would prevent that)
## ✅🔒Fairy spawn limitations (#880)
@ Mitsukara opened this issue on 09/15/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/887599395028213791



=== @ Mitsukara 09/15/2021 07:23

ZC has some sort of limitation that makes it so a second fairly will not spawn* if there is a second fairy onscreen, even with a 100% item drop rate for just a fairy (moving; haven't tried stationary). 

 (* - _Usually, inconsistently_. Sometimes I could only get one to spawn, sometimes a second one would appear, but definitely not more than 2).

This may be a deliberate bit of code to try to simulate some sort of NES limitation (though it's not even accurate at that because you can have at least two fairies in Zelda 1), but it doesn't make sense / might warrant some kind of QR change or something. 

~~(Why do I have a feeling this is one of those "a previous dev had a hard-on for difficulty" bits of code, like the thing about not letting people use that one cheats program....)~~

However, spawning at least 3 fairies with FFC scripts works normally as expected, thankfully. So this is just something about how they work as item drops.

Was discussed here (found by P-Tux): https://discord.com/channels/876899628556091432/887461043117391872/887550177739694102

Note: This isn't a new bug, and I haven't confirmed it still works this way in 2.55 (though I would think P-Tux would know if it didn't?). Only tested it in 2.50.2 linux myself.

=== @ P-Tux7 09/15/2021 07:53

i think zelda 1 has a 1 fairy limit - if a fairy is on-screen, no enemies will drop fairies until that one is gone
and the other fairies spawning are when two fairy-spawning enemies are killed on the same frame, meaning that both checks for a fairy on-screen fail
it takes some careful practice or luck to perform, which is probably why phantom menace thought that 1 fairy was the limit

=== @ Mitsukara 09/15/2021 19:00

I suppose it makes some sense but it'd be nice to have the option to disable it for modern quests, at least.

=== @EmilyV99 (discord: Emily) 09/15/2021 19:07

probably something to do with the fact that fairies are both an enemy and an item

=== @arceusplayer11 (discord: Deedee) 10/09/2021 17:04

this is pain
fairies are hardcoded
this is a feature request to surpass ~~metal gear~~ sideview swimming

=== @arceusplayer11 (discord: Deedee) 10/09/2021 19:13

Fixed; also have a new QR as well to let fairies spawn with different directions cause that annoyed me
(meta) thread name was changed: ✅🔒Fairy spawn limitations
@ Mitsukara the real reason this was implemented the way it was was because the item just grabbed the first fairy enemy on screen to attach itself to it
so I had to rewrite how fairies worked to let multiple exist

=== @ P-Tux7 10/09/2021 19:58

Why are fairies enemies?

=== @EmilyV99 (discord: Emily) 10/09/2021 19:59

because moving

=== @ P-Tux7 10/09/2021 19:59

I understand they're Guys but enemy Goriyas and Guy Goriyas are different
(replying to @EmilyV99 (discord: Emily) "because moving"): I'd have thought they would be an LWeapon in that case

=== @EmilyV99 (discord: Emily) 10/09/2021 19:59

guy fairies and item fairies are differnet too
lweapons don't have movement behaviors other than straight line

=== @ P-Tux7 10/09/2021 20:00

boomerangs?

=== @EmilyV99 (discord: Emily) 10/09/2021 20:00

that's straight line, and when it dies, straight line
to add proper movement behaviors and the variables to store that it'd need to be a subclass of weapon
which would be annoying
as all `lweapon`/`eweapon` are a single class, no subclasses

=== @ P-Tux7 10/09/2021 20:01

okay so what did dimi turn the fairies into now?

=== @EmilyV99 (discord: Emily) 10/09/2021 20:01

nothing changed
it's just that it no longer just grabs the first fairy enemy on screen for every fairy
it actually makes separate ones for each

=== @ P-Tux7 10/09/2021 20:09

well that's going in the lttp tileset
always-spawn-fairy combos like in the eastern palace pots

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:45

(replying to @ P-Tux7 "always-spawn-fairy combos lik…"): they also no longer default to facing up with a new QR
that annoyed me when I made lttp-styled fairy fountains in HF

=== @ P-Tux7 10/09/2021 20:47

wait how'd you do it if more than one fairy couldn't exist

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:48

literally had to rewrite the system to give each fairy item a value that stores it's enemy counterpart

=== @ P-Tux7 10/09/2021 20:48

no i meant in HF

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:48

See here's the weird thing
the limitation for some reason doesn't exist for scripts
and I don't know why

=== @ P-Tux7 10/09/2021 20:48

that *works*?

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:48

yeah
but the code seemed to suggest that it wouldn't

=== @ P-Tux7 10/09/2021 20:49

i'd have thought zc would just start crying if ordered to make multiple fairies

=== @arceusplayer11 (discord: Deedee) 10/09/2021 20:49

it's possible the limitation is just poor understanding on my part
but uh, the math used for tying fairies to enemies was fuckin weird
glad it's deprecated
## ⏱🔒Bridge Combo or Bridge Flag for Liquid Combos (#881)
@ bigjoe opened this issue on 09/16/2021

Status: closed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/887961556380450826



=== @ bigjoe 09/16/2021 07:22

A bridge combo that allows over walking and under-swimming depending upon what combo you are approaching it from. This seems like a long shot given the dislike for liquid related stuff, but it would be a cool and useful feature.

=== @EmilyV99 (discord: Emily) 09/16/2021 13:58

over/under is not happening until rewrite

=== @EmilyV99 (discord: Emily) 09/21/2021 01:42

(meta) thread name was changed: ⏱🔒Bridge Combo or Bridge Flag for Liquid Combos
## Editable Guys (#882)
@ P-Tux7 opened this issue on 09/16/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/888085826460852256



=== @ P-Tux7 09/16/2021 15:36

Guys are already editable in the 2.55 alphas. This allows for you to, for example, change Ama to CSet 7 like in BS Zelda with no scripting or 8-bit mode. I would like to request this to be retained, and for them to be renamed to "Goriya (Guy)" etc. to reduce confusion.
Something else that might also be cool is to allow rooms to have the room's Guy selector read all "Guy" enemies from the enemy list, and allow you to select one, allowing for custom Guys.  I know a lot of people just use invisible Guys and make the graphics as tiles so the Guys don't disappear, but I know users like NightmareJames like to use real Guys and even use scripts to change the room's Guy graphic.

=== @ P-Tux7 09/16/2021 15:47

Or in worst-case scenario, just entering the ID # of the enemy to be the Guy. Though it's not idiot-proof

=== @EmilyV99 (discord: Emily) 09/16/2021 15:55

I have no fucking clue
guys are janky jank mcjank

=== @ P-Tux7 09/16/2021 17:42

well i mean what does the pick the room guy dialog set
just look there

=== @ 4matsy 09/16/2021 17:43

_suddenly remembers that many eldritch horrors are rumored about the infamous "guys.cpp" file in the source code, which was also among the largest in the code... <\_<'_

=== @EmilyV99 (discord: Emily) 09/16/2021 17:45

I mean, pretty sure that's hardcoded @ P-Tux7

=== @EmilyV99 (discord: Emily) 09/16/2021 17:46

also `guys.cpp` is everything enemy related, not just room guys

=== @ P-Tux7 09/16/2021 17:47

i mean if what setting a guy in the list does is puts a numerical ID in the room as to what enemy to use, then a dialog box that allows setting that would allow for non-default guys

=== @ 4matsy 09/16/2021 17:47

Ah, so that's why the guys were made editable along with the enemies. I was wondering about that.

=== @EmilyV99 (discord: Emily) 09/16/2021 17:47

guys are jankily made part of enemies
even though they shouldn't realistically be remotely related
because, you know, jank jank mcjank jank

=== @ P-Tux7 09/16/2021 17:54

i mean they do have enemy-like features
they poof in, they can be "hurt", they count as enemies for purposes of door opening (feed the goriya, life or money etc.)

=== @EmilyV99 (discord: Emily) 09/16/2021 17:57

and hookshot chainlinks share a lot with weapons
but they aren't stored in the same spritelist as weapons
## midi copy-pasting + moving entries (#883)
@ FireSeraphim opened this issue on 09/16/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/888100481900101652



=== @ FireSeraphim 09/16/2021 16:34

I don't see why this isn't a thing already in Zquest's midi menu. I would like to request the ability to move midi entries up and down the list via ctrl+up and ctrl+down and the ability to copy and paste midi entries in zquest's midi list via ctrl+c and ctrl+v
@EmilyV99 (discord: EmilyV) Sorry to pester you again but I figure you would probably be interested in seeing this.

=== @EmilyV99 (discord: Emily) 09/16/2021 16:35

love that you ping me as I'm already reading it XD

=== @ FireSeraphim 09/16/2021 16:35

sorry.

=== @EmilyV99 (discord: Emily) 09/16/2021 16:35

nothing to apologize for, just funny timing

=== @ FireSeraphim 09/16/2021 16:35

Also I hope this QOL suggestion isn't too much

=== @ FireSeraphim 09/16/2021 16:36

I kinda like to keep my quest midi list tidy and the lack of these features kinda make that impossible.

=== @ FireSeraphim 12/01/2021 19:54

Any progress on this?

=== @ FireSeraphim 12/22/2021 21:53

any progress on this one?

=== @EmilyV99 (discord: Emily) 12/23/2021 00:41

Nope, not yet

=== @EmilyV99 (discord: Emily) 12/23/2021 07:35

(replying to @ FireSeraphim "I don't see why this isn't a…"): Do any menus in ZC already have `ctrl+up`/`ctrl+down` for anything like this?

=== @EmilyV99 (discord: Emily) 12/23/2021 08:52

...I tried adding copy/paste here, and it just crashed. Don't have the energy to get this crap working, MIDIs are terrible to work with
@arceusplayer11 (discord: Deedee) can feel free
if she feels like

=== @arceusplayer11 (discord: Deedee) 12/23/2021 08:56

see the best part is because I read all these pings, the ping disappears and I forget where I was pinged
so in the end, I save myself from suffering via my lack of memory

=== @EmilyV99 (discord: Emily) 12/23/2021 08:57

lol
but yeah, so, the problem I immediately see
is midis are pointers
that have within them pointers to tracks
and I thought I understood it well enough copying the code that existed already
but then it just crashed
and I went `nope`

=== @EmilyV99 (discord: Emily) 12/23/2021 09:00

(meta) thread name was changed: midi copy-pasting + moving entries

=== @ FireSeraphim 07/22/2022 09:12

bump

=== @EmilyV99 (discord: Emily) 07/22/2022 09:18

@connorjclark (discord: connorclark)
## ✅🔒Init Data Broken (#884)
@ Jared opened this issue on 09/17/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888230580855136327



=== @ Jared 09/17/2021 01:11

Initial Data boxes are broken. First page you can't hit cancel

![image](https://cdn.discordapp.com/attachments/888230580855136327/888230614900297788/unknown.png)

![image](https://cdn.discordapp.com/attachments/888230580855136327/888230700044681326/unknown.png)

=== @EmilyV99 (discord: Emily) 09/17/2021 01:12

wah
wtf
presuming this is in the build just posted?
Does it occur in the previous build?

=== @ Jared 09/17/2021 01:15

Yes this is the build you just put up
I don't think it happened on the one before, but I don't remember

=== @EmilyV99 (discord: Emily) 09/17/2021 01:26

so it seems that the frames are all messed up
and the cancel button is just not working because a frame is in front of it, no other reason

=== @EmilyV99 (discord: Emily) 09/17/2021 01:29

@ Saffith any idea why `jwin_frame_proc` is messed up?

=== @ Saffith 09/17/2021 01:30

Nope, I didn't touch that one.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:31

...also
```cpp
do                                             \
{                                              \
    if(dlg->flags&D_NEW_GUI)                   \
    {                                          \
        int ret = new_gui_event(dlg-1, event); \
        if(ret >= 0)                           \
            return ret;                        \
    }                                          \
} while(false)```
why `do {} while(false)`?

=== @ Guinevere 09/17/2021 01:31

the button works, you just can't just use the mouse to click on it.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:31

yeah, because the frame is in the way

=== @ Guinevere 09/17/2021 01:32

ah

=== @EmilyV99 (discord: Emily) 09/17/2021 01:32

when you click, only the top widget at that position gets the click message

=== @ Guinevere 09/17/2021 01:32

gotcha

=== @ Saffith 09/17/2021 01:34

(replying to @EmilyV99 (discord: Emily) "why `do {} while(false)`?"): It's basically a trick to make it work like a regular statement.
https://www.generacodice.com/en/articolo/41901/why-use-apparently-meaningless-do-while-and-if-else-statements-in-macros-

=== @EmilyV99 (discord: Emily) 09/17/2021 01:35

...why not just do `{}`
```cpp
{                                              \
    if(dlg->flags&D_NEW_GUI)                   \
    {                                          \
        int ret = new_gui_event(dlg-1, event); \
        if(ret >= 0)                           \
            return ret;                        \
    }                                          \
}```
would that not work identically?
oh
I see
....that's...... kinda jank as fuck
but ok
> Of course, it could (and probably should) be argued at this point that it would be better to declare BAR as an actual function, not a macro.

=== @ Saffith 09/17/2021 01:37

Yeah, but I wanted it to be able to return from the proc.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:37

you'd just do

=== @EmilyV99 (discord: Emily) 09/17/2021 01:39

```cpp
int GUI_EVENT(DIALOG* d, int event)
{
    if(d->flags&D_NEW_GUI)
        return new_gui_event(d-1, event);
    return -1;
}```
then
```cpp
int ret = GUI_EVENT(d, whatever);
if(ret >= 0) return ret;
```
....meh, either way
not a big deal

=== @ Saffith 09/17/2021 01:40

I prioritized minimizing the code changes in the existing procs, basically.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:40

fair

=== @ Saffith 09/17/2021 01:40

Anyway, I'm not seeing a problem with the frames myself...
And it doesn't look like anything weird happened to the code.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:41

oh, is it a windows only issue, just like the sprite invisibility?
that sounds fucking fun

=== @ Saffith 09/17/2021 01:41

Yep, seems to be.
And it's pretty simple, so I have no clue what the problem could be.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:41

oh ffs
question
you changed some function pointer stuff to no longer use `(*func)(params)` but instead `func(params)`
I'm guessing that's a c++ change?
I'm guessing something to do with `==` on func pointers is different
which would break `large_dialog()`

=== @ Saffith 09/17/2021 01:42

No, that was to do with the new ListData.

=== @EmilyV99 (discord: Emily) 09/17/2021 01:42

and likely cause something approximately like this
oh
hmmm

=== @EmilyV99 (discord: Emily) 09/17/2021 01:49


![image](https://cdn.discordapp.com/attachments/888230580855136327/888240145453694996/unknown.png)
well it appears not to be broken in small mode
so my suspicion of `large_dialog` seems correct

=== @EmilyV99 (discord: Emily) 09/17/2021 02:07

hmm,no
they are *only* broken in the init data dlg
wtf
only in init data, and only in large mode....

=== @EmilyV99 (discord: Emily) 09/17/2021 02:11

. . .
and ONLY in ZQ
the same fucking dialog launched via the cheats menu in ZC
fucking works fine
WHAT THE SHIT

=== @EmilyV99 (discord: Emily) 09/17/2021 02:13

. . .I just have no clue
This does not make sense
whatsoever
the code is shared between ZC and ZQ
and the large_dialog code is shared by multiple dialogs
only this dialog, only in ZQ, is affected
this should *not be possible*
.....I have a fucking jank way to fix it, which I'm gonna do
(just remove the frames)

=== @ Saffith 09/17/2021 02:15

Have you tried rebuilding from scratch to rule out some sort of build error?

=== @EmilyV99 (discord: Emily) 09/17/2021 02:15

aye, multiple times
that's always the *first* thing I try

=== @ Saffith 09/17/2021 02:16

Welp, that's the only logical explanation I had.

=== @EmilyV99 (discord: Emily) 09/17/2021 02:16

I would say cosmic rays
but uh
that would need to be occurring every single time
which uh, not likely
there is no logical explaination for this, it is the new boogie-man
...time to jank around it.
(Replacing the init data dialog with a new gui system thing at some point would be wonderful)
(though, needs a lot of stuff)

=== @ Saffith 09/17/2021 02:18

Well, good excuse to do it.

=== @EmilyV99 (discord: Emily) 09/17/2021 02:22


![image](https://cdn.discordapp.com/attachments/888230580855136327/888248468152414208/unknown.png)
looks a bit odd with the frames missing
but, for now, it will do
that gui will be a mountain of a project to rewrite, considering it's >3k indexes
but, a lot of that is generated in a loop
for the LItem stuff
....could probably do that in some saner way

=== @EmilyV99 (discord: Emily) 09/17/2021 02:27

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594) fix posted

=== @EmilyV99 (discord: Emily) 09/17/2021 02:28

(meta) thread name was changed: ✅🔒Init Data Broken
## More Itemclasses (#885)
@ Guinevere opened this issue on 09/17/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/888296011766845460



=== @ Guinevere 09/17/2021 05:31

To pick up from the default module discussion
there are some items that were scripted into the previous default module that i think would be pretty nice to have being built-in itemclasses;
Compass (Magic)
Key (Boss, Magic)
Map (Magic)
Scroll: Half Magic
Scroll: Learn Slash
## ❌🔒New Default Module Messes with Quests Sfx (#886)
@ Guinevere opened this issue on 09/17/2021

Status: wont-fix

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888307587215405106



=== @ Guinevere 09/17/2021 06:17

the quests that were using the sounds default of the previous default module have been changed with the sounds of the new module

=== @ NightmareJames 09/17/2021 12:38

Don't know if this is a bug,but deserves a mention.  Second

=== @EmilyV99 (discord: Emily) 09/17/2021 14:29

???????

=== @ Guinevere 09/17/2021 19:09

Since the new module changes the default sound effects, quests that used the previous default sound effects are now using the new ones.

=== @ Guinevere 09/17/2021 19:11

So in laments terms
Zelda 1 sounds got turned into Koten sounds

=== @EmilyV99 (discord: Emily) 09/17/2021 19:12

sfx should be stored in the quest file
this points to a serious underlying problem

=== @ NightmareJames 09/17/2021 20:15

Good thing we reported it then

=== @ Guinevere 09/17/2021 20:15

indeed
people can sorta fix it by going back to the previous module but it's still pretty weird that the sfx aren't tied to the quests

=== @EmilyV99 (discord: Emily) 09/17/2021 20:22

The problem I see here is this may not be fully fixable, depending on the exact nature of the problem
because to fix it may *require* a quest be re-saved
unless it stores the appropriate sfx, and is just *ignoring* them for the module, which is possible; I haven't looked into it yet

=== @ NightmareJames 09/17/2021 20:24

Hey @EmilyV99 (discord: EmilyV) , can we get together in the server's voice chat for a minute?  General1?

=== @EmilyV99 (discord: Emily) 09/17/2021 20:25

give me a few, just got done with a super difficult run of a game that I've been doing for *hours*

=== @ NightmareJames 09/17/2021 20:25

OK

=== @EmilyV99 (discord: Emily) 09/17/2021 20:43

. . .
so no one is gonna like this
but it's literally not fixable
the SFX for the ones from sfx.dat are literally not being saved in the qst file
so old quests literally don't have anything in them in those slots
meaning either we need to include the copyrighted sfx in the default package *forever*
or break sfx in old quests
both of which are "unacceptable" outcomes
catch-22 situation, nothing we can do
....I can fix this for quests that are *re-saved in a new build*
but can't do anything more

=== @ Guinevere 09/17/2021 20:46

mmm
that is pretty problematic

=== @EmilyV99 (discord: Emily) 09/17/2021 20:47

gonna have to discuss with devs on course of action here
because either we break old quests
or we postpone being copyright-free until the rewrite

=== @ Guinevere 09/17/2021 20:53

i mean
i know my two-sense isn't the strongest in terms of development discussions like this
but i think it would be much less of a headache if you postpone until the rewrite, since one of the main focuses of 2.55 is backwards compatibility with all the quests that were made in the previous versions
it keeps priorities of what you want to do with both 2.55 and the rewrite intact

=== @ NightmareJames 09/17/2021 21:13

https://youtu.be/WGWweXnW__w This is the bug in action (including a custom SFX in action)

=== @ vlamart 09/17/2021 22:27

If I work on a sfx library, should I follow the "tracklisting" in the constants doc?

=== @EmilyV99 (discord: Emily) 09/17/2021 22:28

what listing?
The `SFX_` constants?

=== @ vlamart 09/17/2021 22:29

Yup

=== @EmilyV99 (discord: Emily) 09/17/2021 22:29

probably
scripts may potentially expect them to be as-is
and most questmakers keep their sfx in the same order as default for ease of use

=== @EmilyV99 (discord: Emily) 09/17/2021 22:48

Marking this `cannot be fixed`, see [#announcements](https://discord.com/channels/876899628556091432/876904615403196467)
(meta) thread name was changed: ❌🔒New Default Module Messes with Quests Sfx
## ❌🔒New Quest Template Does Not Make Water Solid (#887)
@ Moosh opened this issue on 09/17/2021

Status: wont-fix

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888554597122207775



=== @ Moosh 09/17/2021 22:38

May just be a bug with the Koten file included, when I hit Authentic NES when making a new quest, the water is not solid as it should be.

=== @ Moosh 09/17/2021 22:41

Trying the same in 2.53 implies it may be an issue with the template dialog though. Also solidity preview in 2.53 shows a teal color for walkable water with the rule off, yet the latest nigtly has it unmarked

=== @EmilyV99 (discord: Emily) 09/17/2021 22:43

Water has never been *made solid* by rulesets
it is made *non-solid* by the more modern rulesets
but nothing has *ever* made it solid

=== @ Moosh 09/17/2021 22:43

Sorry the correct wording is it is not _left_ solid by the template dialog 🤦

=== @EmilyV99 (discord: Emily) 09/17/2021 22:43

oh
tis quite different

=== @ Moosh 09/17/2021 22:44

So either it was never solid to begin or the template code that makes it walkable runs every time

=== @EmilyV99 (discord: Emily) 09/17/2021 22:44

would guess never solid to begin with
because that code only exists in the blocks for the newer rulesets
and all instances of that code would pop up asking you for confirmation of converting the water
so if you get no pop-up asking `"Convert all water to non-solid?"` then it isn't doing anything

=== @ Moosh 09/17/2021 22:45

No pop-up

=== @EmilyV99 (discord: Emily) 09/17/2021 22:45

then aye, it just isn't solid in that tileset

=== @ Moosh 09/17/2021 22:45

But hitting no on the popup still leaves it walkable
Odd that it's that way in both the 2.55 and 2.53 defaults

=== @EmilyV99 (discord: Emily) 09/17/2021 22:46

Fun thing is it never used to have a popup even though it always has done that conversion, as far back as 2.50.2

=== @ Moosh 09/17/2021 22:46

Anyways, I'm meaning to comb over all ZQuest dialogues I can and report any oddities I find

=== @EmilyV99 (discord: Emily) 09/17/2021 22:48

Regardless, any issues with that tileset won't matter long
given [#announcements](https://discord.com/channels/876899628556091432/876904615403196467)
anyway, marking this `not a bug`
(meta) thread name was changed: ❌🔒New Quest Template Does Not Make Water Solid
## ✅🔒Small GUI Bugs (#888)
@ Moosh opened this issue on 09/18/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888594488493232148



=== @ Moosh 09/18/2021 01:17

Finished looking over ZQuest, only a couple things in the GUIs stood out as out of place:
```-Pickup flags in the item editor still has that big honkin' checkbox next to it
-SFX menu flickers when pressing the play button sometimes
-Background bezel on the side warp menu is mis-sized```
Here's what side warp triggers look like now
![image](https://cdn.discordapp.com/attachments/888594488493232148/888594608840376340/unknown.png)
vs how it used to be
![image](https://cdn.discordapp.com/attachments/888594488493232148/888594679678001152/unknown.png)
I imagine this is the same thing that happened with the rectangles in init data

=== @ Moosh 09/18/2021 01:19

here's a snap of the play button flicker in action. Harmless but a little off. I'm really reaching to find anything in the editor that's immediately obviously broken, which is good
![image](https://cdn.discordapp.com/attachments/888594488493232148/888595058893389824/unknown.png)

=== @ vlamart 09/18/2021 02:00

(replying to @ Moosh "Here's what side warp trigger…"): Similar bug in CSets

=== @EmilyV99 (discord: Emily) 09/18/2021 02:01

(replying to @ Moosh "Here's what side warp trigger…"): ok, so this happens in exactly 2 places
and has no explaination
fun
@ Saffith should probably be in this thread

=== @ Saffith 09/18/2021 02:02

... That is very random and weird.

=== @ Moosh 09/18/2021 02:03

Oh! It is in the CSets menu as well. Thanks for catching vlamart

![image](https://cdn.discordapp.com/attachments/888594488493232148/888606115821146183/unknown.png)

=== @EmilyV99 (discord: Emily) 09/18/2021 02:04

ok, 3 places
but it wasn't occurring in every place
and it also wasn't occurring in ZC's menus

=== @EmilyV99 (discord: Emily) 09/18/2021 02:06

like, check the control binding menus

=== @ Saffith 09/18/2021 02:09

Also View -> View Palette

=== @EmilyV99 (discord: Emily) 09/18/2021 02:11


![image](https://cdn.discordapp.com/attachments/888594488493232148/888608131662360576/unknown.png)
see how this menu isn't fucked up
makes me so confused

=== @ Saffith 09/18/2021 03:27

I think it's affecting every `jwin_frame_proc` in ZQuest, and some are just more obvious than others.
Windows
![image](https://cdn.discordapp.com/attachments/888594488493232148/888627280883109928/Windows.png)
Linux
![image](https://cdn.discordapp.com/attachments/888594488493232148/888627302731218964/Linux.png)

=== @EmilyV99 (discord: Emily) 09/18/2021 03:27

oh, it's also affecting the textbox there
huh

=== @ Saffith 09/18/2021 03:28

That's not a textbox. It's just a frame with text inside.

=== @EmilyV99 (discord: Emily) 09/18/2021 03:28

the `Music.nsf` box?

=== @ Saffith 09/18/2021 03:28

Yep.

=== @EmilyV99 (discord: Emily) 09/18/2021 03:28

huh
that makes sense then
but I know I opened some places that use frame and didn't see it

=== @ Saffith 09/18/2021 03:30

Are you sure it was in ZQuest? ZC seems to be unaffected.

=== @EmilyV99 (discord: Emily) 09/18/2021 03:33

I could swear at least 2 spots in zq had no issue
but could have just been non-noticable
so, it's only in ZQ, and only in large mode
that points to `zq_custom.cpp` `large_dialog()`

=== @ Saffith 09/18/2021 03:36

Hm... The secret combos dialog looks weirdly okay.
Nothing's off by even a pixel.
`large_dialog(secret_dlg,1.75);`
... Is 1.75 okay, but 1.5 isn't?

=== @EmilyV99 (discord: Emily) 09/18/2021 03:38

hmm, that's odd

=== @ Saffith 09/18/2021 23:54

Okay, seriously, WTF.
I found the problem.
```
if (jwin_frame_proc == d_comboframe_proc)
        std::cout << "Yep, they're the same" << std::endl;
```

=== @EmilyV99 (discord: Emily) 09/18/2021 23:55

wh-what

=== @ Saffith 09/18/2021 23:55

The functions are identical, so I guess it just combined them...
Not sure why that's allowed.

=== @EmilyV99 (discord: Emily) 09/18/2021 23:55

C++ what the shit is this
```cpp
// Identical to jwin_frame_proc, but is treated differently by large_dialog()
int d_comboframe_proc(int msg, DIALOG *d, int c)```
fucking
wtf

=== @ Saffith 09/18/2021 23:57

https://docs.microsoft.com/en-us/archive/msdn-magazine/2015/february/compilers-what-every-programmer-should-know-about-compiler-optimizations
Also, by specifying the /OPT:ICF switch, the linker will fold identical functions and global constant variables.
So I guess that's enabled somehow.

=== @ Saffith 09/19/2021 00:01

Project > Properties, Configuration Properties > Linker > Optimization, set "Enable COMDAT Folding" to false, and it's fixed.

=== @EmilyV99 (discord: Emily) 09/19/2021 00:01

now time to figure out how to do that in cmake

=== @EmilyV99 (discord: Emily) 09/19/2021 00:03

need to set `/OPT:NOICF` switch

=== @EmilyV99 (discord: Emily) 09/19/2021 00:08


![image](https://cdn.discordapp.com/attachments/888594488493232148/888939464922107914/unknown.png)
success

=== @ Saffith 09/19/2021 00:09

Excellent.
So there are breaking optimizations enabled automatically, huh...
Not any more of those, hopefully.

=== @EmilyV99 (discord: Emily) 09/19/2021 00:11


![image](https://cdn.discordapp.com/attachments/888594488493232148/888940234220400690/unknown.png)
woo

=== @EmilyV99 (discord: Emily) 09/19/2021 00:16

(replying to @ Moosh "here's a snap of the play but…"): this only seems to occur if you click the button really fast?
Methinks allegro issue
processing the mouse click before the first `draw` command of the dialog

=== @EmilyV99 (discord: Emily) 09/19/2021 00:19

(keep in mind most buttons that do special code are actually closing the entire dialog, and then re-opening it almost instantly)

=== @EmilyV99 (discord: Emily) 09/19/2021 00:21

. . . and I had one idea for something that might fix it, which promptly failed

=== @EmilyV99 (discord: Emily) 09/19/2021 00:24

gonna call that one `acceptable graphical issue`, considering it seems you really need to spam click to make it happen

=== @EmilyV99 (discord: Emily) 09/19/2021 00:33

and finally

![image](https://cdn.discordapp.com/attachments/888594488493232148/888945778771496961/unknown.png)
no more honkin' checkbox
or any of the other crap there that should have been removed when @arceusplayer11 (discord: Deedee) added the `Pickup Flags` tab
....should probably shift the `String:` stuff left....

=== @EmilyV99 (discord: Emily) 09/19/2021 00:36

god fucking dammit
I keep pressing `F7` expecting it to build
but in MSVC2019 the shortcut is `Ctrl+Shift+B` instead..... 🤢

=== @EmilyV99 (discord: Emily) 09/19/2021 00:38

ah, thank god that's rebindable

=== @EmilyV99 (discord: Emily) 09/19/2021 00:40


![image](https://cdn.discordapp.com/attachments/888594488493232148/888947566841045012/unknown.png)
becomes

![image](https://cdn.discordapp.com/attachments/888594488493232148/888947587959369738/unknown.png)
...plenty of space in the lower-right if we need to add more stuff.
@ Moosh this all seem good?

=== @ Moosh 09/19/2021 00:41

beautiful

=== @EmilyV99 (discord: Emily) 09/19/2021 00:47

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
marking `fixed`
(meta) thread name was changed: ✅🔒Small GUI Bugs
## ✅🔒Dins Fire Lags ZC 2.55 (#889)
@ Guinevere opened this issue on 09/18/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888637215637385226



=== @ Guinevere 09/18/2021 04:07

when the flames are released from Din's Fire, ZC lags. even at the default 32 flames

=== @ Guinevere 09/18/2021 04:08

this doesn't occur in the previous builds that doesn't use C++17

=== @EmilyV99 (discord: Emily) 09/18/2021 04:10

@ Saffith

=== @ Saffith 09/18/2021 04:13

This one's happening on Linux, too. I'll see if I can find anything.

=== @EmilyV99 (discord: Emily) 09/18/2021 04:16

It could be something to do with the massive memory allocation/deallocation being slower for some reason
keep in mind that it generates and destroys 32 lweapons per frame
which all have a *full script stack* attached
.....should probably make it so the script stack only allocates the memory if it is going to be used.
.........for all sprite types......
which sounds like a fun adventure
might not be the only issue, though; could be something else at play

=== @ Guinevere 09/18/2021 04:19

(replying to @EmilyV99 (discord: Emily) "keep in mind that it generate…"): that's a funny way to do it

=== @ Guinevere 09/18/2021 04:20

i thought it just moves the the lweapons just moved away from link until they hit the radius
<:derp:675738486397206578>

=== @ Guinevere 09/18/2021 04:22

until i saw how slow it ran and you could see them replace themselves in slow motion

=== @EmilyV99 (discord: Emily) 09/18/2021 04:22

Nope, it generates new ones each frame; that's why they appear to not die on hitting enemies

=== @ Guinevere 09/18/2021 04:22

i see
that's one way to do it
if that's the case how do things like piercing arrows and beams work?
do they work the same way?
or candle flames for that matter

=== @EmilyV99 (discord: Emily) 09/18/2021 04:27

Those won't pierce an enemy with "Block" defense
Din's, pretty sure would
Given moving the flames and having a hardcoded pierce anything value would be far more sane
But ZC jankify

=== @ Guinevere 09/18/2021 04:28

uh huh
learning so much today
<a:ablobpopcorn:722876973449478363>

=== @ Saffith 09/18/2021 04:29

Geez.
Callgrind drops from ~13.5 FPS to <0.5.

=== @EmilyV99 (discord: Emily) 09/18/2021 04:29

Fun

=== @ Saffith 09/18/2021 04:30

The full animation is like five minutes.

=== @ Guinevere 09/18/2021 04:30

ouch

=== @EmilyV99 (discord: Emily) 09/18/2021 04:32

2 things to definitely help this:
- compat QR for old behavior, make new behavior where it moves the flames instead of creating new ones; needs new pierce behavior
- Make memory for script info only be allocated when it is first needed, not on sprite creation. This way unscripted sprites don't need to alloc/dealloc those. A simple `sprite::allocscript()` function to allocate the memory if and only if the pointers are null, and deallocating appropriately in the destructor, would fix this. This should lower lag of all sprite types significantly, including fixing particle effects.
Those are both just general optimizations though
not sure if there's a specific issue with C++17 that should also be corrected here

=== @EmilyV99 (discord: Emily) 09/18/2021 04:34

Adding a general weapon piercing property, which could be script-readwrite, would be useful for the former; `*weapon->Pierce`. Would be `int`, with `0 = no pierce`, `1 = standard pierce`, `2 = pierce even block defense enemies`; 2 being what dins effectively does now

=== @ Saffith 09/18/2021 04:36

Looks like it's spending the bulk of its time in `sprite::draw()`.

=== @EmilyV99 (discord: Emily) 09/18/2021 04:36

Oh?
That seems fun
And not what either of my optimizations would target
Does it occur with the compat QR `Old (Faster) sprite draws` enabled?

=== @ Saffith 09/18/2021 04:39

Haven't checked that, but I'm betting it does...
Looks like it's mainly `dithercircfill`, called from `doDarkroomCircle`.
`ditherblit`, in particular.
And that's mainly `getpixel`.

=== @EmilyV99 (discord: Emily) 09/18/2021 04:41

Oh fun
Darkroom functions don't have a check to only run in darkrooms
That'd do it
And fire weapons have light radius by default
That's my bad

=== @ Guinevere 09/18/2021 04:42

oopsie doodle

=== @EmilyV99 (discord: Emily) 09/18/2021 04:43

And was not in the last build before the C++17 stuff
So that explains the issue
3 fixes, I'll handle them all
... when I wake. G'nite all!

=== @ Guinevere 09/18/2021 04:44

gnite
<:patcat:677072862036885504>

=== @ Saffith 09/18/2021 04:44

Yeah, it's a bit late for all that.

=== @ Saffith 09/18/2021 04:48

In a quick test of just picking up Din's Fire and using it twice, `getpixel` accounted for ~35% of the program's total run time.

=== @EmilyV99 (discord: Emily) 09/18/2021 04:49

That's used in the dithering functions

=== @ Saffith 09/18/2021 04:49

Yeah. If there's any way you can cut down on it..

=== @EmilyV99 (discord: Emily) 09/18/2021 04:50

Not really... unless you want to look at optimizing the `drawing.cpp` stuff while having the same visual effect
But, making it only run when it actually is in a dark room will help a lot

=== @ Saffith 09/18/2021 05:17

I see almost no framerate hit by doing this:
```cpp
#include <allegro/internal/aintern.h>
void ditherblit(BITMAP* dest, BITMAP* src, int color, byte dType, byte dArg, int xoffs, int yoffs)
{
    int wid = zc_min(dest->w, src->w);
    int hei = zc_min(dest->h, src->h);
    for(int ty = 0; ty < hei; ++ty)
    {
        uintptr_t addr = bmp_read_line(src, ty);
        for(int tx = 0; tx < wid; ++tx)
        {
            if(bmp_read8(addr+tx) && dithercheck(dType,dArg,tx+xoffs,ty+yoffs,wid,hei))
            {
                putpixel(dest, tx, ty, color);
            }
        }
        bmp_unwrite_line(src);
    }
}
```

=== @EmilyV99 (discord: Emily) 09/18/2021 05:18

I don't recognize any of those functions
But if it works smoother, then yes please
Does it respect the clipping rect of the dest?
Wait that's all on the src
So duh the dest code didn't change

=== @EmilyV99 (discord: Emily) 09/18/2021 14:33

K
\#3 - saff's fix- is implemented, and works beautifully
also simultaneously made it so none of that shit runs if the screen isn't dark
or new darkrooms aren't enabled

=== @EmilyV99 (discord: Emily) 09/18/2021 14:47

Using `->Explode(2)`, running it a bunch of times per frame, I can cause this:
![image](https://cdn.discordapp.com/attachments/888637215637385226/888798434772025424/unknown.png)
which, is a solid FREEZE on trying to scroll screens, due to massive memory dealloc
optimization 2 should target this type of lag directly, so time to test that

=== @EmilyV99 (discord: Emily) 09/18/2021 16:07

...well, it doesn't do as much as expected for this particular usecase
and took far more work than expected
but it should in theory be working now
....particles really still need to become a separate class, and not `: public sprite`

=== @EmilyV99 (discord: Emily) 09/18/2021 16:13

. . . wait wtf
So, on optimization `1.` .... I appear to be wrong?
It appears to only generated the flames once, not each frame
. . . I could have sworn I ran into an issue with it generating each frame before . . .

=== @EmilyV99 (discord: Emily) 09/18/2021 16:19

@here

https://cdn.discordapp.com/attachments/888637215637385226/888821557705736273/zelda.exe

https://cdn.discordapp.com/attachments/888637215637385226/888821582384996382/zquest.exe
should fix your issues

=== @ P-Tux7 09/18/2021 16:21

ooh better din's fire now?
better as in can be blocked and doesn't spawn every frame

=== @EmilyV99 (discord: Emily) 09/18/2021 16:22

1. Dark rooms no longer run their drawing code when you aren't in a dark room
2. Dithered drawing is now just faster fps-wise, thanks to Saff's code
3. Sprites no longer generate script data if they aren't using it
Apparently it didn't spawn every frame? And I'm very confused by this?
Or if it is, I don't see any possible way the code that spawns it could be doing that, so

=== @ P-Tux7 09/18/2021 16:22

something i'd appreciate is a way to spawn the ring of fire routine without the actual item

=== @EmilyV99 (discord: Emily) 09/18/2021 16:23

?

=== @ P-Tux7 09/18/2021 16:23

i.e. for a book fire effect, or an enemy making a ring of fire
some way to spawn it with a radius argument

=== @EmilyV99 (discord: Emily) 09/18/2021 16:23

blehg
far too much work

=== @ P-Tux7 09/18/2021 16:23

no sorry i meant
SCRIPT ONLY

=== @EmilyV99 (discord: Emily) 09/18/2021 16:24

so a script being able to just spawn a ring of fire?
That's a ridiculously easy thing to do in zscript
```cpp
for(int flamecounter=((-1)*(flamemax/2))+1; flamecounter<=((flamemax/2)+1); flamecounter++)
{
    Lwpns.add(new weapon((zfix)LinkX(),(zfix)LinkY(),(zfix)LinkZ(),wFire,itemsbuf[magicitem].fam_type,itemsbuf[magicitem].power*game->get_hero_dmgmult(),
                         isSideViewGravity() ? (flamecounter<flamemax ? left : right) : 0, magicitem, Link.getUID(), false, 0, 0, 0, itemsbuf[magicitem].family));
    weapon *w = (weapon*)(Lwpns.spr(Lwpns.Count()-1));
    w->step=(itemsbuf[magicitem].misc2/100.0);
    w->angular=true;
    w->angle=(flamecounter*PI/(flamemax/2.0));
}
```
that's the internal code
converting it to ZScript should be relatively easy
the `Lwpns.add` is just a `CreateLWeapon` that sets a bunch of the variables
and the actual ring is done by the `->angular`/`->angle` calcs
so like

=== @EmilyV99 (discord: Emily) 09/18/2021 16:28

```cpp
void spawnFireRing(int x, int y, int dmg, int stp, int numflames)
{
    for(int flamecounter=((-1)*(numflames/2))+1; flamecounter<=((numflames/2)+1); flamecounter++)
    {
        lweapon weap = Screen->CreateLWeapon(LW_FIRE);
        weap->X = x;
        weap->Y = y;
        weap->Damage = dmg;
        weap->Step = stp;
        weap->Angular = true;
        weap->Angle = ((flamecounter*PI)/(numflames/2));
    }
}```
there you go

=== @ P-Tux7 09/18/2021 16:28

thank you!

=== @EmilyV99 (discord: Emily) 09/18/2021 16:28

that doesn't set some of the vars the internal one does, like the parent item
but you wouldn't want those
oh wait, let me make an ew version

=== @EmilyV99 (discord: Emily) 09/18/2021 16:29

```cpp
void spawnLWRing(int x, int y, int dmg, int stp, int numweaps, int type)
{
    for(int count=((-1)*(numweaps/2))+1; count<=((numweaps/2)+1); count++)
    {
        lweapon weap = Screen->CreateLWeapon(type);
        weap->X = x;
        weap->Y = y;
        weap->Damage = dmg;
        weap->Step = stp;
        weap->Angular = true;
        weap->Angle = ((count*PI)/(numweaps/2));
    }
}
void spawnEWRing(int x, int y, int dmg, int stp, int numweaps, int type)
{
    for(int count=((-1)*(numweaps/2))+1; count<=((numweaps/2)+1); count++)
    {
        eweapon weap = Screen->CreateEWeapon(type);
        weap->X = x;
        weap->Y = y;
        weap->Damage = dmg;
        weap->Step = stp;
        weap->Angular = true;
        weap->Angle = ((count*PI)/(numweaps/2));
    }
}```
woo there you go, LW and EW version, and I made it take any weapon type

=== @ P-Tux7 09/18/2021 16:30

how does the fire know when to stop moving

=== @EmilyV99 (discord: Emily) 09/18/2021 16:30

err, it doesn't
stop moving
or if it does, that's hardcoded to fire weapons

=== @ P-Tux7 09/18/2021 16:31

oh well that's fine
i'll test it out with fire and see if it does

=== @ P-Tux7 09/18/2021 16:32

~~time for me to mod it as an npc death effect~~

=== @EmilyV99 (discord: Emily) 09/18/2021 16:34

you could also add a `script`/`InitD` param
to assign a script and init values to each weapon
which could be used for stopping them moving after a certain time
or doing any number of other effects
as it's a ZScript function, the number of ways you could simply modify it is endless

=== @EmilyV99 (discord: Emily) 09/19/2021 00:48

(meta) thread name was changed: ✅🔒Dins Fire Lags ZC 2.55
## ❌More fonts for Zquests string editor (#890)
@ FireSeraphim opened this issue on 09/18/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/888833859049906187



=== @ FireSeraphim 09/18/2021 17:08

I would formally like to ask about adding more fonts to the string editor and I personally happen to have a huge collection of fonts from various games, including Castlevania 3 - Dracula's Curse, Chrono Trigger and a few others. Here's the DL File for my personal font collection: https://drive.google.com/file/d/1VQ0wm05uV8EQVqXrzeklGwviaUHQUZSF/view?usp=sharing
@<role: Developer> Heads up!

=== @ P-Tux7 09/18/2021 17:09

reminder that all fonts must be reduced to one colour

=== @EmilyV99 (discord: Emily) 09/18/2021 17:09

don't need to ping all the devs

=== @ P-Tux7 09/18/2021 17:09

(for lttp, zc outlines the text using code in a string setting)

=== @ FireSeraphim 09/18/2021 17:10

aye, my apologies.

=== @ FireSeraphim 10/04/2021 22:48

@ZoriaRPG (discord: Timelord) I vaguely recall you showing off screenshots of a build that had more fonts and I'm pinging you because I still kinda want the actual Castlevania 3 font in ZC
Please reply to this thread when you can.

=== @ P-Tux7 10/05/2021 00:20

oh yeah where's the allegro font tool
nvm i'm dumb

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:05

@ FireSeraphimIwasgoingto add a `userfonts.dat`with twenty slots into which anyone could make a file and use those fonts via a module

=== @ FireSeraphim 10/05/2021 07:06

mind if I paged @EmilyV99 (discord: EmilyV)?

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:06

I suppose that once 
I install vc2019 I coud add that. It is not that difficult
(replying to @ FireSeraphim "mind if I paged <@!2424224362…"): I do not  mind,but even if I did it isn't my server so as  long as it is permitted do as you wish.

=== @ FireSeraphim 10/05/2021 07:07

aye

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:07

It's about one total day of work to add this feature.

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:09

I may just bake it into fonts.dat as ten user fonts and be done

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:10

I do however think that a custom userfonts is best with a command to load it n ZScript so that you can hot swap fonts adhoc.
this would allow a lot of freedom but it needs a lot  of GUI shyte in ZQE to support it

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:14

as it is not up to me now I do not have say on if this is going to be included if I make it and I want assurance that it will, ere I waste time creating it
I short I will not even begin on such a task unless the concept is preapproved.

=== @EmilyV99 (discord: Emily) 10/05/2021 07:14

The question I have is, how much would it add to embed a few custom fonts in the .qst?
like how SFX are loaded?

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:15

how much what?

=== @EmilyV99 (discord: Emily) 10/05/2021 07:15

would that add too much bloat to the quest file?
if not, I feel like that would be a far better system

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:15

Fonts are bitmap images
you'd store tem externally
but if you do tat tewn ZQ cannot preview te messages

=== @EmilyV99 (discord: Emily) 10/05/2021 07:16

Why couldn't they be stored internally though?

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:16

hence why I thought that a ten font userfonts.dat was the best solution

=== @EmilyV99 (discord: Emily) 10/05/2021 07:16

just write the contents of the bitmap to the quest file, `pfwrite()`

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:16

I suppose they could
but that has the same problem
https://www.allegro.cc/manual/4/api/fonts/load_font
if you have a better idea there is the documentaton

=== @EmilyV99 (discord: Emily) 10/05/2021 07:17

I mean, it can `write_bitmap()` to a tempfile and then load the tempfile
if the load_font requires it be a file

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:17

that only supports GRX
IDK if the fonted output would wor

=== @EmilyV99 (discord: Emily) 10/05/2021 07:18

`or any bitmap format that can be loaded by load_bitmap()`
if you read the full sentence

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:18

and again, there is the string editor and te subscreen to cnsider

=== @EmilyV99 (discord: Emily) 10/05/2021 07:18

`a GRX format .fnt file, a 8x8 or 8x16 BIOS format .fnt file, a datafile or any bitmap format that can be loaded by load_bitmap().`
For string editor/subscreen, the user fonts would just be appended to the dropdown lists

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:18

Sure
I do not ind this
but it reuires team effort
not e alone sitting and doing it

=== @EmilyV99 (discord: Emily) 10/05/2021 07:19

aye, certainly

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:19

and the complications of working with an eternal repo pus the new vs version mean it won't happen fast
coding this is not that hard
for the basic font loading
I'd do it in ZScript first
then you can add the other crud
incuding the file sel dialogue to add a font
it will need a somewhat complex dialogue including storing a font name and a pulldown for the slot (1 to 10)
and will further deprecate Tango to a point

=== @EmilyV99 (discord: Emily) 10/05/2021 07:22

well, it'd be kinda like the `SFX` dialog

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:22

so that is a bonus

=== @EmilyV99 (discord: Emily) 10/05/2021 07:22

you select a slot to edit, then name it and load a file

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:22

sure
I just want a team effort to add that jank

=== @EmilyV99 (discord: Emily) 10/05/2021 07:22

should be fairly simple, though I'll want to build it in the new system, so won't just be pure copy+paste on the sfx one

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:23

Adding a major feature like this is not something I a wiling to do solo
I am more than happy to do the skeleton implementation at some point and let you do all of the GUI crud

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:25

I still need to do the basic ffscript stuff fr rgbdata and palette
so I need to reserve registers and ASM opcodes for my use
first
twenty to thirty
I don't want to resolve erge conflicts on an external repo and futz about

=== @ZoriaRPG (discord: Timelord) 10/05/2021 07:27

in general when anything artificially pads a task to increase the amount of required time I just say no.
so reserving these allows me to avoid merge conficts
and thus not waste time

=== @ P-Tux7 10/05/2021 15:24

(replying to @EmilyV99 (discord: Emily) "would that add too much bloat…"): i can't imagine so
allegro fonts are 1-bit images
i'm sure one page of 8-bit tiles would take the same amount of room as 10 or even 20 allegro fonts

=== @ P-Tux7 10/05/2021 15:26

and it should add almost zero bloat if the user does not ADD any, just like sfx and 8-bit tiles

=== @EmilyV99 (discord: Emily) 10/05/2021 15:27

aye, fair

=== @ FireSeraphim 07/22/2022 09:45

Bump

=== @EmilyV99 (discord: Emily) 07/22/2022 09:47

(meta) thread name was changed: ❌More fonts for Zquests string editor
## ✅🔒variable `Animation` doesnt exist in itemsprite script (#891)
@ Lincolnpepper opened this issue on 09/18/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/888897583047671838



=== @ Lincolnpepper 09/18/2021 21:21

Zscript Additions.txt includes a variable `Animation` that is a member of sprite objects, including itemsprite. but i get an error for `Animation` not existing under pointer when i use `this->Animation` in a itemsprite script.

=== @EmilyV99 (discord: Emily) 09/19/2021 22:38

(meta) thread name was changed: 🔓variable `Animation` doesnt exist in itemsprite script

=== @EmilyV99 (discord: Emily) 09/20/2021 20:29

@ Lincolnpepper this work?

https://cdn.discordapp.com/attachments/888897583047671838/889609320688402493/zelda.exe

https://cdn.discordapp.com/attachments/888897583047671838/889609328447848458/zquest.exe

=== @ Lincolnpepper 09/20/2021 20:41

(replying to @EmilyV99 (discord: Emily) "@ Lincolnpepper this w…"): it compiles, but it doesn't seem to work. 
```
itemsprite script Test
{
    void run()
    {
        this->Animation = false;
    }
}
```
i put this itemsprite script on a rupee and it didn't stop the rupee's animation

=== @EmilyV99 (discord: Emily) 09/20/2021 20:41

ahk, damn. Was hoping only the script side was missing.....

=== @EmilyV99 (discord: Emily) 09/20/2021 20:44

try this

https://cdn.discordapp.com/attachments/888897583047671838/889613017237565510/zelda.exe

=== @EmilyV99 (discord: Emily) 09/20/2021 20:47

? @ Lincolnpepper

=== @ Lincolnpepper 09/20/2021 20:49

yep, it works

=== @EmilyV99 (discord: Emily) 09/20/2021 20:49

wonderful
(meta) thread name was changed: ✅🔒variable `Animation` doesnt exist in itemsprite script
## ✅🔒`Grab-able` flag for items (#892)
@ Lincolnpepper opened this issue on 09/18/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/888899827734306907



=== @ Lincolnpepper 09/18/2021 21:30

The way that boomerang and hookshot grabbing items works in zc is not intuitive and is very limiting. It would make a lot of sense to just have a `Grab-able` flag for each item that determines if they can be grabbed by the boomerang and hookshot or something similar.

=== @EmilyV99 (discord: Emily) 09/19/2021 19:22

@ Lincolnpepper
Test if this works (new `IP_` constant, `IP_ALWAYSGRAB`, or pickup flags tab of item editor)

=== @EmilyV99 (discord: Emily) 09/19/2021 19:24


https://cdn.discordapp.com/attachments/888899827734306907/889230472067039263/2.55_NightlyBuild_Package.zip

=== @EmilyV99 (discord: Emily) 09/19/2021 20:33

(meta) thread name was changed: 💊🔓`Grab-able` flag for items

=== @ Lincolnpepper 09/19/2021 22:36

both setting the script constant and flags in the item editor seem to work
thank you!

=== @EmilyV99 (discord: Emily) 09/19/2021 22:37

(meta) thread name was changed: ✅🔒`Grab-able` flag for items
## Negative values on Lock Block Combo Counter Field as ScreenD (#893)
@ bigjoe opened this issue on 09/20/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/889365955032014878



=== @ bigjoe 09/20/2021 04:22

This would make lock blocks capable of changing and being dependant on ScreenD values. I can see a variety of possible uses here.

=== @ bigjoe 09/20/2021 04:27

If I could give examples. You might use strings to initiate the thought of getting a key from a bucket which could later be used on a lock block on the screen. Or you could have gathering mini games of sorts.

=== @ bigjoe 09/20/2021 08:07

Is this a viable idea? other combos have made use of Screen->D so I can see some use for it. Its by no means absolutely necessary, but would arm the user with "tricks up their sleeve"

=== @EmilyV99 (discord: Emily) 09/21/2021 00:08

The `Counter` value is an attribyte
meaning, it has a range of `0-255`, and literally can't hold a negative
## ✅🔒Writing to DMapData-ActiveSubscreen = Instant Update (#894)
@ Bagu opened this issue on 09/20/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/889554575089078323



=== @ Bagu 09/20/2021 16:52

I wrote a very simple function for RPG  quests, that can check the selected character and exchange the active subscreen, depending on it.

So I just thought it would be nice, if there was a Quest Script Option, that allows to instantly update the active subscreen Application (on every frame) if writing to "DMapData->ActiveSubscreen".
...without warping or scrolling to reinitiate the actual screen

=== @ Bagu 09/20/2021 16:54

Thank you.
I didn't know where I should post this

=== @ Bagu 09/20/2021 17:25

(meta) thread name was changed: Writing to DMapData-ActiveSubscreen = Instant Update

=== @EmilyV99 (discord: Emily) 09/20/2021 22:50

(meta) thread name was changed: 💊🔓Writing to DMapData-ActiveSubscreen = Instant Update

=== @EmilyV99 (discord: Emily) 09/20/2021 22:51

@ Bagu check if this works

=== @EmilyV99 (discord: Emily) 09/21/2021 00:07


https://cdn.discordapp.com/attachments/889554575089078323/889664171195662366/zelda.exe

https://cdn.discordapp.com/attachments/889554575089078323/889664185569538119/zquest.exe
works
(meta) thread name was changed: ✅🔒Writing to DMapData-ActiveSubscreen = Instant Update
## 💊🔓__AutoGhostParseName() Bugs (#895)
@ mitchfork opened this issue on 09/21/2021

Status: needs-testing

Labels: ['bug', 'needs-testing']

Source: https://discord.com/channels/876899628556091432/889915807159685202



=== @ mitchfork 09/21/2021 16:47

This is from a discussion in the Z-Zone scripting discussion channel with @ Lejes
In `__AutoGhostParseName()` there is a for loop to go through the NPC name string - there is a `return 1;` line that will always execute before the for loop finishes
this messes up AutoGhost in 2.55

=== @EmilyV99 (discord: Emily) 09/21/2021 17:02

....and it doesn't mess it up in 2.53?

=== @ mitchfork 09/21/2021 17:04

Haven't checked the file in 2.53
It looks like it would have the same bug
seems like to me that the `return 1;` should be inside an `else` but I'm not certain
line 351 btw

=== @EmilyV99 (discord: Emily) 09/21/2021 17:09

....wtf

=== @ mitchfork 09/21/2021 17:09

yeah, I use ghost heavily but don't use autoghost so I never encountered this

=== @EmilyV99 (discord: Emily) 09/21/2021 17:12

No, this occurred in an update of zoria's
where he royally fucked up without testing

=== @EmilyV99 (discord: Emily) 09/21/2021 17:16


https://cdn.discordapp.com/attachments/889915807159685202/889923012940427274/ghost2_global.zh
should be fixed with that update

=== @EmilyV99 (discord: Emily) 09/21/2021 21:53

(meta) thread name was changed: 💊🔓__AutoGhostParseName() Bugs

=== @arceusplayer11 (discord: Deedee) 10/29/2021 05:17

Could someone test this? More bugs I can close, the better
## Change color of screen transition animations (#896)
@ aslion opened this issue on 09/21/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/889943522881454130



=== @ aslion 09/21/2021 18:37

Could we have a way to change the color of the screen wipe animations on tile warps and the start of a quest?

=== @ Guinevere 09/28/2021 01:27

porc must live in 4 colors
anymore is blasphemy
<:nekopog:835231816620965948>
## ✅🔒std_functions.zh - Off by 1 error in collision detecting functions (#897)
@ Alucard648 opened this issue on 09/21/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/889997141248991272



=== @ Alucard648 09/21/2021 22:10

In all Collision functions all hitboxes are extended 1 pixel rightwards and 1 pixel downwards. Here is the example from std_functions.zh.
```

// Returns true if there is a collision between Link's hitbox and the FFC's.
// This only checks hitboxes.
bool LinkCollision(ffc f) 
{
    int ax = Link->X + Link->HitXOffset;
    int ay = Link->Y + Link->HitYOffset;
    return RectCollision(f->X, f->Y, f->X+(f->TileWidth*16), f->Y+(f->TileHeight*16), ax, ay, ax+Link->HitWidth, ay+Link->HitHeight);
}```
Here Hero`s default hit box counts as 17 pixels long, not 16 and 9 pixels high, not 8. In case of 1x1 FFC, its hitbox treated by function as 17x17 pixels, not 16x16 as intended. And that imprecision is across all collision detection functions in std.zh

=== @EmilyV99 (discord: Emily) 09/26/2021 04:40

@ Alucard648 this good? Did I miss anything?
https://cdn.discordapp.com/attachments/889997141248991272/891544775608651776/std_functions.zh
(meta) thread name was changed: 💊🔓std_functions.zh - Off by 1 error in collision detecting functions

=== @EmilyV99 (discord: Emily) 09/26/2021 04:58


https://cdn.discordapp.com/attachments/889997141248991272/891549369948594176/std_constants.zh

https://cdn.discordapp.com/attachments/889997141248991272/891549370858766336/std_functions.zh
here, actually did a bit more updating for dir stuff

=== @ Alucard648 09/26/2021 07:47

👍

=== @EmilyV99 (discord: Emily) 09/26/2021 07:47

(meta) thread name was changed: ✅🔒std_functions.zh - Off by 1 error in collision detecting functions
## ✅🔒ZC Init Data Bug (#898)
@ Guinevere opened this issue on 09/22/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/890072230724239410



=== @ Guinevere 09/22/2021 03:09

If there is more than 2 items in an item class, the init data bugs out, off-centering the item checkbox and doesn't allow you to click it on.

![image](https://cdn.discordapp.com/attachments/890072230724239410/890072327243595878/Screenshot_2021-09-21_200446.png)

=== @ Guinevere 09/22/2021 03:11

(meta) thread name was changed: ZC Init Data Bug

=== @EmilyV99 (discord: Emily) 09/22/2021 03:11

@ Saffith whaaaaaaaaaaaa

=== @ Saffith 09/22/2021 03:13

... Huh. Yep, that's a weird one.

=== @ Saffith 09/22/2021 03:18

You can still reach them with keyboard navigation, at least, so they're not totally unusable.

=== @ Saffith 09/22/2021 03:19

And they're similarly broken in small mode this time...

=== @ P-Tux7 09/22/2021 21:30

@ Bagu

=== @ Bagu 09/22/2021 21:31

Sorry
...didn't notice that it's already been reported...
...so my thread can be  deleted/archieved

=== @EmilyV99 (discord: Emily) 09/22/2021 22:06

Found the issue, technically my fault
...but, more a fault of poor original design.

=== @EmilyV99 (discord: Emily) 09/22/2021 22:23


https://cdn.discordapp.com/attachments/890072230724239410/890362657289424916/zelda.exe

https://cdn.discordapp.com/attachments/890072230724239410/890362687102521374/zquest.exe
fixed
(meta) thread name was changed: ✅🔒ZC Init Data Bug
## ✅🔒Whistle tornado sound effect wont stop playing (#899)
@ SkyLizardGirl opened this issue on 09/22/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/890294018678861844



=== @ SkyLizardGirl 09/22/2021 17:50

Whistle tornado sound effect won't stop playing after one use in latest Alpha 2.55

=== @ SkyLizardGirl 09/22/2021 17:52

When tornado is off screen and finished and gone it's sound still plays, over and over again.

=== @EmilyV99 (discord: Emily) 09/28/2021 15:01

Try un-checking `Weapons Can Go Out of Bounds (Offscreen)` under `options->backwards compatability->2`

=== @EmilyV99 (discord: Emily) 09/29/2021 12:55

? @ SkyLizardGirl

=== @ SkyLizardGirl 09/29/2021 22:20

It is unchecked

=== @ SkyLizardGirl 09/29/2021 22:23

Try giving the Whistles tornado a sound effect and see what happens.

=== @arceusplayer11 (discord: Deedee) 10/09/2021 14:03

Should be fixed now
(meta) thread name was changed: 💊🔓Whistle tornado sound effect wont stop playing

=== @arceusplayer11 (discord: Deedee) 10/09/2021 14:15

gonna post a nightly in a bit

=== @arceusplayer11 (discord: Deedee) 10/11/2021 13:47

@ SkyLizardGirl please check if the latest stuff fixes it
if not, please send a test quest and a description of when it happens

=== @ SkyLizardGirl 10/11/2021 21:39

Ok I will check

=== @arceusplayer11 (discord: Deedee) 10/26/2021 16:04

@ SkyLizardGirl did you check?

=== @ SkyLizardGirl 10/27/2021 03:10

No I haven’t yet I took a long break from ZC I will check now
I gotta load up my laptop

=== @arceusplayer11 (discord: Deedee) 10/28/2021 00:52

SLG PM'd me, it's fixed
(meta) thread name was changed: ✅🔒Whistle tornado sound effect wont stop playing
## ✅🔒dmapdata int Type not returning the right value? (#900)
@ OmegaX opened this issue on 09/24/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/890770390606020638



=== @ OmegaX 09/24/2021 01:23

when I tried used dm->Type it returns 128 for a Dungeon Type dmap instead of 0. (found this out via the trace function.)

=== @EmilyV99 (discord: Emily) 09/24/2021 01:24

It returns the internal type data
you need to `&11b` it, IIRC
ex
```cpp
switch(dm->Type&11b)
{
    case DMAP_OVERWORLD:
        //blah blah
        break;
}```
....still have no clue WHY it's like that, should probably investigate further. Zoria's doing, I believe.

=== @EmilyV99 (discord: Emily) 09/26/2021 04:23

fixing this

=== @EmilyV99 (discord: Emily) 09/26/2021 04:27


https://cdn.discordapp.com/attachments/890770390606020638/891541419485954058/zelda.exe

https://cdn.discordapp.com/attachments/890770390606020638/891541438238715924/zquest.exe
@ OmegaX Does it work right in this?
(meta) thread name was changed: 💊🔓dmapdata int Type not returning the right value?

=== @ OmegaX 09/27/2021 13:54

windows is complaining about these files being viruses.

=== @EmilyV99 (discord: Emily) 09/27/2021 14:29

fun
windows hates zc

=== @ OmegaX 09/27/2021 16:11

Yeah, it also deletes the files when i try to open them. also, on an unrelated note: Trace is writing twice to allegro.log (ZScript Debug) instead of once. don't know why i need to do more testing...

=== @ OmegaX 09/27/2021 16:15

I have Trace run in a dmapdata script and it preform its function twice even though I have it written down once, one at the start before the warp opening starts and then another one after the warp animation is finish.

=== @arceusplayer11 (discord: Deedee) 01/15/2022 09:27

@EmilyV99 (discord: EmilyV) is this fixed?

=== @arceusplayer11 (discord: Deedee) 01/15/2022 09:28

@ OmegaX wait, I should be asking you
Sorry for the late ping, assuming you still use ZC

=== @ OmegaX 01/15/2022 09:29

Yep

=== @arceusplayer11 (discord: Deedee) 01/15/2022 09:30

This fixed it?

=== @ OmegaX 01/15/2022 09:33

I believe it was fixed in a official build after this, yes.

=== @arceusplayer11 (discord: Deedee) 01/15/2022 09:36

Aight, thank you!
(meta) thread name was changed: ✅🔒dmapdata int Type not returning the right value?
## ALTTP Sword (#901)
@ FireSeraphim opened this issue on 09/24/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/891105305306464326



=== @ FireSeraphim 09/24/2021 23:34

This just occurred to me and I think it would be great if this was an engine side feature but the default slash in Zeldaclassic is the GB Zelda 45 degree slash and it would be great as either a QR or sword exclusive item attribute to have 90 degree slashes ala ALTTP.

=== @EmilyV99 (discord: Emily) 09/24/2021 23:39

🤢 I don't want to think about the code required for this

=== @ FireSeraphim 09/24/2021 23:42

I see. My sincere apologies

=== @ P-Tux7 09/26/2021 01:41

iirc zoria planned to add this but we couldn't find the hitbox size for each frame even after asking on zeldix
i suppose i can ask on one of the randomizer discords nowadays
still it'd probably be hard since lttp had two different sword lengths that people would want
although as for scripting, isn't it much easier to do items now?

=== @EmilyV99 (discord: Emily) 09/29/2021 12:03

(meta) thread name was changed: ALTTP Sword

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:06

I did intend to add this and there is an lwpn for it ,  but as stated, I never found a complete definition for how it works in Z3

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:07

Thus, I left it on simmer.

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:09

If someone wants to fully document the code for how Z3 handles slashes and the sprites and timing, then K could do it with a 1:1 conversion. I  do not want to implement a shoddy or inaccurate emulation of it in ZC.

=== @ P-Tux7 10/24/2021 18:10

not to mention i don't quite like the sword or hammer in lttp
small hitboxes

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:11

What you like or dislike is not in debate. I happen to prefer both over zc, but I was more used to both ere either *existed* in zc.

=== @ P-Tux7 10/24/2021 18:13

btw something you *can* do is port the variable length property of Z3 swords to the current sword
since iirc hitboxes for them are extremely hardcoded rn and don't respect the input value in the item editor

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:17

I could, but I won't.
If I am going to do tqt I want to do it all at one time, or not at all.

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:20

Adding hotbox sizing to base swords is far from trivial
If I had all the metrics for z3 I would have done all of it for the z360 lwpn
Or z3slash
Or whatever I called it

=== @ZoriaRPG (discord: Timelord) 10/24/2021 18:22

Without the metrics and frame details, if fell to the bottom of my list. scripts allow implementation of it by anyone who wants to try and if they provide the script then  we could add I to future engine versions.
## ❌🔒Allowing variables, or constants to be used in defining size for an array? (#902)
@ OmegaX opened this issue on 09/25/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/891176320187379714



=== @ OmegaX 09/25/2021 04:16

(Using ZC 2.55 Alpha 96)

For some reason this isn't a thing even though the documentation says it supports it (ZScript_Additions: line 808-834, I don't know if I'm misreading it or if I'm going crazy).

This is what I have been trying to do but the compiler spits out an error at me: 
int ArraySize = ArrayWidth * ArrayHeight;
int TempRoomArray[ArraySize];

=== @ OmegaX 09/25/2021 04:18

(meta) thread name was changed: Allowing variables, or constants to be used in defining size for an array?

=== @EmilyV99 (discord: Emily) 09/25/2021 04:29

Is this being done inside a function, or globally?
@ OmegaX

=== @ OmegaX 09/25/2021 04:32

Inside a function

=== @EmilyV99 (discord: Emily) 09/25/2021 04:32

should work for constants or variables

=== @ OmegaX 09/25/2021 04:35

Pass 1: Parsing
Pass 2: Preprocessing
Pass 3: Registration
Pass 4: Analyzing Code

Final Adventure Quest\Final Adventure Scripts\DMap Scripts\Z3ScrollingEngine.zs Line 90 @ Columns 31-40 - Error T046: An expression is not constant that needs to be.

Compile took 0.104000 seconds (104 cycles)
This is what im getting from allegro.log

=== @EmilyV99 (discord: Emily) 09/25/2021 04:38

oh, yeah, variables wouldn't work
oof
constants will work, though, if you make it `const int`
oh
the documentation specifically says `constant expression`
> Arrays now support being declared with any constant expression.
variables are not constant
so

=== @ OmegaX 09/25/2021 04:41

But the code examples shown below seem to suggest otherwise??? (I think I may be misinterpreting it...)

=== @EmilyV99 (discord: Emily) 09/25/2021 04:42

>     [example--
> 
>         int arr[10*4]; 
>         //This is now the same as int arr[40];
>         
>     --end example]
`10*4` are both number literals
`10*4` is constant, it is always `40`
>     [example--
> 
>         const int sARR_MAX = 20;
>         int arr[sARR_MAX];
>         
>     --end example]
That's a `const int`
a constant, not a variable

=== @ OmegaX 09/25/2021 04:43

so this would never work: const int ArraySize = ArrayWidth * ArrayHeight;

=== @EmilyV99 (discord: Emily) 09/25/2021 04:44

if `ArrayWidth` and `ArrayHeight` are constants, it would
```cpp
const int WIDTH = 5;
const int HEIGHT = 10;
const int SIZE = WIDTH*HEIGHT;
int arr[SIZE];```
that works fine

=== @ OmegaX 09/25/2021 04:45

(replying to @EmilyV99 (discord: Emily) "if `ArrayWidth` and `ArrayHei…"): those two variables are not constant in my script...
RoomWidth = TempRoomX2 - TempRoomX1;
RoomHeight = TempRoomY2 - TempRoomY1;
const int ArrayWidth = RoomWidth / SCREEN_W;
const int ArrayHeight = RoomHeight / SCREEN_H;
const int ArraySize = ArrayWidth * ArrayHeight;
int TempRoomArray[ArraySize];

=== @EmilyV99 (discord: Emily) 09/25/2021 04:46

then yep, that won't work there
the value needs to be constant at compile time
for the compiler to size the array

=== @ OmegaX 09/25/2021 04:48

damn...

=== @EmilyV99 (discord: Emily) 09/25/2021 04:49

I will tell you, making an array really big doesn't hurt that much at all
so you can just make them really big

=== @ OmegaX 09/25/2021 04:56

Can I create an array, fill it up to a certain point (for ex: array size being 30 and the point we fill it up too is up to entry 10, with the other 20 being empty or 0) and then copy that array onto empty variable with only those filled in values (essentially another array with a size of 10)?

=== @EmilyV99 (discord: Emily) 09/25/2021 05:02

. . . how would you size that other array any differently?
Anyway, when you create an array, everything in it is 0 by default

=== @ OmegaX 09/25/2021 05:03

Well I’m out of ideas...

=== @EmilyV99 (discord: Emily) 09/25/2021 05:04

....just make it bigger than you need it to be?
What is the biggest it could ever need to be?
Or if you need all the space, just make it sized `MAX_INT`

=== @ OmegaX 09/25/2021 05:15

May I ask why ZC can't use variables to define array size? (being able to do something like would be really useful)

=== @EmilyV99 (discord: Emily) 09/25/2021 05:28

because it uses the size during compile
it might be able to be changed, but it wouldn't work well with global arrays, which would be problematic and/or require additional error checking, which is a bunch of work to do.

=== @EmilyV99 (discord: Emily) 09/28/2021 15:14

(meta) thread name was changed: ❌🔒Allowing variables, or constants to be used in defining size for an array?
## ✅🔒custom MISC Death animation not playing all the way through (#903)
@ FireSeraphim opened this issue on 09/25/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891354181447856138



=== @ FireSeraphim 09/25/2021 16:03

I'm running into a curious phenomenon where the last 4 frames of my custom animation for the MISC:Death sprite is simply not playing. I partly suspect it has something to do with how that animation is handled by default. I have the number of frames set to nine and the animation speed set to six. The animation speed variable doesn't seem affect MISC:Death.

=== @ FireSeraphim 09/25/2021 16:05

As a test, I recommend starting a fresh quest file and then importing and setting this https://cdn.discordapp.com/attachments/598566141992108032/891132421884506122/16x16_IOG_Death_Animation.png as the MISC:Death animation (since that's what I was using) with the same numbers I was using.

=== @ FireSeraphim 09/25/2021 16:14

I went ahead and make a quick pair of gifs to illustrate what's actually happening in comparison to what should be happening

=== @ FireSeraphim 09/25/2021 16:15

This is how it looks in game due to the bug in question
![image](https://cdn.discordapp.com/attachments/891354181447856138/891357283399905300/How_it_actually_looks_in_game.gif)

=== @ FireSeraphim 09/25/2021 16:16

This is how it should look. The animation and spritework is meant to resemble the enemy death animation from Illusion of Gaia
![image](https://cdn.discordapp.com/attachments/891354181447856138/891357586815860756/How_it_should_look.gif)

=== @ FireSeraphim 09/25/2021 16:45

@<role: Developer> Sorry to pester you guys, but I figure a bug like this wouldn't be too difficult to fix

=== @ P-Tux7 09/26/2021 01:43

while we're at it, can you check the poof spawn animation as well?
and the "blocked" effect (boomerang on edge of screen or shooting an arrow at a darknut)

=== @EmilyV99 (discord: Emily) 09/26/2021 04:31

The `iwDeath` sprite only reads the tile, nothing else. So the frame count/speed is hard-coded.
to fix this without giving enemies custom death sprites per-enemy would be stupid... so this'll be fixed whenever the energy to add that is found

=== @EmilyV99 (discord: Emily) 09/28/2021 03:58

so
firstly

![image](https://cdn.discordapp.com/attachments/891354181447856138/892258891084234762/unknown.png)
this won't fix the frames, but lets you pick what sprite you want

=== @ FireSeraphim 09/28/2021 04:10

Thank you. I take it that it will be tonight's nightly build?

=== @EmilyV99 (discord: Emily) 09/28/2021 04:11

still working on fixing the frames part

=== @ FireSeraphim 09/28/2021 04:11

I see...

=== @EmilyV99 (discord: Emily) 09/28/2021 05:06

O-KAY
```cpp
int lweapon->ShadowSprite;
int eweapon->ShadowSprite;
int itemsprite->ShadowSprite;
int npc->ShadowSprite;
int npc->SpawnSprite;
int npc->DeathSprite;
int npcdata->ShadowSprite;
int npcdata->SpawnSprite;
int npcdata->DeathSprite;```
9 new zscript vars added

=== @EmilyV99 (discord: Emily) 09/28/2021 05:09

@ FireSeraphim if you wouldn't mind testing this out

=== @ FireSeraphim 09/28/2021 05:09

Honestly I'm not a coder by any means.

=== @EmilyV99 (discord: Emily) 09/28/2021 05:09


https://cdn.discordapp.com/attachments/891354181447856138/892276911571599380/buildpack.zip
not necessarily the script part
There's a QR under `Backwards compat -> 3` for changing the hardcoded frames
and the enemy editor `Graphics->Sprites` tab for changing the sprites on enemies without scriptsw

=== @ FireSeraphim 09/28/2021 05:11

I'll test the QR thing. I'm not interested in driving myself mad by trying to manually set each enemy's death sprite to a new one

=== @EmilyV99 (discord: Emily) 09/28/2021 05:12

as long as it fixes the issue you reported

=== @ FireSeraphim 09/28/2021 05:21

I'm testing it now. I'll let you how it pans out on that front

=== @EmilyV99 (discord: Emily) 09/28/2021 05:22

The ability to switch the sprite was the easy part, so frankly I don't expect issues with that at all
but the animation frames stuff is janky AF
thankfully if it works in once place it should work in all since it's the same code

=== @ FireSeraphim 09/28/2021 05:23

It works on my end. Now I just need to tweak the death animation to not play so fast

=== @EmilyV99 (discord: Emily) 09/28/2021 05:23

woo
it played fast, that's a good sign
guessing the speed was 0?

=== @ FireSeraphim 09/28/2021 05:24

I had the speed on six for a nine frame animation

=== @EmilyV99 (discord: Emily) 09/28/2021 05:24

ah, you had edited it
that's about half a second for the whole anim
...given, the engine one only ran for 18 frames
if I read this right anyway
I'll leave this open marked sick for a bit in case any issues come up with it
(meta) thread name was changed: 💊🔓custom MISC Death animation not playing all the way through

=== @ FireSeraphim 09/28/2021 05:28

Not quite there yet...
Now I can't help but to wonder if I'm doing it wrong on my end.

=== @EmilyV99 (discord: Emily) 09/28/2021 05:29

oh?
What's your setup

=== @ FireSeraphim 09/28/2021 05:29

9 frames, speed of 12 (and the animation still seems to play too fast from what I'm seeing)
(replying to @ FireSeraphim "As a test, I recommend starti…"): These are the sprites I'm using

=== @EmilyV99 (discord: Emily) 09/28/2021 05:30

this is unchecked?
![image](https://cdn.discordapp.com/attachments/891354181447856138/892282028303712334/unknown.png)

=== @ FireSeraphim 09/28/2021 05:30

Yep

=== @ FireSeraphim 09/28/2021 05:33

Is a lower number the way to go for a slower animation? Just now tried it with the frame speed set to 16 as a brute force measure

=== @EmilyV99 (discord: Emily) 09/28/2021 05:33

lower is faster
I noticed something wrong
one moment

https://cdn.discordapp.com/attachments/891354181447856138/892283008122499072/zelda.exe
try that
(I thought the sprite anim clock was counting up.... turns out it was counting *down*, so something was set up backwards... oops)

=== @ FireSeraphim 09/28/2021 05:39

Nope. Just now set the animation frame speed to eight and it's still playing too fast

=== @EmilyV99 (discord: Emily) 09/28/2021 05:39

Really?
oh wait
fuck
I'm stupid

=== @EmilyV99 (discord: Emily) 09/28/2021 05:41


https://cdn.discordapp.com/attachments/891354181447856138/892284870661918740/zelda.exe

https://cdn.discordapp.com/attachments/891354181447856138/892285018964111380/zquest.exe

=== @ FireSeraphim 09/28/2021 05:45

You'll have to zip those. Chrome is being a paranoid bitch

=== @EmilyV99 (discord: Emily) 09/28/2021 05:47


https://cdn.discordapp.com/attachments/891354181447856138/892286288428949545/buildpack.zip

=== @ FireSeraphim 09/28/2021 05:50

Okay, now this going to the freaking twilight zone. Link has utterly vanished!
Where is Elf?
![image](https://cdn.discordapp.com/attachments/891354181447856138/892287211205185576/zc_screen00005.png)

=== @EmilyV99 (discord: Emily) 09/28/2021 05:54

...wtf
....not gonna get this done tonight.

=== @ FireSeraphim 09/28/2021 06:16

@EmilyV99 (discord: EmilyV) I did some further testing
It only seems to affect my quest
Link seems to appear just fine in other quests

=== @EmilyV99 (discord: Emily) 09/28/2021 06:18

...load an older backup of your quest?

=== @ FireSeraphim 09/28/2021 06:18

I am temporarily re-enabling the QR for backwards compatibility
just to see if it fixes that anomalous behavior
and then I'll load an older copy of my project afterwards as a futher test

=== @ FireSeraphim 09/28/2021 06:23

loaded and tested the copy I sent you at 'round midnight and the same phantom elf problem persists

=== @EmilyV99 (discord: Emily) 09/28/2021 06:24

Did the QR fix it?

=== @ FireSeraphim 09/28/2021 06:24

Nope
I did some futher tentative experiementation and link and the enemy and item sprites are invisible. I can seemingly still move the invisible elf into new screens and all
the items aren't invisible in the subscreens.

=== @ FireSeraphim 09/28/2021 06:27

enemy shadows are still visible as well as other particle effects (have not tried giving myself a magic or fire boomerang yet)

=== @EmilyV99 (discord: Emily) 09/28/2021 06:28

How about `Old (Faster) Sprite Drawing`, under `backwards compat -> 2`

=== @ FireSeraphim 09/28/2021 06:29

Trying that now.

=== @ FireSeraphim 09/28/2021 06:30

That seems to have fixed the invisible elf problem

=== @EmilyV99 (discord: Emily) 09/28/2021 06:31

that helps narrow it down

=== @ FireSeraphim 09/28/2021 06:31

Now I am going to do yet another test and re-disable the new QR you added for death animation as a experiement

=== @EmilyV99 (discord: Emily) 09/28/2021 06:32

The funny thing is, the same new code runs regardless of the state of the old drawing QR
so a new issue shouldn't be caused by that
let me rebuild from clean

=== @EmilyV99 (discord: Emily) 09/28/2021 06:37


https://cdn.discordapp.com/attachments/891354181447856138/892298998487064637/buildpack.zip
@ FireSeraphim try this, either will fix everything or change nothing

=== @ FireSeraphim 09/28/2021 06:38

Alright.
I'll let you know how it goes

=== @ FireSeraphim 09/28/2021 06:43

It seems to play alright so far, other than the `Old (Faster) Sprite Drawing` rule still being enabled. The new death animation QR is still disabled but I'm noticing an old thing where the death animation doesn't play all the way through on certain enemies (zols and bats) and the death animation is still too fast despite me setting it to a frames speed of 16.
I am going to disable the `Old (Faster) Sprite Drawing` rule real quick and see how that pans out

=== @EmilyV99 (discord: Emily) 09/28/2021 06:44

if the death compat qr is checked, the animations will be locked in speed and frames
also I just noticed another issue

=== @ FireSeraphim 09/28/2021 06:44

that QR is currently not checked

=== @EmilyV99 (discord: Emily) 09/28/2021 06:44

fun

=== @ FireSeraphim 09/28/2021 06:45

disabled `Old (Faster) Sprite Drawing` just now and the elf and friends are once again invisible

=== @EmilyV99 (discord: Emily) 09/28/2021 06:52

ok, try this one now.

https://cdn.discordapp.com/attachments/891354181447856138/892302947810148392/buildpack.zip

=== @ FireSeraphim 09/28/2021 07:06

Elf and friends are no longer invisible. You're making steps in the right direction, but custom death animations are still borked, in that it doesn't play all the way through and on some enemies it starts on a different frame (bats and gels come to mind as an example)

=== @EmilyV99 (discord: Emily) 09/28/2021 07:07

send allegro.log

=== @ FireSeraphim 09/28/2021 07:07


https://cdn.discordapp.com/attachments/891354181447856138/892306507100725268/allegro.log

=== @EmilyV99 (discord: Emily) 09/28/2021 07:08

hmm, that only has zq logs
run it in zc again, make sure to watch a death animation
then send allegro.log

=== @ FireSeraphim 09/28/2021 07:09

I just now enabled log game events and log script errors to allegro.log in my quest

=== @EmilyV99 (discord: Emily) 09/28/2021 07:09

shouldn't matter
I added debug logs
which don't care about the rules
should also show in the console if you have that open

=== @ FireSeraphim 09/28/2021 07:11

I don't have that opened

=== @EmilyV99 (discord: Emily) 09/28/2021 07:11

it'll also show in allegro.log, so

=== @ FireSeraphim 09/28/2021 07:15

I currently have the misc-death animation at a framespeed of 16 if that helps. I haven't changed that since last time
https://cdn.discordapp.com/attachments/891354181447856138/892308527509565500/allegro.log

=== @EmilyV99 (discord: Emily) 09/28/2021 07:16

huh, not seeing anything in the log
Go to `ZC->Show ZScript Debugger`

=== @ FireSeraphim 09/28/2021 07:17

where?

=== @EmilyV99 (discord: Emily) 09/28/2021 07:17


![image](https://cdn.discordapp.com/attachments/891354181447856138/892309020138946600/unknown.png)

=== @ FireSeraphim 09/28/2021 07:17

Oh

=== @ FireSeraphim 09/28/2021 07:21

Here's the log after the debugger been enabled
https://cdn.discordapp.com/attachments/891354181447856138/892310056178167878/allegro.log
I suspect the text near the bottom would be of interest to you

=== @EmilyV99 (discord: Emily) 09/28/2021 07:22

nope, nothing there useful
the debugger being on won't change allegro.log
it will let you see the information printouts as it happens
which should be whenever something is doing a death animation

=== @ FireSeraphim 09/28/2021 07:24

I don't know what you're looking for. I'm killing enemies and getting stuff like DeathAnim: (3/16), fr (5/9)
the fr 2/9 is coming from me killing keese

=== @EmilyV99 (discord: Emily) 09/28/2021 07:25

It should be printing once per frame of the animation
so the first is saying `(3/16) speed`
and `frame (5/9)`
for a 9-frame 16-speed sprite

=== @ FireSeraphim 09/28/2021 07:26

fr 0/9 from killing gels (the little slimes)

=== @EmilyV99 (discord: Emily) 09/28/2021 07:26

it should be making multiple prints per enemy
Technically, if it were working right, it should print `9*16` times per enemy

=== @ FireSeraphim 09/28/2021 07:26

it is, but the fr numbers is remaining the same per enemy killed

=== @EmilyV99 (discord: Emily) 09/28/2021 07:27

that... isn't right

=== @ FireSeraphim 09/28/2021 07:27

just not got multiple fr 2/9 from killing a keese once

=== @EmilyV99 (discord: Emily) 09/28/2021 07:28

you should get the same fr value 16 frames in a row

=== @ FireSeraphim 09/28/2021 07:29

I don't know what to tell you because I don't know what you're looking for.

=== @EmilyV99 (discord: Emily) 09/28/2021 07:29

hopefully for those values to appear in allegro.log
because everything in the console should appear in the log

=== @ FireSeraphim 09/28/2021 07:31

new fresh allegro.log, just now saved and quited
https://cdn.discordapp.com/attachments/891354181447856138/892312445769625600/allegro.log
The fuck?

=== @EmilyV99 (discord: Emily) 09/28/2021 07:31

something's certainly wrong
because none of that is in the log

=== @ FireSeraphim 09/28/2021 07:33

awkward gadwin printscreen time

=== @ FireSeraphim 09/28/2021 07:34

A fullscreen screenshot, debugger in the background of me just now killing a single keese
![image](https://cdn.discordapp.com/attachments/891354181447856138/892313233266966538/Screen_Shot_001.PNG)
and the resulting printout

=== @EmilyV99 (discord: Emily) 09/28/2021 07:34

ah fuck
figured out why it's carrying over
...still not figured out why the animation isn't playing proper length

=== @ FireSeraphim 09/28/2021 07:35

screenshot from me killing a single gel
![image](https://cdn.discordapp.com/attachments/891354181447856138/892313521801560064/Screen_Shot_002.PNG)

=== @ FireSeraphim 09/28/2021 07:37

screenshot from me killing a single blue tektite
![image](https://cdn.discordapp.com/attachments/891354181447856138/892314043799457792/Screen_Shot_004.PNG)

=== @EmilyV99 (discord: Emily) 09/28/2021 07:45

ok, think I fixed it entirely?

=== @ FireSeraphim 09/28/2021 07:46

I don't know.

=== @EmilyV99 (discord: Emily) 09/28/2021 07:46


https://cdn.discordapp.com/attachments/891354181447856138/892316297705160704/buildpack.zip
wait, but I forgot to apply the same fix to the spawn poof
one sec

=== @EmilyV99 (discord: Emily) 09/28/2021 07:48


https://cdn.discordapp.com/attachments/891354181447856138/892316822160936970/buildpack.zip

=== @ FireSeraphim 09/28/2021 07:50

the death animation seems to be working for the most part. There's just a minor curious hiccup where near the end of the animation it repeats the first frame, it's appropriately slow at a speed of 16 so I'm going to dial that back down to 8 and see how that looks

=== @ FireSeraphim 09/28/2021 07:53

oh boy. dialed it down to eight and the zol (little gels) are still playing the animation really slow.

=== @ FireSeraphim 09/28/2021 07:54

ditto for the octorocks playing the death animation slow despite me dialing the animation speed back down to eight (the keese seem to respect the animation speed variable and plays it at the expected 8 speed)

=== @EmilyV99 (discord: Emily) 09/28/2021 07:55

it should be all or nothing

=== @ FireSeraphim 09/28/2021 07:56

peahats seem to respect the 8 anim. speed
black and red moblins play the animation slow

=== @EmilyV99 (discord: Emily) 09/28/2021 07:58

they should play it the same if it's set to the same sprite

=== @ FireSeraphim 09/28/2021 08:05

I checked. They are set to the same sprite

=== @EmilyV99 (discord: Emily) 09/28/2021 08:07

see if this fixes anything

https://cdn.discordapp.com/attachments/891354181447856138/892321839899115530/buildpack.zip

=== @ FireSeraphim 09/28/2021 08:12

gels, octorock and moblins are still playing the animation slow. Other than that you have seemed to fix the hiccup I mentioned previously

=== @EmilyV99 (discord: Emily) 09/28/2021 08:14

in my test quest octoroks play it fine

=== @ FireSeraphim 09/28/2021 08:15

What I just sent you my quest again via dm? I suspect that might be more productive

=== @EmilyV99 (discord: Emily) 09/28/2021 08:15

sure
With 9 frames 8 speed, that should be 72 frames, just over a second

=== @EmilyV99 (discord: Emily) 09/28/2021 08:22

@ FireSeraphim it seems to be working fine in your quest

=== @ FireSeraphim 09/28/2021 08:23

Wha?
that's not what I'm seeing on my end

=== @EmilyV99 (discord: Emily) 09/28/2021 08:23

are you loading a fresh save file?
or one that was saved before?
....given, I don't think that should matter, but that's always the first thing I check

=== @ FireSeraphim 09/28/2021 08:25

just now started and tested a fresh save file
still having the slow anim. from gels

=== @EmilyV99 (discord: Emily) 09/28/2021 08:25

Zoras and Octoroks appear to be animating properly
I frame-counted with frame-advance
the full anim is 72 frames long
which is a bit slow
but that's how you have it set up

=== @ FireSeraphim 09/28/2021 08:27

have you killed a keese yet?

=== @EmilyV99 (discord: Emily) 09/28/2021 08:27

oh
I just killed a tektite
so, uh
the slow animation is not the problem
that's correct
the fast one is the problem

=== @EmilyV99 (discord: Emily) 09/28/2021 08:31

oh
oh wait you motherfucker
. . . so, enemies that are in the air are drawn multiple times per frame. Which uh. Fuck.
Need to move where this logic is done

=== @ FireSeraphim 09/28/2021 08:47

well at least it's two steps forward and one step back, right?

=== @EmilyV99 (discord: Emily) 09/28/2021 08:56

so, the invisibility seems to like coming back constantly on me
but goes away when I build from clean
....fun annoyances that make it take much longer to compile, yay
<a:hugheart:884673091878391828>
hopefully this will be done soon

=== @EmilyV99 (discord: Emily) 09/28/2021 09:55

fucking hell
that was an hour solid of trying to get sprites to stop being invisible
I hate everything
I think I fixed everything

=== @EmilyV99 (discord: Emily) 09/28/2021 10:03

@ FireSeraphim let me know if this works when you get the chance
https://cdn.discordapp.com/attachments/891354181447856138/892350870614847528/buildpack.zip

=== @ P-Tux7 09/28/2021 16:05

thanks a ton
(replying to @ FireSeraphim "the death animation seems to…"): this is how all animations work iirc with the looping
so putting a duplicate frame at the end can pretty much fix the appearance of it

=== @EmilyV99 (discord: Emily) 09/28/2021 16:22

I fixed that issue

=== @ FireSeraphim 09/28/2021 18:17

Sorry about that guys, I was honesty up past what I should have been
I'm in the Central Time Zone and our discussion (for me at least) was past midnight.
I'll promptly let you know how it both pans out

=== @ FireSeraphim 09/28/2021 18:40

I can confirm that the animation bug is fixed on my end. With one caveat: now the octorock, gels, keese and moblins are missing their death sound while the aquamentus and dodongos aren't.
Just one last little problem

=== @ FireSeraphim 09/28/2021 19:17

I'll be back in an hour or two

=== @ FireSeraphim 09/28/2021 21:32

I'm back.

=== @ FireSeraphim 09/29/2021 00:58

Hey @EmilyV99 (discord: EmilyV)
Ping me or DM me when you're ready

=== @ FireSeraphim 09/29/2021 02:01

I kinda want to see this last little hurdle dealt with.

=== @EmilyV99 (discord: Emily) 09/29/2021 02:18

I'll get to it when I can

=== @EmilyV99 (discord: Emily) 09/29/2021 02:49

@ FireSeraphim see if this fixes the death sounds
https://cdn.discordapp.com/attachments/891354181447856138/892603909967843368/buildpack.zip

=== @ FireSeraphim 09/29/2021 03:24

I can confirm it is fixed.

=== @ FireSeraphim 09/29/2021 06:04

@EmilyV99 (discord: EmilyV) Hello?

=== @EmilyV99 (discord: Emily) 09/29/2021 06:05

hi

=== @ FireSeraphim 09/29/2021 06:14

As I just said I can confirm it is fixed. I tested the new build you sent me and it the problem is finally fixed

=== @EmilyV99 (discord: Emily) 09/29/2021 06:20

Good

=== @EmilyV99 (discord: Emily) 09/29/2021 07:23

(meta) thread name was changed: ✅🔒custom MISC Death animation not playing all the way through
## ✅🔒Quest Icons revert on relaunch (#904)
@ NightmareJames opened this issue on 09/25/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891427226623561768



=== @ NightmareJames 09/25/2021 20:53

Quest Icons change after saving quest, but not after loading quest or reloading quest after shutdown.  Just back to default quest icons
Alpha 96 Nightly 9/23/2021

=== @ P-Tux7 09/26/2021 01:44

oh yeah i noticed years ago and reported it on the old server. this applies to getting a ring and then BEATING a quest without saving as well
it may be tricky to write it to the save file without saving the rest of the game as well

=== @ P-Tux7 09/26/2021 01:46

but wait, that's odd... isn't the game saved after winning it? i wonder what the issue is here

=== @EmilyV99 (discord: Emily) 09/28/2021 15:08

no, p-tux, that's unrelated
this is a bug with the `reload_game_icons` config

=== @EmilyV99 (discord: Emily) 09/29/2021 13:45

@ NightmareJames try this
https://cdn.discordapp.com/attachments/891427226623561768/892769003410436106/buildpack.zip
(meta) thread name was changed: 💊🔓Quest Icons revert on relaunch

=== @ NightmareJames 09/29/2021 15:12

Fixed

=== @EmilyV99 (discord: Emily) 10/04/2021 10:59

(meta) thread name was changed: ✅🔒Quest Icons revert on relaunch
## ✅🔒CSet2 issue on loading tileset? (#905)
@ Moosh opened this issue on 09/26/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891560675233640519



=== @ Moosh 09/26/2021 05:43

Attempting to load DoR in the latest nightly is yielding some seriously strange results. Many combos have wonky CSet2 properties and cset offsets

![image](https://cdn.discordapp.com/attachments/891560675233640519/891560706888044614/unknown.png)
Here's what one of the sample screens look like

=== @ Moosh 09/26/2021 05:45

Here's what one of the combos looks like in the editor
![image](https://cdn.discordapp.com/attachments/891560675233640519/891561046127558666/unknown.png)
According to Russ CSet2 was set to 1 in 2.53. Now it's 15
Clicking a combo and clicking OK also changes it to 11

=== @EmilyV99 (discord: Emily) 09/26/2021 05:48

well this just jumped to next on my list... but I'm in the middle of adding #deleted-channel

=== @ Moosh 09/26/2021 05:50


![image](https://cdn.discordapp.com/attachments/891560675233640519/891562470446096444/unknown.png)

=== @EmilyV99 (discord: Emily) 09/26/2021 05:51

. . .

=== @ Moosh 09/26/2021 05:51

Same combo when viewed in 1.92
So it's meant to be shifting the tile back 1 cset

=== @EmilyV99 (discord: Emily) 09/26/2021 05:51

hmmm

=== @ Moosh 09/26/2021 05:52

Here's how the sample screen looks
![image](https://cdn.discordapp.com/attachments/891560675233640519/891562747521798205/unknown.png)

=== @ Moosh 09/26/2021 05:53

Combo page in 2.53 looks consistent
![image](https://cdn.discordapp.com/attachments/891560675233640519/891563003126886480/unknown.png)

=== @EmilyV99 (discord: Emily) 09/26/2021 05:53

so, the error is that `-1` is being wrapped improperly

=== @ Moosh 09/26/2021 05:53

That would seem to be the case

=== @EmilyV99 (discord: Emily) 09/26/2021 05:53

@arceusplayer11 (discord: Deedee)

=== @ Moosh 09/26/2021 05:54

Hopefully this is the only combo field being interpreted incorrectly...
Cause it'd suck to start a quest and then run into the discovery that my whole combo table had been corrupted :/

=== @EmilyV99 (discord: Emily) 09/26/2021 06:19

definitely @arceusplayer11 (discord: Deedee) https://github.com/ArmageddonGames/ZeldaClassic/commit/0be2f8f5328ba3a67e5b9e9ff437f0722bc83ffa
this isn't a problem I foresaw

=== @EmilyV99 (discord: Emily) 09/26/2021 06:21

see if you can figure out a good way to handle this, Dimi....

=== @EmilyV99 (discord: Emily) 09/26/2021 06:23

....also, why would you `vbound` and then `%12`? the modulo is supposed to be doing the bounding there, so the logic is slightly off

=== @EmilyV99 (discord: Emily) 09/26/2021 06:25

So, it seems that the issue is of sign
because the 0-16 value range
was treated as `-8 to 7`
....so, uh

=== @EmilyV99 (discord: Emily) 09/26/2021 06:31

something like
```cpp
if(loading_old_version)
{
    int cs = temp_combo.csets&15;
    if(cs&8) //sign bit
    {
        cs |= ~int(0xF); //bitwise shit to make it correct
        temp_combo.csets = 12+cs;
    }
}```
...won't work perfectly, but will fix most situations
it won't fix it if csets 12-15 were being used
@arceusplayer11 (discord: Deedee) 's change to fix, when she's up to it

=== @EmilyV99 (discord: Emily) 09/26/2021 07:05

....except wait, no
I know a better way to fix this.... dammit
now it's in my head so I guess I have to code it

=== @EmilyV99 (discord: Emily) 09/26/2021 07:42

@ Moosh

https://cdn.discordapp.com/attachments/891560675233640519/891590635595919420/zelda.exe

https://cdn.discordapp.com/attachments/891560675233640519/891590638305431582/zquest.exe
see how this build treats you

=== @ Moosh 09/26/2021 07:43

gimme a sec while windows detects a new virus 🤦

=== @EmilyV99 (discord: Emily) 09/26/2021 07:43

fun

=== @ Moosh 09/26/2021 07:44

"No current threats" fuck off and let me open the damn file
...what the fuck windows

=== @EmilyV99 (discord: Emily) 09/26/2021 07:45

windows is real nice sometimes
in all the worst of ways

=== @ Moosh 09/26/2021 07:46

I genuinely have no idea how to allow this build :/
Every other one, it gives me the warning, I tell it to allow it, bing bong goodbye
Here it pops up for a second, the immediately deletes the file

=== @EmilyV99 (discord: Emily) 09/26/2021 07:48


https://cdn.discordapp.com/attachments/891560675233640519/891591975436951583/Release.zip
maybe it'll like a zip better

=== @ Moosh 09/26/2021 07:50

That fixed it

=== @EmilyV99 (discord: Emily) 09/26/2021 07:51

confuse the virus-like antivirus via compression

=== @ Moosh 09/26/2021 07:51

It's weird because it still catches it and gives the exact same warning, but doesn't auto delete if it's in a zip

=== @EmilyV99 (discord: Emily) 09/26/2021 07:51

great job windows

=== @ Moosh 09/26/2021 07:52

Also I can add exclusions but only at an exact path. eg, a file named zelda.exe in my downloads folder but not any file named zelda.exe
That seems like an important distinction to be able to make

=== @EmilyV99 (discord: Emily) 09/26/2021 07:52

yep I hate that so much
guessing it doesn't like `*/zelda.exe` as a path, huh?

=== @ Moosh 09/26/2021 07:54

That would imply being able to specifiy a path as a string, rather than with a file picker dialogue 🤔

=== @EmilyV99 (discord: Emily) 09/26/2021 07:54

oof
probably a string somewhere in the registry.... totally safe to edit, right?

=== @ Moosh 09/26/2021 07:54

Maybe if I hack up some registry shit it'd work, but it's not worth that level of effort

=== @EmilyV99 (discord: Emily) 09/26/2021 07:55

Anyway, to the issue at hand
there's a compat QR, should be enabled when loading any quest saved before *this build*
with it on, cset2 will work exactly as before

=== @ Moosh 09/26/2021 07:56

probably sound like a boomer here but this just shows how infanitilized tech is becoming.

=== @EmilyV99 (discord: Emily) 09/26/2021 07:56

also, independently fixed the issue with negative values

=== @ Moosh 09/26/2021 07:57

I recall I used to complain about odd issues with windows usability but at least back then they could trust the user to use their own shit
And yeah, DoR appears to load properly now

=== @EmilyV99 (discord: Emily) 09/26/2021 07:57

now do `pick ruleset: modern`
and see if anything changes
(or disable the compat rule on the last tab)

=== @ Moosh 09/26/2021 07:58

Modern ruleset doesn't appear to have changed anything

=== @EmilyV99 (discord: Emily) 09/26/2021 07:59

k, so most of the issue was the separate bug
the QR affects the wrapping of csets, so if you have `CS 11, CS2 +1` that will go to `CS 12` in old quests, but `CS 0` in new quests

=== @EmilyV99 (discord: Emily) 09/26/2021 08:01

Any chance you have time to test #deleted-channel ?

=== @EmilyV99 (discord: Emily) 09/26/2021 08:04

(meta) thread name was changed: ✅🔒CSet2 issue on loading tileset?
## ✅🔒Demo ZX crashes on J-Dungeon Gleeok, Part 3 (#906)
@ NightmareJames opened this issue on 09/26/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891823251402158080



=== @ NightmareJames 09/26/2021 23:07

Demo ZX crashes on J-Dungeon Gleeok, Part 3, Reproducable
@EmilyV99 (discord: EmilyV) @arceusplayer11 (discord: Deedee) @ Moosh

=== @ NightmareJames 09/26/2021 23:08

Alpha 96 9/25/2021

=== @ NightmareJames 09/26/2021 23:09

Allegro Log
https://cdn.discordapp.com/attachments/891823251402158080/891823954115846165/allegro.log

=== @ Moosh 09/26/2021 23:16

Is this a script crash or purely engine? What's happening on that screen where it crashed and were you streaming when it happened?

=== @ NightmareJames 09/26/2021 23:17

I'll be posting the videos moemntarily
They're processing

=== @ NightmareJames 09/26/2021 23:20

https://youtu.be/_6DDSA-lYF0
https://youtu.be/y8r8vNPz5aI

=== @ NightmareJames 09/26/2021 23:26

@ DeletedUser

=== @ Deleted User 09/26/2021 23:26

I'm here.

=== @ NightmareJames 09/26/2021 23:28

@ Moosh The videos are up

=== @ Moosh 09/26/2021 23:30

So something related to the gleeok taking damage I assume

=== @ Moosh 09/26/2021 23:31

To be clear, is this the kind of crash where Windows reports ZC is not responding, the kind of crash where the window closes immediately, or the kind where the screen stops updating

=== @ NightmareJames 09/26/2021 23:36

Yes

=== @ NightmareJames 09/27/2021 14:29

Reproduced the crash in another room, this time the Pols Voice room/Like Like room with Red and Blue Bubbles.  Has something to do with Red Bubble Jinxes I believe, which were also in the Gleeok room
I could recreate all three rooms in a test quest with all the current items if needed
Quest in question
https://cdn.discordapp.com/attachments/891823251402158080/892055745946849350/demozx255.qst

=== @ NightmareJames 09/27/2021 14:36

Cheat Codes:  Lv. 3:  "Phantom Menace"  Lv. 4:  "Huan ying guang lin"

=== @ NightmareJames 09/27/2021 15:09

Tested ZNR with the same conditions.  It did not crash.  So it's the jinx AND something else

=== @ NightmareJames 09/27/2021 15:17

Couldn't replicate it on Downfall either

=== @ NightmareJames 09/27/2021 16:30

Ruled out upgrading FFCScript to 2.0.1 too

=== @ NightmareJames 09/27/2021 16:50

Ruled out upgrading Ghost to 2.8.15 too :: sigh ::
I'm about out of things I can try

=== @EmilyV99 (discord: Emily) 09/28/2021 13:57

your cheat4 is typoed, it has an extra space after the last letter

=== @EmilyV99 (discord: Emily) 09/28/2021 14:08

Exception thrown: Read access violation, zfix::getInt()
...which doesn't tell me anywhere near enough context, yay
it probably tried to read an invalid zfix pointer or something

=== @EmilyV99 (discord: Emily) 09/28/2021 14:13

it occurs even if I just stand on the screen invincible in the wall

=== @EmilyV99 (discord: Emily) 09/28/2021 14:33

fuck
I thought I had converted all of those calls....
this very much seems to be my fault

=== @EmilyV99 (discord: Emily) 09/28/2021 14:35

So, there was a rand call that wasn't converted properly
and it was selecting negative heads of the gleeok
which uh
isn't fun for memory access

=== @EmilyV99 (discord: Emily) 09/28/2021 14:42

@ NightmareJames @ FireSeraphim should fix crashes
https://cdn.discordapp.com/attachments/891823251402158080/892420985301663784/buildpack.zip

=== @EmilyV99 (discord: Emily) 09/28/2021 14:45

(meta) thread name was changed: 💊🔓Demo ZX crashes on J-Dungeon Gleeok, Part 3

=== @ NightmareJames 09/28/2021 15:42

I recompiled Demo ZX in A97.  Hopefully these bugs are crushed
I also upgraded ffcscript and ghost to as far as they could go to avoid other hassles

=== @ NightmareJames 09/28/2021 16:17

All fixed
Raid kills bugs DEAD
@<role: Developer>

=== @EmilyV99 (discord: Emily) 09/28/2021 16:35

(meta) thread name was changed: ✅🔒Demo ZX crashes on J-Dungeon Gleeok, Part 3
## ✅🔒Demo ZX (recompile) - Enemies spawning on solid tiles (#907)
@ NightmareJames opened this issue on 09/26/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891829309067632640



=== @ NightmareJames 09/26/2021 23:31

Just confirmed this in the quest, several instances of enemies spawning on solid tiles.  Will post videos
Alpha 96 Nightly 9/25/2021
@EmilyV99 (discord: EmilyV) @arceusplayer11 (discord: Deedee) @ Moosh @ DeletedUser

=== @ NightmareJames 09/26/2021 23:42

https://youtu.be/pnXjddlEhHU  Video

=== @ Deleted User 09/27/2021 00:17

I'm here.

=== @EmilyV99 (discord: Emily) 09/28/2021 14:48

Same thing that fixes #906 might fix this too
(meta) thread name was changed: 💊🔓Demo ZX (recompile) - Enemies spawning on solid tiles

=== @ NightmareJames 09/28/2021 16:18

I haven't seen a reoccurance, but I'm going to further test to say before I say it's dead
@ FireSeraphim Check for me too please

=== @ FireSeraphim 09/28/2021 18:42

I can confirm that this bug has been fixed on my end. Gleeok also no longer crashes the game

=== @EmilyV99 (discord: Emily) 09/28/2021 23:46

(meta) thread name was changed: ✅🔒Demo ZX (recompile) - Enemies spawning on solid tiles
## ✅🔒Item cant be collected when `Always Grabbable` is checked. (#908)
@ Lincolnpepper opened this issue on 09/27/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891844020110774323



=== @ Lincolnpepper 09/27/2021 00:29

As far as I can tell, items cannot be collected when `Always Grabbable` is checked in the item editor or when the pickup flag `IP_ALWAYSGRAB` is true.

=== @EmilyV99 (discord: Emily) 09/28/2021 14:58

Fixed
There was a condition, and it was inverted
bleh
(meta) thread name was changed: ✅🔒Item cant be collected when `Always Grabbable` is checked.
## ✅🔒Compilling script causes audio playback (#909)
@ Mani Kanina opened this issue on 09/27/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891876852048756788



=== @ Mani Kanina 09/27/2021 02:40

Whenever you compile scripts in newer version of ZC it blarts loud audio. This is obviously an oversight, but it completely hurts the ears every time.
(I'm being slightly facitious, if it wasn't clear, but make it a toggle please).

=== @EmilyV99 (discord: Emily) 09/27/2021 02:40

zquest.cfg, literally at the top

=== @ Mani Kanina 09/27/2021 02:41

oh

=== @EmilyV99 (discord: Emily) 09/27/2021 02:41

@ Lunaria

=== @ Mani Kanina 09/27/2021 02:41

thanks

=== @EmilyV99 (discord: Emily) 09/27/2021 02:41

...should add gui setting for it

=== @ Mani Kanina 09/27/2021 02:41

that would be nice

=== @EmilyV99 (discord: Emily) 09/27/2021 02:41

so I'll leave this open

=== @ Mani Kanina 09/27/2021 02:41

thanks
👍

=== @arceusplayer11 (discord: Deedee) 01/15/2022 09:27

@EmilyV99 (discord: EmilyV) did you do the smart and add the gui?

=== @EmilyV99 (discord: Emily) 02/08/2022 11:37


![image](https://cdn.discordapp.com/attachments/891876852048756788/940571957617893386/unknown.png)
yes
(meta) thread name was changed: ✅🔒Compilling script causes audio playback

=== @EmilyV99 (discord: Emily) 02/09/2022 15:19

[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
## ✅🔒EWeapon Scripts No Longer Do Anything (#910)
@ Moosh opened this issue on 09/27/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891877678926422076



=== @ Moosh 09/27/2021 02:43

Pretty much what it says on the tin, lemme know if I'm doing something stupid here :/

https://cdn.discordapp.com/attachments/891877678926422076/891877713726541854/WeaponScriptDontDoShit.qst
Script is in the buffer, assigned to the enemy's weapon, and isn't tracing or playing the sound when the moblin fires

=== @ Moosh 09/27/2021 02:49

Expanding on the issue, lweapon scripts also appear to be gone. Stuck one on the wand, nothing happen
https://cdn.discordapp.com/attachments/891877678926422076/891879150778974228/WeaponScriptDontDoShit.qst

=== @EmilyV99 (discord: Emily) 09/27/2021 02:50


![image](https://cdn.discordapp.com/attachments/891877678926422076/891879492652519484/unknown.png)
so the weapon has a script assigned to it from the enemy data
it's just... not working

=== @ Moosh 09/27/2021 02:51

NPC scripts appear unaffected, they still run as expected
So it's just weapons

=== @EmilyV99 (discord: Emily) 09/27/2021 02:53

Just EWeapons, or LWeapons too?
And what about itemsprites?

=== @EmilyV99 (discord: Emily) 09/27/2021 02:56

OH fuck I'm dumb aren't I

=== @ Moosh 09/27/2021 03:00

sorry for late response, itemsprites still work

=== @EmilyV99 (discord: Emily) 09/27/2021 03:03

lweapons?

=== @ Moosh 09/27/2021 03:04

EWeapons and LWeapons are the only scripts that I've observed have the problem

=== @EmilyV99 (discord: Emily) 09/27/2021 03:06

GAH there's the typo
hopefully that fixes it...

=== @EmilyV99 (discord: Emily) 09/27/2021 03:09

@ Moosh
https://cdn.discordapp.com/attachments/891877678926422076/891884308095193119/2.55_NightlyBuild_Package.zip

=== @ Moosh 09/27/2021 03:10

Provided this works, is it safe to develop in?

=== @EmilyV99 (discord: Emily) 09/27/2021 03:11

provided this works I'll be posting it in [#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
so yes
this includes #deleted-channel too, now

=== @ Moosh 09/27/2021 03:15

Eyyy it all works

=== @EmilyV99 (discord: Emily) 09/27/2021 03:17

There's some stupid variable naming
And a backend refactor of some code left something checking `script` instead of `weaponscript`
... nice thing is now sprites (npc/wpn/itmspr) don't allocate script info or stack memory unless they have a script
And they all use a consistent function for script running
.... but weapons have a tiny difference for no good reason, thanks zoria.

=== @EmilyV99 (discord: Emily) 09/27/2021 03:24

(meta) thread name was changed: ✅🔒EWeapon Scripts No Longer Do Anything
## ✅🔒BitmapToTile() Function (#911)
@ Moosh opened this issue on 09/27/2021

Status: fixed

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/891941762359242772



=== @ Moosh 09/27/2021 06:58

This would work similarly to CopyTile() and similar functions, but be sourced from a ZScript bitmap. I imagine arguments would look something like:
`BitmapToTile(bitmap b, int x, int y, int dest, bool eightbit)`
It'd always copy in 16x16 sections from the source bitmap and if 8-bit is turned off, would merge the colors into one cset by index like in the editor. Hopefully the internals of CopyTile could do enough heavy lifting that the latter part isn't especially difficult. If not I wouldn't be against assuming 8-bit in all cases. But yeah, this would be handy for paper doll systems, switching out large graphics banks from external files (would probably require a loading screen) and just generally give ZScript total access to the tile page.

=== @EmilyV99 (discord: Emily) 09/27/2021 07:21

Tile stuff uses *pointer math*, so it's always a huge headache to comprehend what *anything* is doing
which is why this hasn't been done already
but, this is certainly something I'd like to add at some point

=== @EmilyV99 (discord: Emily) 09/29/2021 06:48

so
so
uh
this was way too easy

=== @EmilyV99 (discord: Emily) 09/29/2021 07:08

@ Moosh

![image](https://cdn.discordapp.com/attachments/891941762359242772/892669076382580766/2021-09-29_03-07-24.mp4)
All 17 of those tiles are blank at the start, and nothing ever changes what tiles are being displayed, nor is there any copytile usage.
Bitmap drawing to tiles magic
```cpp
void WriteTile( int layer, int x, int y, int tile, bool is8bit, bool mask);
 * Writes a 16x16 area from (x,y) of the bitmap at layer 'layer' 
 *     TO the tile page, overwriting the tile 'tile', either 4 or 8 bit.
 * If 'mask' is true, overlays instead of overwrites```

=== @ Moosh 09/29/2021 07:10

Splendid. And it's updating in real time too? Looks excellent

=== @EmilyV99 (discord: Emily) 09/29/2021 07:10

Obviously it has the same restraints as CopyTile
in that it won't carry over between reloads and such

=== @ Moosh 09/29/2021 07:10

No copying to blank tiles I assume

=== @EmilyV99 (discord: Emily) 09/29/2021 07:10

?

=== @ Moosh 09/29/2021 07:10

Though IIRC, flagging a tile as 8-bit makes it no longer treated as blank

=== @EmilyV99 (discord: Emily) 09/29/2021 07:11

why would you not be able to write to blank tiles

=== @ Moosh 09/29/2021 07:12

Beats me. Been that way as long as I remember. I kinda figured it had something to do with how tiles are compressed. Though in hindsight it may just be a bug 🤣

=== @EmilyV99 (discord: Emily) 09/29/2021 07:12

is that an issue with CopyTile?

=== @ Moosh 09/29/2021 07:12

As far as I can tell yeah
Didn't try with the other variations
And haven't tried it yet in 2.55 to be fair

=== @EmilyV99 (discord: Emily) 09/29/2021 07:13

I see no reason that should be the case
either for copytile or for this

=== @EmilyV99 (discord: Emily) 09/29/2021 07:16

..and uh, in fact, the tiles in the video were 'blank'
so

=== @EmilyV99 (discord: Emily) 09/29/2021 07:22

(meta) thread name was changed: ✅🔒BitmapToTile() Function
[#builds-255](https://discord.com/channels/876899628556091432/876906918847852594)
## ✅🔒Forgot to update std_zh with Nightly 9-27-2021 (#912)
@ NightmareJames opened this issue on 09/27/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/891986915430113320



=== @ NightmareJames 09/27/2021 09:57

Functions not compiling with Nightly 9-27-2021, inserted 9-25-2021's std_functions.zh and it compiled

![image](https://cdn.discordapp.com/attachments/891986915430113320/891987030928654366/unknown.png)
@EmilyV99 (discord: EmilyV) @ Moosh

=== @EmilyV99 (discord: Emily) 09/27/2021 10:00

god dammit I made a typo and forgot to compile check it

https://cdn.discordapp.com/attachments/891986915430113320/891987676507570206/std_functions.zh
does this compile right?

=== @ NightmareJames 09/27/2021 10:02

Works now

=== @EmilyV99 (discord: Emily) 09/27/2021 10:03

(meta) thread name was changed: ✅🔒Forgot to update std_zh with Nightly 9-27-2021
## ❌🔒Enemy Knockback (#913)
@ Architect Abdiel opened this issue on 09/28/2021

Status: wont-fix

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/892226946178641980



=== @ Architect Abdiel 09/28/2021 01:51

Apologies if this has already been requested, but I was wanting to request enemy knockback as a feature.

The idea is that take a darknut for instance. Darknuts probably wouldn't realistically get knocked back by sword as like a keese.

Furthermore, with enemies drowning in water being a thing, enemy knockback could be used to make that harder.

Bonus points if you could alter the knockback the enemy experiences based on weapons.

=== @EmilyV99 (discord: Emily) 09/28/2021 01:52

Scripts can access scripted knockback via new npc-> commands

=== @ P-Tux7 09/28/2021 16:02

the darknut thing isn't even scripted
you'd just set whatever npc flag determines knockback to 0 via npc script
as usual removing is easier than adding

=== @EmilyV99 (discord: Emily) 09/29/2021 11:08

(meta) thread name was changed: ❌🔒Enemy Knockback
## ✅🔒Weird enemy spawn position in current (as of the time of this posting) nighty build (#914)
@ FireSeraphim opened this issue on 09/28/2021

Status: fixed

Labels: ['bug']

Source: https://discord.com/channels/876899628556091432/892263135635988530



=== @ FireSeraphim 09/28/2021 04:15

The screenshot I'm about to post should clarify what I'm talking about. I've been noticing weird enemy spawn positions in a few screens in my side project.

![image](https://cdn.discordapp.com/attachments/892263135635988530/892263186806480906/zc_screen00004.png)

=== @ FireSeraphim 09/28/2021 04:29

So far I'm seeing it happen on screens with "enemies enter from the side - random" and one instance of "random spawn"

=== @ NightmareJames 09/28/2021 06:28

Second instance of this, thanks for reporting in a different quest @ FireSeraphim

=== @EmilyV99 (discord: Emily) 09/28/2021 15:01

see #907
(meta) thread name was changed: 💊🔓Weird enemy spawn position in current (as of the time of this posting) nighty build

=== @ FireSeraphim 09/28/2021 18:41

I can confirm that this bug has been fixed

=== @EmilyV99 (discord: Emily) 09/28/2021 23:45

(meta) thread name was changed: ✅🔒Weird enemy spawn position in current (as of the time of this posting) nighty build
## Higher level bracelets affecting block pushing speed as an item attribute (#915)
@ FireSeraphim opened this issue on 09/29/2021

Status: open

Labels: ['feature']

Source: https://discord.com/channels/876899628556091432/892601876720259103



=== @ FireSeraphim 09/29/2021 02:41

Wouldn't be possible to have bracelets that have a noticeable effect on pushing speeds on lower tiered/leveled blocks. An example being a Lv2 Bracelet pushing a Lv0 Block at a noticeably faster speed. Partially quoting myself but I think this simple tweak might be a good idea.

=== @EmilyV99 (discord: Emily) 09/29/2021 02:43

Wouldn't be level-based, would be an attribute of the bracelet item

=== @ FireSeraphim 09/29/2021 02:45

I see.

=== @ Alucard648 09/29/2021 03:33

And also ability to push multiple blocks at the same time.
https://www.purezc.net/index.php?page=scripts&id=394

=== @EmilyV99 (discord: Emily) 09/29/2021 03:39

oh
that uh, is less easy
because that requires rewriting how the movingblock sprite is handled
