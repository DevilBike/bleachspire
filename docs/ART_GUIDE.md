# Art guide

How to fill the mod with Bleach art. You collect the images yourself; this guide says what to look for and where each file goes.

## Who is who

| Slay the Spire 2 | Bleach | Why |
|---|---|---|
| Ironclad | Kenpachi Zaraki | Berserker who loves taking hits: Strength, self-damage, Exhaust |
| Silent | Soi Fon | Stealth-force assassin with a poison blade: Poison, Shivs, discard |
| Defect | Kisuke Urahara | Inventor with gadgets and kido: orbs |
| Regent | Byakuya Kuchiki | Noble whose Senbonzakura becomes countless blades: blade and stars |
| Necrobinder | Mayuri Kurotsuchi, with Nemu as Osty | Mad scientist with a loyal companion: the Osty cards are Nemu |

Chosen by Bike. To swap, change `BLEACH_CHARACTER` in `tools/asset_map.py` and `data/bleach_matches.csv`, then rerun `tools/asset_map.py`, `tools/make_drop.py` and `tools/art_guide.py`.

## Where to look (official sources)

- **VIZ Media Bleach page** (https://viz.com/bleach): English manga volumes and covers, plus links to the official Shonen Jump reader.
- **Bleach: Thousand-Year Blood War anime**: the official site and its key visuals, and screenshots you take yourself from the episodes on the streaming service you use.
- **Bleach: Brave Souls** (https://bleach-bravesouls.com): official character art from the KLab mobile game.
- **Bleach: Rebirth of Souls**: official screenshots and press art from Bandai Namco.
- Your own manga volumes or art books (for example *Bleach: All Colour But The Black*).

Card art shows at 250x190 (tall "ancient" cards 250x351) and in the big view at 4x that, so aim for at least 1000x760 and a landscape crop with the subject centred. Any size works; the build crops to fit.

## How to add an image

1. Open `drop/<wave>/<pool>/`. Every card already has a grey placeholder with its name.
2. Save your image over the placeholder, keeping the same file name (PNG or JPG renamed to .png both work).
3. Run `python tools/build_mod.py`. Placeholders are skipped, so a half-filled folder still builds.

Character images in `drop/1-every-run/characters/` are listed now and get wired into the build in the next step.

## Wave 1: every run (34 cards)

Also 71 character images: select screen, top-bar icons, map markers, energy icons and orbs (`drop/1-every-run/characters/`).

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Bash | ironclad | Kenpachi Zaraki | Kenpachi's two-handed Kendo overhead slash (vs Nnoitra) | `drop/1-every-run/ironclad/bash.png` |
| Defend | ironclad | Kenpachi Zaraki | Kenpachi taking a blade on his bare chest without flinching | `drop/1-every-run/ironclad/defend_ironclad.png` |
| Strike | ironclad | Kenpachi Zaraki | Kenpachi mid-swing with his chipped sword one-handed | `drop/1-every-run/ironclad/strike_ironclad.png` |
| Defend | silent | Soi Fon | Soi Fon in Onmitsukido stealth stance with arms crossed | `drop/1-every-run/silent/defend_silent.png` |
| Neutralize | silent | Soi Fon | Soi Fon's Suzumebachi butterfly mark (Homonka) appearing on a target | `drop/1-every-run/silent/neutralize.png` |
| Strike | silent | Soi Fon | Soi Fon lunging with Suzumebachi's stinger | `drop/1-every-run/silent/strike_silent.png` |
| Survivor | silent | Soi Fon | Soi Fon crouched and recovering after a hit | `drop/1-every-run/silent/survivor.png` |
| Defend | defect | Kisuke Urahara | Urahara blocking with his cane sword (Benihime) still sheathed | `drop/1-every-run/defect/defend_defect.png` |
| Dualcast | defect | Kisuke Urahara | Urahara firing two kido at once | `drop/1-every-run/defect/dualcast.png` |
| Strike | defect | Kisuke Urahara | Urahara drawing Benihime from his cane in one slash | `drop/1-every-run/defect/strike_defect.png` |
| Zap | defect | Kisuke Urahara | Urahara's fingertip Byakurai lightning | `drop/1-every-run/defect/zap.png` |
| Defend | regent | Byakuya Kuchiki | Byakuya's Senbonzakura petals swirling into a shield | `drop/1-every-run/regent/defend_regent.png` |
| Falling Star | regent | Byakuya Kuchiki | Senbonzakura petals raining down from above | `drop/1-every-run/regent/falling_star.png` |
| Strike | regent | Byakuya Kuchiki | Byakuya drawing Senbonzakura in a single clean slash | `drop/1-every-run/regent/strike_regent.png` |
| Venerate | regent | Byakuya Kuchiki | Byakuya standing calmly with his captain's haori and Kenseikan | `drop/1-every-run/regent/venerate.png` |
| Bodyguard | necrobinder | Nemu Kurotsuchi | Nemu standing guard beside Mayuri | `drop/1-every-run/necrobinder/bodyguard.png` |
| Defend | necrobinder | Nemu Kurotsuchi | Nemu stepping in front of Mayuri as a shield | `drop/1-every-run/necrobinder/defend_necrobinder.png` |
| Strike | necrobinder | Mayuri Kurotsuchi | Mayuri slashing with Ashisogi Jizo | `drop/1-every-run/necrobinder/strike_necrobinder.png` |
| Unleash | necrobinder | Mayuri Kurotsuchi | Mayuri sending Nemu into battle | `drop/1-every-run/necrobinder/unleash.png` |
| Beckon | status | Hollow | A Menos Grande reaching out of a Garganta | `drop/1-every-run/status/beckon.png` |
| Burn | status | Hollow | A Cero blast scorching the ground | `drop/1-every-run/status/burn.png` |
| Dazed | status | Shinigami | A Soul Reaper staggered by overwhelming spiritual pressure | `drop/1-every-run/status/dazed.png` |
| Debris | status | Karakura Town | Rubble of a collapsed building after a fight | `drop/1-every-run/status/debris.png` |
| Frantic Escape | status | Shinigami | A Soul Reaper fleeing with Shunpo (flash step blur) | `drop/1-every-run/status/frantic_escape.png` |
| Infection | status | Hollow | Hollowfication mask spreading across a face | `drop/1-every-run/status/infection.png` |
| Slimed | status | Mayuri Kurotsuchi | Mayuri melted into liquid form | `drop/1-every-run/status/slimed.png` |
| Soot | status | Hollow | Smoke and ash after an explosion in Karakura Town | `drop/1-every-run/status/soot.png` |
| Toxic | status | Mayuri Kurotsuchi | Mayuri's poison gas or a dripping syringe | `drop/1-every-run/status/toxic.png` |
| Void | status | Hollow | A Garganta tear opening into black space | `drop/1-every-run/status/void.png` |
| Wound | status | Shinigami | A bloodied Soul Reaper clutching a sword cut | `drop/1-every-run/status/wound.png` |
| Disintegration | token | Quincy | Quincy Blut or Sklaverei breaking down a body into reishi | `drop/1-every-run/token/disintegration.png` |
| Mind Rot | token | Aizen | Kyoka Suigetsu's hypnosis (Aizen's illusion) | `drop/1-every-run/token/mind_rot.png` |
| Sloth | token | Starrk | Coyote Starrk asleep or lounging | `drop/1-every-run/token/sloth.png` |
| Waste Away | token | Barragan | Barragan's Respira decaying something to dust | `drop/1-every-run/token/waste_away.png` |

## Wave 2: most runs (commons) (100 cards)

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Anger | ironclad | Kenpachi Zaraki | Kenpachi's yellow skull-shaped spiritual pressure flaring | `drop/2-most-runs/ironclad/anger.png` |
| Armaments | ironclad | Kenpachi Zaraki | Kenpachi gripping his notched blade with both hands | `drop/2-most-runs/ironclad/armaments.png` |
| Blood Wall | ironclad | Kenpachi Zaraki | Kenpachi drenched in his own blood still standing | `drop/2-most-runs/ironclad/blood_wall.png` |
| Body Slam | ironclad | Kenpachi Zaraki | Kenpachi crashing shoulder-first into an opponent | `drop/2-most-runs/ironclad/body_slam.png` |
| Breakthrough | ironclad | Kenpachi Zaraki | Kenpachi breaking through a wall or barrier | `drop/2-most-runs/ironclad/breakthrough.png` |
| Cinder | ironclad | Kenpachi Zaraki | Kenpachi's reiatsu burning around him | `drop/2-most-runs/ironclad/cinder.png` |
| Havoc | ironclad | Squad 11 | Ikkaku and Yumichika brawling with Squad 11 | `drop/2-most-runs/ironclad/havoc.png` |
| Headbutt | ironclad | Kenpachi Zaraki | Kenpachi headbutting / close-range grin | `drop/2-most-runs/ironclad/headbutt.png` |
| Iron Wave | ironclad | Kenpachi Zaraki | Kenpachi's wide horizontal slash | `drop/2-most-runs/ironclad/iron_wave.png` |
| Molten Fist | ironclad | Kenpachi Zaraki | Kenpachi punching barehanded | `drop/2-most-runs/ironclad/molten_fist.png` |
| Perfected Strike | ironclad | Kenpachi Zaraki | Kenpachi's slash that splits the ground (vs Ichigo or Unohana) | `drop/2-most-runs/ironclad/perfected_strike.png` |
| Pommel Strike | ironclad | Kenpachi Zaraki | Kenpachi striking with the hilt | `drop/2-most-runs/ironclad/pommel_strike.png` |
| Setup Strike | ironclad | Kenpachi Zaraki | Kenpachi removing his eyepatch before attacking | `drop/2-most-runs/ironclad/setup_strike.png` |
| Shrug It Off | ironclad | Kenpachi Zaraki | Kenpachi laughing off a deep wound | `drop/2-most-runs/ironclad/shrug_it_off.png` |
| Sword Boomerang | ironclad | Kenpachi Zaraki | Kenpachi's sword spinning through the air | `drop/2-most-runs/ironclad/sword_boomerang.png` |
| Taunt | ironclad | Kenpachi Zaraki | Kenpachi beckoning an enemy with a wild grin | `drop/2-most-runs/ironclad/taunt.png` |
| Thunderclap | ironclad | Kenpachi Zaraki | Kenpachi's spiritual pressure shockwave cracking the ground | `drop/2-most-runs/ironclad/thunderclap.png` |
| Tremble | ironclad | Kenpachi Zaraki | An enemy trembling under Kenpachi's reiatsu | `drop/2-most-runs/ironclad/tremble.png` |
| True Grit | ironclad | Kenpachi Zaraki | Kenpachi with bandages and torn haori grinning | `drop/2-most-runs/ironclad/true_grit.png` |
| Twin Strike | ironclad | Kenpachi Zaraki | Kenpachi with Yachiru on his shoulder | `drop/2-most-runs/ironclad/twin_strike.png` |
| Anticipate | silent | Soi Fon | Soi Fon watching from the shadows | `drop/2-most-runs/silent/anticipate.png` |
| Backflip | silent | Soi Fon | Soi Fon flipping away mid-air | `drop/2-most-runs/silent/backflip.png` |
| Blade Dance | silent | Soi Fon | Onmitsukido squad members throwing kunai | `drop/2-most-runs/silent/blade_dance.png` |
| Cloak and Dagger | silent | Soi Fon | Soi Fon in her Onmitsukido hood holding a blade | `drop/2-most-runs/silent/cloak_and_dagger.png` |
| Dagger Spray | silent | Soi Fon | A spray of thrown kunai | `drop/2-most-runs/silent/dagger_spray.png` |
| Dagger Throw | silent | Soi Fon | Soi Fon throwing a single kunai | `drop/2-most-runs/silent/dagger_throw.png` |
| Deadly Poison | silent | Soi Fon | Suzumebachi's sting glowing | `drop/2-most-runs/silent/deadly_poison.png` |
| Deflect | silent | Soi Fon | Soi Fon parrying with her forearm | `drop/2-most-runs/silent/deflect.png` |
| Dodge and Roll | silent | Soi Fon | Soi Fon dodging with Shunpo | `drop/2-most-runs/silent/dodge_and_roll.png` |
| Flick-Flack | silent | Soi Fon | Soi Fon spinning kick | `drop/2-most-runs/silent/flick_flack.png` |
| Leading Strike | silent | Soi Fon | Soi Fon's first strike with Suzumebachi | `drop/2-most-runs/silent/leading_strike.png` |
| Piercing Wail | silent | Soi Fon | Soi Fon shouting her Shikai release | `drop/2-most-runs/silent/piercing_wail.png` |
| Poisoned Stab | silent | Soi Fon | Suzumebachi stabbing a target (Nigeki Kessatsu) | `drop/2-most-runs/silent/poisoned_stab.png` |
| Predator | silent | Soi Fon | Soi Fon stalking a target from above | `drop/2-most-runs/silent/predator.png` |
| Prepared | silent | Soi Fon | Soi Fon tying back her hair before a fight | `drop/2-most-runs/silent/prepared.png` |
| Ricochet | silent | Soi Fon | Kunai bouncing off a wall | `drop/2-most-runs/silent/ricochet.png` |
| Slice | silent | Soi Fon | Soi Fon's quick horizontal cut | `drop/2-most-runs/silent/slice.png` |
| Snakebite | silent | Soi Fon | Close-up of the stinger tip | `drop/2-most-runs/silent/snakebite.png` |
| Sucker Punch | silent | Soi Fon | Soi Fon's surprise hand-to-hand blow (Hakuda) | `drop/2-most-runs/silent/sucker_punch.png` |
| Untouchable | silent | Soi Fon | Soi Fon with Shunko lightning around her shoulders | `drop/2-most-runs/silent/untouchable.png` |
| Ball Lightning | defect | Kisuke Urahara | A crackling ball of kido lightning in Urahara's palm | `drop/2-most-runs/defect/ball_lightning.png` |
| Barrage | defect | Kisuke Urahara | Benihime's Nake (crimson blasts) firing in a volley | `drop/2-most-runs/defect/barrage.png` |
| Beam Cell | defect | Kisuke Urahara | Urahara's thin red energy beam from Benihime | `drop/2-most-runs/defect/beam_cell.png` |
| Boost Away | defect | Kisuke Urahara | Urahara leaping away with Shunpo | `drop/2-most-runs/defect/boost_away.png` |
| Charge Battery | defect | Kisuke Urahara | Urahara charging one of his inventions | `drop/2-most-runs/defect/charge_battery.png` |
| Claw | defect | Yoruichi Shihoin | Yoruichi's cat-form claw swipe | `drop/2-most-runs/defect/claw.png` |
| Cold Snap | defect | Kisuke Urahara | Urahara's ice-binding kido freezing an enemy | `drop/2-most-runs/defect/cold_snap.png` |
| Compile Driver | defect | Kisuke Urahara | Urahara typing at his lab console | `drop/2-most-runs/defect/compile_driver.png` |
| Coolheaded | defect | Kisuke Urahara | Urahara relaxed with his fan over his face | `drop/2-most-runs/defect/coolheaded.png` |
| Focused Strike | defect | Kisuke Urahara | Urahara's precise single thrust | `drop/2-most-runs/defect/focused_strike.png` |
| Go for the Eyes | defect | Kisuke Urahara | Urahara's sharp eyes peeking from under his hat brim | `drop/2-most-runs/defect/go_for_the_eyes.png` |
| Gunk Up | defect | Kisuke Urahara | Urahara's sticky trap gadget catching an enemy | `drop/2-most-runs/defect/gunk_up.png` |
| Hologram | defect | Kisuke Urahara | Urahara's decoy body (Keitai) left behind | `drop/2-most-runs/defect/hologram.png` |
| Hotfix | defect | Kisuke Urahara | Urahara patching up Ichigo after training | `drop/2-most-runs/defect/hotfix.png` |
| Leap | defect | Kisuke Urahara | Urahara jumping high above the Urahara Shop | `drop/2-most-runs/defect/leap.png` |
| Lightning Rod | defect | Kisuke Urahara | Urahara's cane pointing skyward in a storm | `drop/2-most-runs/defect/lightning_rod.png` |
| Momentum Strike | defect | Kisuke Urahara | Urahara rushing forward mid-slash | `drop/2-most-runs/defect/momentum_strike.png` |
| Sweeping Beam | defect | Kisuke Urahara | Benihime's wide crimson energy wave | `drop/2-most-runs/defect/sweeping_beam.png` |
| TURBO | defect | Kisuke Urahara | Urahara's Shunpo burst | `drop/2-most-runs/defect/turbo.png` |
| Uproar | defect | Urahara Shop | Jinta and Ururu causing chaos at the Urahara Shop | `drop/2-most-runs/defect/uproar.png` |
| Astral Pulse | regent | Byakuya Kuchiki | Senbonzakura petals pulsing outward | `drop/2-most-runs/regent/astral_pulse.png` |
| BEGONE! | regent | Byakuya Kuchiki | Byakuya dismissing an enemy with his back turned | `drop/2-most-runs/regent/begone.png` |
| Celestial Might | regent | Byakuya Kuchiki | Senbonzakura Kageyoshi's thousand blades rising | `drop/2-most-runs/regent/celestial_might.png` |
| Cloak of Stars | regent | Byakuya Kuchiki | Byakuya's scarf (Ginpaku Kazahana no Uzuginu) fluttering | `drop/2-most-runs/regent/cloak_of_stars.png` |
| Collision Course | regent | Byakuya Kuchiki | Byakuya clashing swords with Ichigo | `drop/2-most-runs/regent/collision_course.png` |
| Cosmic Indifference | regent | Byakuya Kuchiki | Byakuya's cold expressionless stare | `drop/2-most-runs/regent/cosmic_indifference.png` |
| Crescent Spear | regent | Byakuya Kuchiki | Byakuya's single-blade thrust (Senka) | `drop/2-most-runs/regent/crescent_spear.png` |
| Crush Under | regent | Byakuya Kuchiki | Senkei's walls of blades closing in | `drop/2-most-runs/regent/crush_under.png` |
| Gather Light | regent | Byakuya Kuchiki | Petals gathering into Byakuya's hand | `drop/2-most-runs/regent/gather_light.png` |
| Glitterstream | regent | Byakuya Kuchiki | A stream of shimmering pink petals | `drop/2-most-runs/regent/glitterstream.png` |
| Glow | regent | Byakuya Kuchiki | Byakuya's Shukei Hakuteiken white glow | `drop/2-most-runs/regent/glow.png` |
| Guiding Star | regent | Byakuya Kuchiki | Byakuya pointing his sword at an enemy | `drop/2-most-runs/regent/guiding_star.png` |
| Hidden Cache | regent | Byakuya Kuchiki | The Kuchiki manor and its gardens | `drop/2-most-runs/regent/hidden_cache.png` |
| Know Thy Place | regent | Byakuya Kuchiki | Byakuya looking down at a kneeling enemy | `drop/2-most-runs/regent/know_thy_place.png` |
| Patter | regent | Byakuya Kuchiki | Petals falling gently like rain | `drop/2-most-runs/regent/patter.png` |
| Photon Cut | regent | Byakuya Kuchiki | Byakurai lightning kido from his fingertip | `drop/2-most-runs/regent/photon_cut.png` |
| Refine Blade | regent | Byakuya Kuchiki | Byakuya holding Senbonzakura upright before release | `drop/2-most-runs/regent/refine_blade.png` |
| Solar Strike | regent | Byakuya Kuchiki | Byakuya's bright overhead slash | `drop/2-most-runs/regent/solar_strike.png` |
| Spoils of Battle | regent | Byakuya Kuchiki | Byakuya after victory sheathing his sword | `drop/2-most-runs/regent/spoils_of_battle.png` |
| Wrought in War | regent | Byakuya Kuchiki | Byakuya's Bankai blades forged into a single sword | `drop/2-most-runs/regent/wrought_in_war.png` |
| Afterlife | necrobinder | Mayuri Kurotsuchi | Mayuri reassembling himself after being destroyed | `drop/2-most-runs/necrobinder/afterlife.png` |
| Blight Strike | necrobinder | Mayuri Kurotsuchi | Ashisogi Jizo's paralysing poison cut | `drop/2-most-runs/necrobinder/blight_strike.png` |
| Defile | necrobinder | Mayuri Kurotsuchi | Mayuri experimenting on a captured specimen | `drop/2-most-runs/necrobinder/defile.png` |
| Defy | necrobinder | Mayuri Kurotsuchi | Mayuri sneering at an opponent (vs Szayelaporro) | `drop/2-most-runs/necrobinder/defy.png` |
| Drain Power | necrobinder | Mayuri Kurotsuchi | Mayuri's drug slowing an enemy's senses | `drop/2-most-runs/necrobinder/drain_power.png` |
| Fear | necrobinder | Mayuri Kurotsuchi | Mayuri's grinning mask face in shadow | `drop/2-most-runs/necrobinder/fear.png` |
| Flatten | necrobinder | Nemu Kurotsuchi | Nemu's crushing punch (vs Pernida) | `drop/2-most-runs/necrobinder/flatten.png` |
| Grave Warden | necrobinder | Nemu Kurotsuchi | Nemu waiting silently in the lab | `drop/2-most-runs/necrobinder/grave_warden.png` |
| Graveblast | necrobinder | Mayuri Kurotsuchi | Konjiki Ashisogi Jizo spraying poison | `drop/2-most-runs/necrobinder/graveblast.png` |
| Invoke | necrobinder | Mayuri Kurotsuchi | Mayuri calling out Bankai | `drop/2-most-runs/necrobinder/invoke.png` |
| Negative Pulse | necrobinder | Mayuri Kurotsuchi | Mayuri's lab equipment releasing a shockwave | `drop/2-most-runs/necrobinder/negative_pulse.png` |
| Poke | necrobinder | Nemu Kurotsuchi | Nemu poking at something with blank curiosity | `drop/2-most-runs/necrobinder/poke.png` |
| Pull Aggro | necrobinder | Nemu Kurotsuchi | Nemu drawing an enemy away from Mayuri | `drop/2-most-runs/necrobinder/pull_aggro.png` |
| Reap | necrobinder | Mayuri Kurotsuchi | Ashisogi Jizo's wide sweeping slash | `drop/2-most-runs/necrobinder/reap.png` |
| Reave | necrobinder | Mayuri Kurotsuchi | Mayuri's blade tearing through a target | `drop/2-most-runs/necrobinder/reave.png` |
| Scourge | necrobinder | Mayuri Kurotsuchi | Mayuri injecting an enemy | `drop/2-most-runs/necrobinder/scourge.png` |
| Sculpting Strike | necrobinder | Mayuri Kurotsuchi | Mayuri modifying his own body | `drop/2-most-runs/necrobinder/sculpting_strike.png` |
| Snap | necrobinder | Nemu Kurotsuchi | Nemu snapping an enemy's arm | `drop/2-most-runs/necrobinder/snap.png` |
| Sow | necrobinder | Mayuri Kurotsuchi | Mayuri planting a bomb or seed in a body | `drop/2-most-runs/necrobinder/sow.png` |
| Wisp | necrobinder | Nemu Kurotsuchi | Nemu's soul-like Gigai body glowing | `drop/2-most-runs/necrobinder/wisp.png` |

## Wave 3: often (uncommons) (230 cards)

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Ashen Strike | ironclad | Kenpachi Zaraki | Kenpachi's slash leaving a trail of dust and rubble | `drop/3-often/ironclad/ashen_strike.png` |
| Battle Trance | ironclad | Kenpachi Zaraki | Kenpachi grinning wide-eyed mid-fight | `drop/3-often/ironclad/battle_trance.png` |
| Bloodletting | ironclad | Kenpachi Zaraki | Kenpachi cutting his own arm in the Unohana fight | `drop/3-often/ironclad/bloodletting.png` |
| Bludgeon | ironclad | Kenpachi Zaraki | Kenpachi smashing down with Nozarashi's giant cleaver | `drop/3-often/ironclad/bludgeon.png` |
| Bully | ironclad | Kenpachi Zaraki | Kenpachi towering over a cowering Hollow | `drop/3-often/ironclad/bully.png` |
| Burning Pact | ironclad | Kenpachi Zaraki | Kenpachi's reiatsu blazing red during his Bankai | `drop/3-often/ironclad/burning_pact.png` |
| Colossus | ironclad | Kenpachi Zaraki | Kenpachi standing unmoved as giant enemies close in | `drop/3-often/ironclad/colossus.png` |
| Cruelty | ironclad | Kenpachi Zaraki | Kenpachi's evil grin covered in an enemy's blood | `drop/3-often/ironclad/cruelty.png` |
| Demonic Shield | ironclad | Kenpachi Zaraki | Kenpachi's skull-shaped spiritual pressure surrounding him | `drop/3-often/ironclad/demonic_shield.png` |
| Dismantle | ironclad | Kenpachi Zaraki | Kenpachi cutting Nnoitra's weapon apart | `drop/3-often/ironclad/dismantle.png` |
| Drum of Battle | ironclad | Kenpachi Zaraki | The bells in Kenpachi's hair ringing as he charges | `drop/3-often/ironclad/drum_of_battle.png` |
| Evil Eye | ironclad | Kenpachi Zaraki | Close-up of Kenpachi's single exposed eye | `drop/3-often/ironclad/evil_eye.png` |
| Expect a Fight | ironclad | Kenpachi Zaraki | Kenpachi walking into a battlefield with sword on shoulder | `drop/3-often/ironclad/expect_a_fight.png` |
| Feel No Pain | ironclad | Kenpachi Zaraki | Kenpachi impaled but still smiling | `drop/3-often/ironclad/feel_no_pain.png` |
| Fight Me! | ironclad | Kenpachi Zaraki | Kenpachi calling out Ichigo to fight | `drop/3-often/ironclad/fight_me.png` |
| Flame Barrier | ironclad | Kenpachi Zaraki | Kenpachi's reiatsu flaring like fire around him | `drop/3-often/ironclad/flame_barrier.png` |
| Forgotten Ritual | ironclad | Kenpachi Zaraki | Unohana teaching Kenpachi in the Muken prison | `drop/3-often/ironclad/forgotten_ritual.png` |
| Hemokinesis | ironclad | Kenpachi Zaraki | Kenpachi attacking while bleeding heavily | `drop/3-often/ironclad/hemokinesis.png` |
| Howl from Beyond | ironclad | Kenpachi Zaraki | Kenpachi's Bankai roar (monstrous red form) | `drop/3-often/ironclad/howl_from_beyond.png` |
| Infernal Blade | ironclad | Kenpachi Zaraki | Nozarashi released as a giant cleaver | `drop/3-often/ironclad/infernal_blade.png` |
| Inferno | ironclad | Kenpachi Zaraki | Kenpachi's Bankai red reiatsu engulfing everything | `drop/3-often/ironclad/inferno.png` |
| Inflame | ironclad | Kenpachi Zaraki | Kenpachi's spiritual pressure surging upward | `drop/3-often/ironclad/inflame.png` |
| Juggling | ironclad | Kenpachi Zaraki | Yachiru bouncing on Kenpachi's shoulders | `drop/3-often/ironclad/juggling.png` |
| Pillage | ironclad | Squad 11 | Squad 11 members raiding a battlefield | `drop/3-often/ironclad/pillage.png` |
| Rage | ironclad | Kenpachi Zaraki | Kenpachi furious after losing the eyepatch limiter | `drop/3-often/ironclad/rage.png` |
| Rampage | ironclad | Kenpachi Zaraki | Kenpachi hacking through a crowd of enemies | `drop/3-often/ironclad/rampage.png` |
| Rupture | ironclad | Kenpachi Zaraki | Kenpachi's wounds bursting open as his power rises | `drop/3-often/ironclad/rupture.png` |
| Second Wind | ironclad | Kenpachi Zaraki | Kenpachi getting back up after being cut down | `drop/3-often/ironclad/second_wind.png` |
| Spite | ironclad | Kenpachi Zaraki | Kenpachi vs Kaname Tosen (blinded and still swinging) | `drop/3-often/ironclad/spite.png` |
| Stampede | ironclad | Squad 11 | Squad 11 charging together | `drop/3-often/ironclad/stampede.png` |
| Stomp | ironclad | Kenpachi Zaraki | Kenpachi stamping a crater into the ground | `drop/3-often/ironclad/stomp.png` |
| Stone Armor | ironclad | Kenpachi Zaraki | A blade snapping on Kenpachi's skin | `drop/3-often/ironclad/stone_armor.png` |
| Unrelenting | ironclad | Kenpachi Zaraki | Kenpachi swinging over and over at Unohana | `drop/3-often/ironclad/unrelenting.png` |
| Uppercut | ironclad | Kenpachi Zaraki | Kenpachi's rising slash launching an enemy | `drop/3-often/ironclad/uppercut.png` |
| Vicious | ironclad | Kenpachi Zaraki | Kenpachi's bloodthirsty laugh | `drop/3-often/ironclad/vicious.png` |
| Whirlwind | ironclad | Kenpachi Zaraki | Kenpachi spinning with his sword in a full circle | `drop/3-often/ironclad/whirlwind.png` |
| Accelerant | silent | Soi Fon | Suzumebachi poison spreading through a target | `drop/3-often/silent/accelerant.png` |
| Accuracy | silent | Soi Fon | Soi Fon aiming her stinger at the butterfly mark | `drop/3-often/silent/accuracy.png` |
| Acrobatics | silent | Soi Fon | Soi Fon flipping between rooftops | `drop/3-often/silent/acrobatics.png` |
| Backstab | silent | Soi Fon | Soi Fon appearing behind an enemy with Shunpo | `drop/3-often/silent/backstab.png` |
| Blade Symphony | silent | Onmitsukido | Stealth Force squad attacking in formation | `drop/3-often/silent/blade_symphony.png` |
| Blur | silent | Soi Fon | Soi Fon as a blur of afterimages | `drop/3-often/silent/blur.png` |
| Bouncing Flask | silent | Marechiyo Omaeda | Omaeda's spiked flail (Gegetsuburi) bouncing | `drop/3-often/silent/bouncing_flask.png` |
| Bubble Bubble | silent | Marechiyo Omaeda | Omaeda blowing a bubble or eating snacks | `drop/3-often/silent/bubble_bubble.png` |
| Calculated Gamble | silent | Soi Fon | Soi Fon weighing whether to use Bankai | `drop/3-often/silent/calculated_gamble.png` |
| Concoct | silent | Soi Fon | Soi Fon mixing a poison in the Onmitsukido | `drop/3-often/silent/concoct.png` |
| Dash | silent | Soi Fon | Soi Fon dashing with Shunpo | `drop/3-often/silent/dash.png` |
| Echoing Slash | silent | Soi Fon | Soi Fon's afterimages all striking at once | `drop/3-often/silent/echoing_slash.png` |
| Escape Plan | silent | Soi Fon | Soi Fon vanishing in a puff of Shunpo | `drop/3-often/silent/escape_plan.png` |
| Expertise | silent | Yoruichi Shihoin | Yoruichi training young Soi Fon | `drop/3-often/silent/expertise.png` |
| Expose | silent | Soi Fon | Soi Fon tearing off her haori to reveal Shunko | `drop/3-often/silent/expose.png` |
| Fade | silent | Soi Fon | Soi Fon fading into shadow | `drop/3-often/silent/fade.png` |
| Finisher | silent | Soi Fon | Soi Fon's second sting on the butterfly mark (Nigeki Kessatsu) | `drop/3-often/silent/finisher.png` |
| Flechettes | silent | Soi Fon | A spread of small blades from Soi Fon's sleeve | `drop/3-often/silent/flechettes.png` |
| Footwork | silent | Soi Fon | Soi Fon's Shunpo footwork close-up | `drop/3-often/silent/footwork.png` |
| Hand Trick | silent | Soi Fon | Soi Fon's Hakuda hand strike | `drop/3-often/silent/hand_trick.png` |
| Haze | silent | Soi Fon | Soi Fon hidden in smoke | `drop/3-often/silent/haze.png` |
| Hidden Daggers | silent | Soi Fon | Kunai hidden in Soi Fon's sleeves | `drop/3-often/silent/hidden_daggers.png` |
| Infinite Blades | silent | Onmitsukido | Endless kunai raining down | `drop/3-often/silent/infinite_blades.png` |
| Leg Sweep | silent | Soi Fon | Soi Fon's low sweeping kick | `drop/3-often/silent/leg_sweep.png` |
| Memento Mori | silent | Soi Fon | The butterfly death mark (Homonka) | `drop/3-often/silent/memento_mori.png` |
| Mirage | silent | Soi Fon | Soi Fon's Utsusemi afterimage decoy | `drop/3-often/silent/mirage.png` |
| Noxious Fumes | silent | Soi Fon | Purple poison mist around Suzumebachi | `drop/3-often/silent/noxious_fumes.png` |
| Phantom Blades | silent | Soi Fon | Ghostly copies of Soi Fon's stinger | `drop/3-often/silent/phantom_blades.png` |
| Pinpoint | silent | Soi Fon | Soi Fon stabbing a precise pressure point | `drop/3-often/silent/pinpoint.png` |
| Pounce | silent | Soi Fon | Soi Fon leaping down onto an enemy | `drop/3-often/silent/pounce.png` |
| Precise Cut | silent | Soi Fon | Soi Fon's single clean cut | `drop/3-often/silent/precise_cut.png` |
| Reflex | silent | Soi Fon | Soi Fon catching a blade between her fingers | `drop/3-often/silent/reflex.png` |
| Skewer | silent | Soi Fon | Soi Fon piercing through an enemy | `drop/3-often/silent/skewer.png` |
| Speedster | silent | Soi Fon | Soi Fon's Shunpo speed lines | `drop/3-often/silent/speedster.png` |
| Strangle | silent | Soi Fon | Soi Fon pinning Ggio Vega | `drop/3-often/silent/strangle.png` |
| Tactician | silent | Soi Fon | Soi Fon giving Stealth Force orders | `drop/3-often/silent/tactician.png` |
| Up My Sleeve | silent | Soi Fon | Soi Fon hiding a blade in her sleeve | `drop/3-often/silent/up_my_sleeve.png` |
| Boot Sequence | defect | Kisuke Urahara | Urahara powering up a device in his underground training room | `drop/3-often/defect/boot_sequence.png` |
| Bulk Up | defect | Tessai Tsukabishi | Tessai flexing his huge arms | `drop/3-often/defect/bulk_up.png` |
| Capacitor | defect | Kisuke Urahara | Rows of glowing vials in Urahara's lab | `drop/3-often/defect/capacitor.png` |
| Chaos | defect | Kisuke Urahara | Urahara's lab exploding in a mess of gadgets | `drop/3-often/defect/chaos.png` |
| Chill | defect | Kisuke Urahara | Urahara sipping tea at the shop | `drop/3-often/defect/chill.png` |
| Compact | defect | Kisuke Urahara | Urahara's portable Gigai kit | `drop/3-often/defect/compact.png` |
| Darkness | defect | Kisuke Urahara | Urahara's shadowed face under his striped hat | `drop/3-often/defect/darkness.png` |
| Double Energy | defect | Kisuke Urahara | Urahara and Tessai combining kido | `drop/3-often/defect/double_energy.png` |
| Energy Surge | defect | Kisuke Urahara | Urahara's reiatsu flaring red | `drop/3-often/defect/energy_surge.png` |
| FTL | defect | Kisuke Urahara | Urahara vanishing with flash step | `drop/3-often/defect/ftl.png` |
| Feral | defect | Yoruichi Shihoin | Yoruichi's Shunko lightning form | `drop/3-often/defect/feral.png` |
| Fight Through | defect | Kisuke Urahara | Urahara pushing through Aizen's attack | `drop/3-often/defect/fight_through.png` |
| Fusion | defect | Kisuke Urahara | The Hogyoku (Urahara's invention) | `drop/3-often/defect/fusion.png` |
| Genetic Algorithm | defect | Kisuke Urahara | Urahara studying Hollowification research | `drop/3-often/defect/genetic_algorithm.png` |
| Glacier | defect | Kisuke Urahara | A wall of ice from a kido barrier | `drop/3-often/defect/glacier.png` |
| Glasswork | defect | Kisuke Urahara | Urahara's glass flasks and beakers | `drop/3-often/defect/glasswork.png` |
| Hailstorm | defect | Kisuke Urahara | Ice shards raining down around Urahara | `drop/3-often/defect/hailstorm.png` |
| Hibernate | defect | Kisuke Urahara | Urahara napping in the Urahara Shop | `drop/3-often/defect/hibernate.png` |
| Ignition | defect | Kisuke Urahara | Urahara igniting Benihime's crimson blast | `drop/3-often/defect/ignition.png` |
| Iteration | defect | Kisuke Urahara | Urahara testing a prototype again and again | `drop/3-often/defect/iteration.png` |
| Loop | defect | Kisuke Urahara | Benihime's net shield (Chikasumi no Tate) | `drop/3-often/defect/loop.png` |
| Null | defect | Kisuke Urahara | Urahara's sealing kido cancelling an attack | `drop/3-often/defect/null.png` |
| Overclock | defect | Kisuke Urahara | Urahara pushing a device past its limit | `drop/3-often/defect/overclock.png` |
| Refract | defect | Kisuke Urahara | Benihime's shield deflecting a blast | `drop/3-often/defect/refract.png` |
| Rocket Punch | defect | Tessai Tsukabishi | Tessai's massive punch | `drop/3-often/defect/rocket_punch.png` |
| Scavenge | defect | Kisuke Urahara | Urahara digging through junk in the shop storeroom | `drop/3-often/defect/scavenge.png` |
| Scrape | defect | Kisuke Urahara | Benihime scraping across an enemy blade | `drop/3-often/defect/scrape.png` |
| Shadow Shield | defect | Kisuke Urahara | Urahara's hooded cloak (Reishi-hiding cloak) | `drop/3-often/defect/shadow_shield.png` |
| Skim | defect | Kisuke Urahara | Urahara flipping through research notes | `drop/3-often/defect/skim.png` |
| Smokestack | defect | Kisuke Urahara | Smoke rising from the Urahara Shop | `drop/3-often/defect/smokestack.png` |
| Storm | defect | Kisuke Urahara | Urahara standing in a lightning storm | `drop/3-often/defect/storm.png` |
| Subroutine | defect | Kisuke Urahara | Urahara's pre-set kido trap activating | `drop/3-often/defect/subroutine.png` |
| Sunder | defect | Kisuke Urahara | Benihime Aratame (Bankai) cutting and re-stitching | `drop/3-often/defect/sunder.png` |
| Synchronize | defect | Kisuke Urahara | Urahara and Yoruichi fighting in sync | `drop/3-often/defect/synchronize.png` |
| Synthesis | defect | Kisuke Urahara | Urahara mixing compounds in his lab | `drop/3-often/defect/synthesis.png` |
| Tempest | defect | Kisuke Urahara | A whirlwind of crimson energy around Urahara | `drop/3-often/defect/tempest.png` |
| Tesla Coil | defect | Kisuke Urahara | Urahara's lightning device crackling | `drop/3-often/defect/tesla_coil.png` |
| Thunder | defect | Kisuke Urahara | A thunderbolt kido striking down | `drop/3-often/defect/thunder.png` |
| White Noise | defect | Kisuke Urahara | Urahara's communication device crackling with static | `drop/3-often/defect/white_noise.png` |
| Alignment | regent | Byakuya Kuchiki | Senbonzakura's blades lining up in neat rows | `drop/3-often/regent/alignment.png` |
| Black Hole | regent | Byakuya Kuchiki | A dark sphere of petals collapsing inward (Gokei) | `drop/3-often/regent/black_hole.png` |
| Bulwark | regent | Byakuya Kuchiki | A solid wall of Senbonzakura blades | `drop/3-often/regent/bulwark.png` |
| CHARGE!! | regent | Byakuya Kuchiki | Byakuya charging forward with Shunpo | `drop/3-often/regent/charge.png` |
| Child of the Stars | regent | Rukia Kuchiki | Rukia under the night sky | `drop/3-often/regent/child_of_the_stars.png` |
| Conqueror | regent | Byakuya Kuchiki | Byakuya standing victorious over Ichigo | `drop/3-often/regent/conqueror.png` |
| Constellation | regent | Byakuya Kuchiki | Petals scattered like stars in the night sky | `drop/3-often/regent/constellation.png` |
| Convergence | regent | Byakuya Kuchiki | All of Senbonzakura's blades converging on one point | `drop/3-often/regent/convergence.png` |
| Devastate | regent | Byakuya Kuchiki | Senbonzakura shredding an enemy | `drop/3-often/regent/devastate.png` |
| Furnace | regent | Byakuya Kuchiki | Byakuya's reiatsu glowing white-hot | `drop/3-often/regent/furnace.png` |
| Gamma Blast | regent | Byakuya Kuchiki | Hado 63 Raikoho lightning blast | `drop/3-often/regent/gamma_blast.png` |
| Glimmer | regent | Byakuya Kuchiki | Petals glinting in sunlight | `drop/3-often/regent/glimmer.png` |
| Hegemony | regent | Byakuya Kuchiki | Byakuya as head of the Kuchiki clan | `drop/3-often/regent/hegemony.png` |
| Kingly Kick | regent | Byakuya Kuchiki | Byakuya's swift Hakuda kick | `drop/3-often/regent/kingly_kick.png` |
| Kingly Punch | regent | Byakuya Kuchiki | Byakuya's open-palm strike | `drop/3-often/regent/kingly_punch.png` |
| Knockout Blow | regent | Byakuya Kuchiki | Byakuya knocking Renji down in one strike | `drop/3-often/regent/knockout_blow.png` |
| Largesse | regent | Kuchiki clan | Kuchiki clan servants presenting gifts | `drop/3-often/regent/largesse.png` |
| Lunar Blast | regent | Byakuya Kuchiki | Senbonzakura petals under a full moon | `drop/3-often/regent/lunar_blast.png` |
| Manifest Authority | regent | Byakuya Kuchiki | Byakuya's captain's haori and Kenseikan headpiece | `drop/3-often/regent/manifest_authority.png` |
| Monologue | regent | Byakuya Kuchiki | Byakuya explaining his pride to Ichigo | `drop/3-often/regent/monologue.png` |
| Orbit | regent | Byakuya Kuchiki | Petals circling around Byakuya | `drop/3-often/regent/orbit.png` |
| Pale Blue Dot | regent | Byakuya Kuchiki | A single petal against a vast sky | `drop/3-often/regent/pale_blue_dot.png` |
| Parry | regent | Byakuya Kuchiki | Byakuya blocking with two fingers | `drop/3-often/regent/parry.png` |
| Particle Wall | regent | Byakuya Kuchiki | Danku kido barrier | `drop/3-often/regent/particle_wall.png` |
| Pillar of Creation | regent | Byakuya Kuchiki | A tower of rising blades | `drop/3-often/regent/pillar_of_creation.png` |
| Plot | regent | Byakuya Kuchiki | Byakuya quietly planning at his desk | `drop/3-often/regent/plot.png` |
| Prophesize | regent | Byakuya Kuchiki | Byakuya foreseeing his opponent's move | `drop/3-often/regent/prophesize.png` |
| Quasar | regent | Byakuya Kuchiki | A blinding burst of white petals | `drop/3-often/regent/quasar.png` |
| Radiate | regent | Byakuya Kuchiki | Petals radiating out in every direction | `drop/3-often/regent/radiate.png` |
| Reflect | regent | Byakuya Kuchiki | Byakuya's reflection in a still pond at the manor | `drop/3-often/regent/reflect.png` |
| Reserves | regent | Byakuya Kuchiki | Senbonzakura blades waiting in formation | `drop/3-often/regent/reserves.png` |
| Resonance | regent | Byakuya Kuchiki | Byakuya and Senbonzakura's spirit side by side | `drop/3-often/regent/resonance.png` |
| Royal Gamble | regent | Byakuya Kuchiki | Byakuya choosing between law and Rukia | `drop/3-often/regent/royal_gamble.png` |
| Shining Strike | regent | Byakuya Kuchiki | Byakuya's glowing sword cutting through | `drop/3-often/regent/shining_strike.png` |
| Spectrum Shift | regent | Byakuya Kuchiki | Petals changing colour as they scatter | `drop/3-often/regent/spectrum_shift.png` |
| Stardust | regent | Byakuya Kuchiki | Petals dissolving into glittering dust | `drop/3-often/regent/stardust.png` |
| Summon Forth | regent | Byakuya Kuchiki | Senbonzakura Kageyoshi's thousand swords rising from the ground | `drop/3-often/regent/summon_forth.png` |
| Supermassive | regent | Byakuya Kuchiki | A giant mass of petals crushing down | `drop/3-often/regent/supermassive.png` |
| Terraforming | regent | Byakuya Kuchiki | Byakuya's Bankai inner world of endless swords | `drop/3-often/regent/terraforming.png` |
| Bone Shards | necrobinder | Mayuri Kurotsuchi | Shards of a broken specimen flying apart | `drop/3-often/necrobinder/bone_shards.png` |
| Borrowed Time | necrobinder | Mayuri Kurotsuchi | Mayuri's Superhuman Drug slowing time to a crawl (vs Szayelaporro) | `drop/3-often/necrobinder/borrowed_time.png` |
| Bury | necrobinder | Mayuri Kurotsuchi | Mayuri burying a specimen in his lab | `drop/3-often/necrobinder/bury.png` |
| Calcify | necrobinder | Mayuri Kurotsuchi | An enemy frozen stiff by Ashisogi Jizo's paralysis | `drop/3-often/necrobinder/calcify.png` |
| Capture Spirit | necrobinder | Mayuri Kurotsuchi | Mayuri sealing a soul in a specimen jar | `drop/3-often/necrobinder/capture_spirit.png` |
| Cleanse | necrobinder | Mayuri Kurotsuchi | Mayuri taking an antidote | `drop/3-often/necrobinder/cleanse.png` |
| Countdown | necrobinder | Mayuri Kurotsuchi | Mayuri's bomb timer ticking | `drop/3-often/necrobinder/countdown.png` |
| Danse Macabre | necrobinder | Mayuri Kurotsuchi | Mayuri's reanimated Arrancar soldiers (Cirucci and Dordoni) | `drop/3-often/necrobinder/danse_macabre.png` |
| Death March | necrobinder | Mayuri Kurotsuchi | Zombie Arrancar marching for Mayuri | `drop/3-often/necrobinder/death_march.png` |
| Death's Door | necrobinder | Mayuri Kurotsuchi | Mayuri at the gate of his lab | `drop/3-often/necrobinder/deaths_door.png` |
| Deathbringer | necrobinder | Mayuri Kurotsuchi | Mayuri raising Ashisogi Jizo | `drop/3-often/necrobinder/deathbringer.png` |
| Debilitate | necrobinder | Mayuri Kurotsuchi | An enemy's limbs paralysed by poison | `drop/3-often/necrobinder/debilitate.png` |
| Delay | necrobinder | Mayuri Kurotsuchi | Mayuri's drug freezing an enemy's perception | `drop/3-often/necrobinder/delay.png` |
| Dirge | necrobinder | Mayuri Kurotsuchi | Mayuri humming over a fallen enemy | `drop/3-often/necrobinder/dirge.png` |
| Dredge | necrobinder | Mayuri Kurotsuchi | Mayuri pulling something out of a vat | `drop/3-often/necrobinder/dredge.png` |
| Enfeebling Touch | necrobinder | Mayuri Kurotsuchi | Mayuri's fingertip touch injecting poison | `drop/3-often/necrobinder/enfeebling_touch.png` |
| Fetch | necrobinder | Nemu Kurotsuchi | Nemu bringing Mayuri a tool | `drop/3-often/necrobinder/fetch.png` |
| Friendship | necrobinder | Nemu Kurotsuchi | Nemu standing loyally at Mayuri's side | `drop/3-often/necrobinder/friendship.png` |
| Haunt | necrobinder | Nemu Kurotsuchi | Nemu's ghostly pale figure in the dark lab | `drop/3-often/necrobinder/haunt.png` |
| High Five | necrobinder | Nemu Kurotsuchi | Nemu raising a hand to strike | `drop/3-often/necrobinder/high_five.png` |
| Legion of Bone | necrobinder | Mayuri Kurotsuchi | Mayuri's army of reanimated Arrancar | `drop/3-often/necrobinder/legion_of_bone.png` |
| Lethality | necrobinder | Mayuri Kurotsuchi | Ashisogi Jizo's blade dripping poison | `drop/3-often/necrobinder/lethality.png` |
| Melancholy | necrobinder | Nemu Kurotsuchi | Nemu's sad quiet expression | `drop/3-often/necrobinder/melancholy.png` |
| No Escape | necrobinder | Mayuri Kurotsuchi | Konjiki Ashisogi Jizo blocking an enemy's escape | `drop/3-often/necrobinder/no_escape.png` |
| Pagestorm | necrobinder | Mayuri Kurotsuchi | Mayuri's research notes flying everywhere | `drop/3-often/necrobinder/pagestorm.png` |
| Parse | necrobinder | Mayuri Kurotsuchi | Mayuri analysing data on his monitors | `drop/3-often/necrobinder/parse.png` |
| Pull from Below | necrobinder | Konjiki Ashisogi Jizo | Mayuri's Bankai rising out of the ground | `drop/3-often/necrobinder/pull_from_below.png` |
| Putrefy | necrobinder | Mayuri Kurotsuchi | An enemy melting from Mayuri's poison | `drop/3-often/necrobinder/putrefy.png` |
| Rattle | necrobinder | Mayuri Kurotsuchi | Mayuri shaking a test tube | `drop/3-often/necrobinder/rattle.png` |
| Right Hand Hand | necrobinder | Nemu Kurotsuchi | Nemu's punch with her right hand | `drop/3-often/necrobinder/right_hand_hand.png` |
| Scavenge | necrobinder | Mayuri Kurotsuchi | Mayuri collecting samples from a battlefield | `drop/3-often/necrobinder/scavenge.png` |
| Severance | necrobinder | Mayuri Kurotsuchi | Mayuri cutting off his own arm to escape | `drop/3-often/necrobinder/severance.png` |
| Shroud | necrobinder | Mayuri Kurotsuchi | Mayuri's cloak and mask in shadow | `drop/3-often/necrobinder/shroud.png` |
| Sic 'Em | necrobinder | Nemu Kurotsuchi | Mayuri ordering Nemu to attack | `drop/3-often/necrobinder/sic_em.png` |
| Sleight of Flesh | necrobinder | Mayuri Kurotsuchi | Mayuri stretching his body in strange ways | `drop/3-often/necrobinder/sleight_of_flesh.png` |
| Soulbound | necrobinder | Nemu Kurotsuchi | Nemu bound to Mayuri's commands | `drop/3-often/necrobinder/soulbound.png` |
| Spur | necrobinder | Mayuri Kurotsuchi | Mayuri injecting Nemu with a drug | `drop/3-often/necrobinder/spur.png` |
| Underworld | necrobinder | Mayuri Kurotsuchi | Squad 12's underground lab | `drop/3-often/necrobinder/underworld.png` |
| Veilpiercer | necrobinder | Mayuri Kurotsuchi | Ashisogi Jizo piercing through a barrier | `drop/3-often/necrobinder/veilpiercer.png` |
| Automation | colorless |  | _suggestion coming_ | `drop/3-often/colorless/automation.png` |
| Believe in You | colorless |  | _suggestion coming_ | `drop/3-often/colorless/believe_in_you.png` |
| Catastrophe | colorless |  | _suggestion coming_ | `drop/3-often/colorless/catastrophe.png` |
| Coordinate | colorless |  | _suggestion coming_ | `drop/3-often/colorless/coordinate.png` |
| Dark Shackles | colorless |  | _suggestion coming_ | `drop/3-often/colorless/dark_shackles.png` |
| Discovery | colorless |  | _suggestion coming_ | `drop/3-often/colorless/discovery.png` |
| Dramatic Entrance | colorless |  | _suggestion coming_ | `drop/3-often/colorless/dramatic_entrance.png` |
| Equilibrium | colorless |  | _suggestion coming_ | `drop/3-often/colorless/equilibrium.png` |
| Fasten | colorless |  | _suggestion coming_ | `drop/3-often/colorless/fasten.png` |
| Finesse | colorless |  | _suggestion coming_ | `drop/3-often/colorless/finesse.png` |
| Fisticuffs | colorless |  | _suggestion coming_ | `drop/3-often/colorless/fisticuffs.png` |
| Flash of Steel | colorless |  | _suggestion coming_ | `drop/3-often/colorless/flash_of_steel.png` |
| Gang Up | colorless |  | _suggestion coming_ | `drop/3-often/colorless/gang_up.png` |
| Huddle Up | colorless |  | _suggestion coming_ | `drop/3-often/colorless/huddle_up.png` |
| Impatience | colorless |  | _suggestion coming_ | `drop/3-often/colorless/impatience.png` |
| Intercept | colorless |  | _suggestion coming_ | `drop/3-often/colorless/intercept.png` |
| Jack of All Trades | colorless |  | _suggestion coming_ | `drop/3-often/colorless/jack_of_all_trades.png` |
| Lift | colorless |  | _suggestion coming_ | `drop/3-often/colorless/lift.png` |
| Mind Blast | colorless |  | _suggestion coming_ | `drop/3-often/colorless/mind_blast.png` |
| Omnislice | colorless |  | _suggestion coming_ | `drop/3-often/colorless/omnislice.png` |
| Panache | colorless |  | _suggestion coming_ | `drop/3-often/colorless/panache.png` |
| Panic Button | colorless |  | _suggestion coming_ | `drop/3-often/colorless/panic_button.png` |
| Prep Time | colorless |  | _suggestion coming_ | `drop/3-often/colorless/prep_time.png` |
| Production | colorless |  | _suggestion coming_ | `drop/3-often/colorless/production.png` |
| Prolong | colorless |  | _suggestion coming_ | `drop/3-often/colorless/prolong.png` |
| Prowess | colorless |  | _suggestion coming_ | `drop/3-often/colorless/prowess.png` |
| Purity | colorless |  | _suggestion coming_ | `drop/3-often/colorless/purity.png` |
| Restlessness | colorless |  | _suggestion coming_ | `drop/3-often/colorless/restlessness.png` |
| Salvo | colorless |  | _suggestion coming_ | `drop/3-often/colorless/salvo.png` |
| Seeker Strike | colorless |  | _suggestion coming_ | `drop/3-often/colorless/seeker_strike.png` |
| Shockwave | colorless |  | _suggestion coming_ | `drop/3-often/colorless/shockwave.png` |
| Stratagem | colorless |  | _suggestion coming_ | `drop/3-often/colorless/stratagem.png` |
| Tag Team | colorless |  | _suggestion coming_ | `drop/3-often/colorless/tag_team.png` |
| The Ball | colorless |  | _suggestion coming_ | `drop/3-often/colorless/the_ball.png` |
| The Bomb | colorless |  | _suggestion coming_ | `drop/3-often/colorless/the_bomb.png` |
| Thinking Ahead | colorless |  | _suggestion coming_ | `drop/3-often/colorless/thinking_ahead.png` |
| Thrumming Hatchet | colorless |  | _suggestion coming_ | `drop/3-often/colorless/thrumming_hatchet.png` |
| Ultimate Defend | colorless |  | _suggestion coming_ | `drop/3-often/colorless/ultimate_defend.png` |
| Ultimate Strike | colorless |  | _suggestion coming_ | `drop/3-often/colorless/ultimate_strike.png` |
| Volley | colorless |  | _suggestion coming_ | `drop/3-often/colorless/volley.png` |

## Wave 4: sometimes (rares, curses, tokens) (188 cards)

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Aggression | ironclad | Kenpachi Zaraki | Kenpachi lunging forward with both hands on the hilt | `drop/4-sometimes/ironclad/aggression.png` |
| Barricade | ironclad | Kenpachi Zaraki | Kenpachi blocking Nnoitra's scythe with his bare hand | `drop/4-sometimes/ironclad/barricade.png` |
| Brand | ironclad | Kenpachi Zaraki | The scar across Kenpachi's face from Ichigo | `drop/4-sometimes/ironclad/brand.png` |
| Cascade | ironclad | Kenpachi Zaraki | A flurry of Kenpachi slashes | `drop/4-sometimes/ironclad/cascade.png` |
| Conflagration | ironclad | Kenpachi Zaraki | Kenpachi's Bankai red aura exploding outward | `drop/4-sometimes/ironclad/conflagration.png` |
| Crimson Mantle | ironclad | Kenpachi Zaraki | Kenpachi soaked red in his Bankai form | `drop/4-sometimes/ironclad/crimson_mantle.png` |
| Dark Embrace | ironclad | Yumichika Ayasegawa | Ruri'iro Kujaku's vines draining spiritual pressure | `drop/4-sometimes/ironclad/dark_embrace.png` |
| Demon Form | ironclad | Kenpachi Zaraki | Kenpachi's Bankai monstrous form with horns | `drop/4-sometimes/ironclad/demon_form.png` |
| Dominate | ironclad | Kenpachi Zaraki | Kenpachi standing over a defeated Espada | `drop/4-sometimes/ironclad/dominate.png` |
| Feed | ironclad | Yumichika Ayasegawa | Ruri'iro Kujaku's flowers blooming on a drained enemy | `drop/4-sometimes/ironclad/feed.png` |
| Fiend Fire | ironclad | Kenpachi Zaraki | Kenpachi's Bankai slash setting the sky red | `drop/4-sometimes/ironclad/fiend_fire.png` |
| Hellraiser | ironclad | Kenpachi Zaraki | Kenpachi and Unohana's battle in the underground prison | `drop/4-sometimes/ironclad/hellraiser.png` |
| Impervious | ironclad | Kenpachi Zaraki | Kenpachi untouched by a barrage of attacks | `drop/4-sometimes/ironclad/impervious.png` |
| Juggernaut | ironclad | Kenpachi Zaraki | Kenpachi walking unstoppable through enemies | `drop/4-sometimes/ironclad/juggernaut.png` |
| Mangle | ironclad | Kenpachi Zaraki | Kenpachi's brutal cut tearing an enemy open | `drop/4-sometimes/ironclad/mangle.png` |
| Midnight | ironclad | Kenpachi Zaraki | Kenpachi silhouetted against the night sky | `drop/4-sometimes/ironclad/midnight.png` |
| Not Yet | ironclad | Kenpachi Zaraki | Kenpachi refusing to fall after being stabbed by Unohana | `drop/4-sometimes/ironclad/not_yet.png` |
| Offering | ironclad | Retsu Unohana | Unohana's final moment passing her title to Kenpachi | `drop/4-sometimes/ironclad/offering.png` |
| One-Two Punch | ironclad | Ikkaku Madarame | Ikkaku striking with Hozukimaru's spear and sheath | `drop/4-sometimes/ironclad/one_two_punch.png` |
| Pact's End | ironclad | Retsu Unohana | Unohana and Kenpachi's last clash | `drop/4-sometimes/ironclad/pacts_end.png` |
| Primal Force | ironclad | Kenpachi Zaraki | Kenpachi fighting like a beast with bare hands | `drop/4-sometimes/ironclad/primal_force.png` |
| Pyre | ironclad | Kenpachi Zaraki | Kenpachi standing in burning ruins | `drop/4-sometimes/ironclad/pyre.png` |
| Stoke | ironclad | Kenpachi Zaraki | Kenpachi cracking his neck before a fight | `drop/4-sometimes/ironclad/stoke.png` |
| Tank | ironclad | Kenpachi Zaraki | Kenpachi absorbing a direct Cero blast | `drop/4-sometimes/ironclad/tank.png` |
| Tear Asunder | ironclad | Kenpachi Zaraki | Kenpachi cutting Gremmy's giant meteor in two | `drop/4-sometimes/ironclad/tear_asunder.png` |
| Thrash | ironclad | Kenpachi Zaraki | Kenpachi slamming an opponent into the ground | `drop/4-sometimes/ironclad/thrash.png` |
| Unmovable | ironclad | Kenpachi Zaraki | Kenpachi refusing to step back from Nnoitra | `drop/4-sometimes/ironclad/unmovable.png` |
| Abrasive | silent | Soi Fon | Soi Fon's Shunko wind cutting the ground | `drop/4-sometimes/silent/abrasive.png` |
| Adrenaline | silent | Soi Fon | Soi Fon at full Shunko power | `drop/4-sometimes/silent/adrenaline.png` |
| Afterimage | silent | Soi Fon | Soi Fon leaving afterimages around Barragan | `drop/4-sometimes/silent/afterimage.png` |
| Assassinate | silent | Soi Fon | Soi Fon killing in one sting | `drop/4-sometimes/silent/assassinate.png` |
| Blade of Ink | silent | Soi Fon | A black kunai cutting through the dark | `drop/4-sometimes/silent/blade_of_ink.png` |
| Bullet Time | silent | Soi Fon | Soi Fon moving while everything else freezes | `drop/4-sometimes/silent/bullet_time.png` |
| Burst | silent | Soi Fon | Soi Fon's Shunko explosion of energy | `drop/4-sometimes/silent/burst.png` |
| Corrosive Wave | silent | Soi Fon | Barragan's decay wave hitting Soi Fon | `drop/4-sometimes/silent/corrosive_wave.png` |
| Envenom | silent | Soi Fon | Suzumebachi's golden stinger dripping poison | `drop/4-sometimes/silent/envenom.png` |
| Fan of Knives | silent | Onmitsukido | A fan of kunai thrown at once | `drop/4-sometimes/silent/fan_of_knives.png` |
| Flanking | silent | Soi Fon | Soi Fon and Yoruichi attacking from both sides | `drop/4-sometimes/silent/flanking.png` |
| Grand Finale | silent | Soi Fon | Jakuho Raikoben (Soi Fon's missile Bankai) firing | `drop/4-sometimes/silent/grand_finale.png` |
| Knife Trap | silent | Onmitsukido | Kunai traps set around a hideout | `drop/4-sometimes/silent/knife_trap.png` |
| Malaise | silent | Soi Fon | An enemy collapsing from Suzumebachi poison | `drop/4-sometimes/silent/malaise.png` |
| Master Planner | silent | Soi Fon | Soi Fon studying a battle map | `drop/4-sometimes/silent/master_planner.png` |
| Murder | silent | Soi Fon | Soi Fon finishing an enemy with Nigeki Kessatsu | `drop/4-sometimes/silent/murder.png` |
| Nightmare | silent | Soi Fon | Soi Fon's cold stare in the dark | `drop/4-sometimes/silent/nightmare.png` |
| Outbreak | silent | Soi Fon | Poison spreading across many butterfly marks | `drop/4-sometimes/silent/outbreak.png` |
| Serpent Form | silent | Soi Fon | Soi Fon coiled to strike | `drop/4-sometimes/silent/serpent_form.png` |
| Shadow Step | silent | Soi Fon | Soi Fon stepping out of a shadow | `drop/4-sometimes/silent/shadow_step.png` |
| Shadowmeld | silent | Soi Fon | Soi Fon blending into the darkness | `drop/4-sometimes/silent/shadowmeld.png` |
| Sneaky | silent | Soi Fon | Soi Fon sneaking past guards | `drop/4-sometimes/silent/sneaky.png` |
| Storm of Steel | silent | Onmitsukido | A storm of thrown blades | `drop/4-sometimes/silent/storm_of_steel.png` |
| The Gambit | silent | Soi Fon | Soi Fon using her Bankai at point-blank range | `drop/4-sometimes/silent/the_gambit.png` |
| The Hunt | silent | Soi Fon | Soi Fon hunting a fleeing enemy | `drop/4-sometimes/silent/the_hunt.png` |
| Tools of the Trade | silent | Onmitsukido | Stealth Force gear laid out | `drop/4-sometimes/silent/tools_of_the_trade.png` |
| Tracking | silent | Soi Fon | Soi Fon following a trail of spiritual pressure | `drop/4-sometimes/silent/tracking.png` |
| Well-Laid Plans | silent | Soi Fon | Soi Fon and Yoruichi planning together | `drop/4-sometimes/silent/well_laid_plans.png` |
| Adaptive Strike | defect | Kisuke Urahara | Urahara switching tactics mid-fight | `drop/4-sometimes/defect/adaptive_strike.png` |
| All for One | defect | Urahara Shop | Urahara with Tessai Jinta and Ururu together | `drop/4-sometimes/defect/all_for_one.png` |
| Buffer | defect | Kisuke Urahara | Urahara's layered kido barriers | `drop/4-sometimes/defect/buffer.png` |
| Consuming Shadow | defect | Kisuke Urahara | Urahara vanishing into darkness | `drop/4-sometimes/defect/consuming_shadow.png` |
| Coolant | defect | Kisuke Urahara | Urahara's ice-cold calm under pressure | `drop/4-sometimes/defect/coolant.png` |
| Creative AI | defect | Kisuke Urahara | Urahara as the founding head of the Shinigami Research Institute | `drop/4-sometimes/defect/creative_ai.png` |
| Defragment | defect | Kisuke Urahara | Urahara reorganising his chaotic lab | `drop/4-sometimes/defect/defragment.png` |
| Echo Form | defect | Kisuke Urahara | Urahara's multiple decoy bodies | `drop/4-sometimes/defect/echo_form.png` |
| Flak Cannon | defect | Kisuke Urahara | Urahara firing explosive kido shells | `drop/4-sometimes/defect/flak_cannon.png` |
| Helix Drill | defect | Kisuke Urahara | Benihime's spiralling crimson blast | `drop/4-sometimes/defect/helix_drill.png` |
| Hyperbeam | defect | Kisuke Urahara | Benihime's full-power Nake blast | `drop/4-sometimes/defect/hyperbeam.png` |
| Ice Lance | defect | Kisuke Urahara | An ice spear from a binding kido | `drop/4-sometimes/defect/ice_lance.png` |
| Imitation Learning | defect | Kisuke Urahara | Urahara copying an enemy's technique | `drop/4-sometimes/defect/imitation_learning.png` |
| Machine Learning | defect | Kisuke Urahara | Urahara's lab full of experiments | `drop/4-sometimes/defect/machine_learning.png` |
| Meteor Strike | defect | Kisuke Urahara | Urahara's falling kido strike from above | `drop/4-sometimes/defect/meteor_strike.png` |
| Modded | defect | Kisuke Urahara | Urahara's modified soul candy | `drop/4-sometimes/defect/modded.png` |
| Multi-Cast | defect | Kisuke Urahara | Urahara casting chained kido spells | `drop/4-sometimes/defect/multi_cast.png` |
| One for All | defect | Kisuke Urahara | Urahara leading Ichigo's friends into Hueco Mundo | `drop/4-sometimes/defect/one_for_all.png` |
| Rainbow | defect | Kisuke Urahara | Benihime's colourful kido sparks | `drop/4-sometimes/defect/rainbow.png` |
| Reboot | defect | Kisuke Urahara | Urahara reviving himself in a spare body | `drop/4-sometimes/defect/reboot.png` |
| Shatter | defect | Kisuke Urahara | Benihime shattering Aizen's sword | `drop/4-sometimes/defect/shatter.png` |
| Signal Boost | defect | Kisuke Urahara | Urahara amplifying a signal from his device | `drop/4-sometimes/defect/signal_boost.png` |
| Spinner | defect | Kisuke Urahara | Urahara spinning his cane | `drop/4-sometimes/defect/spinner.png` |
| Supercritical | defect | Kisuke Urahara | Urahara's Bankai Kannonbiraki Benihime Aratame at full power | `drop/4-sometimes/defect/supercritical.png` |
| Trash to Treasure | defect | Urahara Shop | Junk items on the Urahara Shop shelves | `drop/4-sometimes/defect/trash_to_treasure.png` |
| Voltaic | defect | Kisuke Urahara | Urahara's body charged with lightning kido | `drop/4-sometimes/defect/voltaic.png` |
| Arsenal | regent | Byakuya Kuchiki | Senkei: rows of a thousand swords around Byakuya | `drop/4-sometimes/regent/arsenal.png` |
| Beat into Shape | regent | Byakuya Kuchiki | Byakuya training Rukia | `drop/4-sometimes/regent/beat_into_shape.png` |
| Big Bang | regent | Byakuya Kuchiki | Senbonzakura exploding outward in every direction | `drop/4-sometimes/regent/big_bang.png` |
| Bombardment | regent | Byakuya Kuchiki | A barrage of blades raining down | `drop/4-sometimes/regent/bombardment.png` |
| Bundle of Joy | regent | Rukia Kuchiki | Rukia smiling with Chappy | `drop/4-sometimes/regent/bundle_of_joy.png` |
| Comet | regent | Byakuya Kuchiki | A streak of petals across the sky | `drop/4-sometimes/regent/comet.png` |
| Crash Landing | regent | Byakuya Kuchiki | Byakuya landing in a cloud of petals | `drop/4-sometimes/regent/crash_landing.png` |
| Decisions, Decisions | regent | Byakuya Kuchiki | Byakuya at Hisana's grave | `drop/4-sometimes/regent/decisions_decisions.png` |
| Dying Star | regent | Byakuya Kuchiki | Byakuya badly hurt after the Quincy invasion | `drop/4-sometimes/regent/dying_star.png` |
| Foregone Conclusion | regent | Byakuya Kuchiki | Byakuya turning his back as an enemy falls | `drop/4-sometimes/regent/foregone_conclusion.png` |
| GUARDS!!! | regent | Kuchiki clan | Kuchiki clan guards at the manor gate | `drop/4-sometimes/regent/guards.png` |
| Genesis | regent | Byakuya Kuchiki | Byakuya first releasing his Bankai | `drop/4-sometimes/regent/genesis.png` |
| Hammer Time | regent | Byakuya Kuchiki | Byakuya's sword hilt striking down | `drop/4-sometimes/regent/hammer_time.png` |
| Heavenly Drill | regent | Byakuya Kuchiki | A spiral of petals drilling forward | `drop/4-sometimes/regent/heavenly_drill.png` |
| Heirloom Hammer | regent | Kuchiki clan | The Kenseikan headpiece (Kuchiki family heirloom) | `drop/4-sometimes/regent/heirloom_hammer.png` |
| I Am Invincible | regent | Byakuya Kuchiki | Byakuya untouched in a storm of petals | `drop/4-sometimes/regent/i_am_invincible.png` |
| Make It So | regent | Byakuya Kuchiki | Byakuya giving a quiet order | `drop/4-sometimes/regent/make_it_so.png` |
| Monarch's Gaze | regent | Byakuya Kuchiki | Byakuya's cold downward glance | `drop/4-sometimes/regent/monarchs_gaze.png` |
| Neutron Aegis | regent | Byakuya Kuchiki | A dense shield of compressed petals | `drop/4-sometimes/regent/neutron_aegis.png` |
| Royalties | regent | Kuchiki clan | The Kuchiki manor's grand hall | `drop/4-sometimes/regent/royalties.png` |
| Seeking Edge | regent | Byakuya Kuchiki | Petals hunting down a fleeing enemy | `drop/4-sometimes/regent/seeking_edge.png` |
| Seven Stars | regent | Byakuya Kuchiki | Seven blades of light around Byakuya | `drop/4-sometimes/regent/seven_stars.png` |
| Sword Sage | regent | Byakuya Kuchiki | Byakuya teaching swordsmanship | `drop/4-sometimes/regent/sword_sage.png` |
| The Smith | regent | Byakuya Kuchiki | Senbonzakura's spirit (the armoured samurai) | `drop/4-sometimes/regent/the_smith.png` |
| Tutor | regent | Byakuya Kuchiki | Byakuya training with Yoruichi as a boy | `drop/4-sometimes/regent/tutor.png` |
| Tyranny | regent | Byakuya Kuchiki | Byakuya enforcing Soul Society's law | `drop/4-sometimes/regent/tyranny.png` |
| Void Form | regent | Byakuya Kuchiki | Byakuya's Bankai Shukei Hakuteiken (white winged form) | `drop/4-sometimes/regent/void_form.png` |
| Banshee's Cry | necrobinder | Konjiki Ashisogi Jizo | The Bankai's baby face screaming | `drop/4-sometimes/necrobinder/banshees_cry.png` |
| Cacophony | necrobinder | Mayuri Kurotsuchi | Alarms blaring in the lab | `drop/4-sometimes/necrobinder/cacophony.png` |
| Call of the Void | necrobinder | Mayuri Kurotsuchi | Mayuri staring into a Garganta | `drop/4-sometimes/necrobinder/call_of_the_void.png` |
| Demesne | necrobinder | Mayuri Kurotsuchi | Mayuri in the middle of his lab | `drop/4-sometimes/necrobinder/demesne.png` |
| Devour Life | necrobinder | Nemu Kurotsuchi | Nemu absorbing Pernida's nerves | `drop/4-sometimes/necrobinder/devour_life.png` |
| Eidolon | necrobinder | Nemu Kurotsuchi | Nemu Eighth (Nemuri Hachigo) as a newborn copy | `drop/4-sometimes/necrobinder/eidolon.png` |
| End of Days | necrobinder | Konjiki Ashisogi Jizo | Mayuri's Bankai looming over a ruined battlefield | `drop/4-sometimes/necrobinder/end_of_days.png` |
| Eradicate | necrobinder | Mayuri Kurotsuchi | Mayuri dissolving an enemy completely | `drop/4-sometimes/necrobinder/eradicate.png` |
| Glimpse Beyond | necrobinder | Mayuri Kurotsuchi | Mayuri peering into a microscope | `drop/4-sometimes/necrobinder/glimpse_beyond.png` |
| Hang | necrobinder | Mayuri Kurotsuchi | A specimen hanging in Mayuri's lab | `drop/4-sometimes/necrobinder/hang.png` |
| Misery | necrobinder | Mayuri Kurotsuchi | Mayuri torturing a captive for data | `drop/4-sometimes/necrobinder/misery.png` |
| Necro Mastery | necrobinder | Mayuri Kurotsuchi | Mayuri as Squad 12 captain with his whole lab behind him | `drop/4-sometimes/necrobinder/necro_mastery.png` |
| Neurosurge | necrobinder | Nemu Kurotsuchi | Nemu's nerve-signal attack on Pernida | `drop/4-sometimes/necrobinder/neurosurge.png` |
| Oblivion | necrobinder | Mayuri Kurotsuchi | Mayuri liquefying himself to disappear | `drop/4-sometimes/necrobinder/oblivion.png` |
| Reanimate | necrobinder | Mayuri Kurotsuchi | Mayuri bringing a dead Arrancar back to life | `drop/4-sometimes/necrobinder/reanimate.png` |
| Reaper Form | necrobinder | Mayuri Kurotsuchi | Mayuri in full Bankai with Konjiki Ashisogi Jizo | `drop/4-sometimes/necrobinder/reaper_form.png` |
| Sacrifice | necrobinder | Nemu Kurotsuchi | Nemu sacrificing herself for Mayuri | `drop/4-sometimes/necrobinder/sacrifice.png` |
| Seance | necrobinder | Mayuri Kurotsuchi | Mayuri communicating with a captured soul | `drop/4-sometimes/necrobinder/seance.png` |
| Sentry Mode | necrobinder | Nemu Kurotsuchi | Nemu standing perfectly still on guard | `drop/4-sometimes/necrobinder/sentry_mode.png` |
| Shared Fate | necrobinder | Nemu Kurotsuchi | Nemu and Mayuri side by side | `drop/4-sometimes/necrobinder/shared_fate.png` |
| Soul Storm | necrobinder | Konjiki Ashisogi Jizo | The Bankai's poison breath storm | `drop/4-sometimes/necrobinder/soul_storm.png` |
| Spirit of Ash | necrobinder | Mayuri Kurotsuchi | Mayuri reforming from liquid | `drop/4-sometimes/necrobinder/spirit_of_ash.png` |
| Squeeze | necrobinder | Konjiki Ashisogi Jizo | The Bankai's giant body crushing an enemy | `drop/4-sometimes/necrobinder/squeeze.png` |
| The Scythe | necrobinder | Mayuri Kurotsuchi | Ashisogi Jizo's three curved blades | `drop/4-sometimes/necrobinder/the_scythe.png` |
| Time's Up | necrobinder | Mayuri Kurotsuchi | Mayuri's bomb exploding | `drop/4-sometimes/necrobinder/times_up.png` |
| Transfigure | necrobinder | Mayuri Kurotsuchi | Mayuri transforming his body | `drop/4-sometimes/necrobinder/transfigure.png` |
| Undeath | necrobinder | Mayuri Kurotsuchi | Mayuri rebuilt after being killed | `drop/4-sometimes/necrobinder/undeath.png` |
| Alchemize | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/alchemize.png` |
| Anointed | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/anointed.png` |
| Beacon of Hope | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/beacon_of_hope.png` |
| Beat Down | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/beat_down.png` |
| Bolas | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/bolas.png` |
| Calamity | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/calamity.png` |
| Entropy | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/entropy.png` |
| Eternal Armor | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/eternal_armor.png` |
| Gold Axe | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/gold_axe.png` |
| Hand of Greed | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/hand_of_greed.png` |
| Hidden Gem | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/hidden_gem.png` |
| Jackpot | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/jackpot.png` |
| Knockdown | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/knockdown.png` |
| Master of Strategy | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/master_of_strategy.png` |
| Mayhem | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/mayhem.png` |
| Mimic | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/mimic.png` |
| Nostalgia | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/nostalgia.png` |
| Rally | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/rally.png` |
| Rend | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/rend.png` |
| Rolling Boulder | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/rolling_boulder.png` |
| Scrawl | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/scrawl.png` |
| Secret Technique | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/secret_technique.png` |
| Secret Weapon | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/secret_weapon.png` |
| Splash | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/splash.png` |
| The Gambit | colorless | Soi Fon | Soi Fon using her Bankai at point-blank range | `drop/4-sometimes/colorless/the_gambit.png` |
| Ascender's Bane | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/ascenders_bane.png` |
| Bad Luck | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/bad_luck.png` |
| Clumsy | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/clumsy.png` |
| Curse of the Bell | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/curse_of_the_bell.png` |
| Debt | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/debt.png` |
| Decay | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/decay.png` |
| Doubt | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/doubt.png` |
| Enthralled | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/enthralled.png` |
| Folly | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/folly.png` |
| Greed | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/greed.png` |
| Guilty | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/guilty.png` |
| Injury | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/injury.png` |
| Normality | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/normality.png` |
| Poor Sleep | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/poor_sleep.png` |
| Regret | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/regret.png` |
| Shame | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/shame.png` |
| Spore Mind | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/spore_mind.png` |
| Writhe | curse |  | _suggestion coming_ | `drop/4-sometimes/curse/writhe.png` |
| Fuel | token |  | _suggestion coming_ | `drop/4-sometimes/token/fuel.png` |
| Giant Rock | token |  | _suggestion coming_ | `drop/4-sometimes/token/giant_rock.png` |
| Luminesce | token |  | _suggestion coming_ | `drop/4-sometimes/token/luminesce.png` |
| Minion Dive Bomb | token |  | _suggestion coming_ | `drop/4-sometimes/token/minion_dive_bomb.png` |
| Minion Sacrifice | token |  | _suggestion coming_ | `drop/4-sometimes/token/minion_sacrifice.png` |
| Minion Strike | token |  | _suggestion coming_ | `drop/4-sometimes/token/minion_strike.png` |
| Shiv | token |  | _suggestion coming_ | `drop/4-sometimes/token/shiv.png` |
| Soul | token |  | _suggestion coming_ | `drop/4-sometimes/token/soul.png` |
| Sovereign Blade | token |  | _suggestion coming_ | `drop/4-sometimes/token/sovereign_blade.png` |
| Sweeping Gaze | token |  | _suggestion coming_ | `drop/4-sometimes/token/sweeping_gaze.png` |

## Wave 5: rarely (ancient, event, quest) (34 cards)

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Break | ironclad | Kenpachi Zaraki | Kenpachi's Bankai splitting the earth (ancient full-art) | `drop/5-rare/ironclad/break.png` |
| Corruption | ironclad | Kenpachi Zaraki | Kenpachi's monstrous Bankai transformation (ancient full-art) | `drop/5-rare/ironclad/corruption.png` |
| Suppress | silent | Soi Fon | Soi Fon pinning Barragan (ancient full-art) | `drop/5-rare/silent/suppress.png` |
| Wraith Form | silent | Soi Fon | Soi Fon in full Shunko with lightning wings (ancient full-art) | `drop/5-rare/silent/wraith_form.png` |
| Biased Cognition | defect | Kisuke Urahara | Urahara's sly grin behind his fan (ancient full-art) | `drop/5-rare/defect/biased_cognition.png` |
| Quadcast | defect | Kisuke Urahara | Urahara casting four kido at once (ancient full-art) | `drop/5-rare/defect/quadcast.png` |
| Meteor Shower | regent | Byakuya Kuchiki | Senbonzakura raining down as a storm (ancient full-art) | `drop/5-rare/regent/meteor_shower.png` |
| The Sealed Throne | regent | Byakuya Kuchiki | Byakuya seated as Kuchiki clan head (ancient full-art) | `drop/5-rare/regent/the_sealed_throne.png` |
| Forbidden Grimoire | necrobinder | Mayuri Kurotsuchi | Mayuri's secret research notes (ancient full-art) | `drop/5-rare/necrobinder/forbidden_grimoire.png` |
| Protector | necrobinder | Nemu Kurotsuchi | Nemu protecting Mayuri from Pernida (ancient full-art) | `drop/5-rare/necrobinder/protector.png` |
| Abundance | event |  | _suggestion coming_ | `drop/5-rare/event/abundance.png` |
| Apotheosis | event |  | _suggestion coming_ | `drop/5-rare/event/apotheosis.png` |
| Apparition | event |  | _suggestion coming_ | `drop/5-rare/event/apparition.png` |
| Brightest Flame | event |  | _suggestion coming_ | `drop/5-rare/event/brightest_flame.png` |
| Byrd Swoop | event |  | _suggestion coming_ | `drop/5-rare/event/byrd_swoop.png` |
| Caltrops | event |  | _suggestion coming_ | `drop/5-rare/event/caltrops.png` |
| Enlightenment | event |  | _suggestion coming_ | `drop/5-rare/event/enlightenment.png` |
| Exterminate | event |  | _suggestion coming_ | `drop/5-rare/event/exterminate.png` |
| Feeding Frenzy | event |  | _suggestion coming_ | `drop/5-rare/event/feeding_frenzy.png` |
| Hello World | event |  | _suggestion coming_ | `drop/5-rare/event/hello_world.png` |
| Maul | event |  | _suggestion coming_ | `drop/5-rare/event/maul.png` |
| Metamorphosis | event |  | _suggestion coming_ | `drop/5-rare/event/metamorphosis.png` |
| Neow's Fury | event |  | _suggestion coming_ | `drop/5-rare/event/neows_fury.png` |
| Peck | event |  | _suggestion coming_ | `drop/5-rare/event/peck.png` |
| Relax | event |  | _suggestion coming_ | `drop/5-rare/event/relax.png` |
| Rip and Tear | event |  | _suggestion coming_ | `drop/5-rare/event/rip_and_tear.png` |
| Squash | event |  | _suggestion coming_ | `drop/5-rare/event/squash.png` |
| Toric Toughness | event |  | _suggestion coming_ | `drop/5-rare/event/toric_toughness.png` |
| Whistle | event |  | _suggestion coming_ | `drop/5-rare/event/whistle.png` |
| Wish | event |  | _suggestion coming_ | `drop/5-rare/event/wish.png` |
| Byrdonis Egg | quest |  | _suggestion coming_ | `drop/5-rare/quest/byrdonis_egg.png` |
| Dowsing | quest |  | _suggestion coming_ | `drop/5-rare/quest/dowsing.png` |
| Lantern Key | quest |  | _suggestion coming_ | `drop/5-rare/quest/lantern_key.png` |
| Spoils Map | quest |  | _suggestion coming_ | `drop/5-rare/quest/spoils_map.png` |
