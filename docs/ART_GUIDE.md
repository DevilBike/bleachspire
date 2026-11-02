# Art guide

How to fill the mod with Bleach art. You collect the images yourself; this guide says what to look for and where each file goes.

## Who is who

| Slay the Spire 2 | Bleach | Why |
|---|---|---|
| Ironclad | Kenpachi Zaraki | Berserker who loves taking hits: Strength, self-damage, Exhaust |
| Silent | Soi Fon | Stealth-force assassin with a poison blade: Poison, Shivs, discard |
| Defect | Mayuri Kurotsuchi | Mad scientist with gadgets: orbs |
| Regent | Byakuya Kuchiki | Noble whose sword becomes countless blades: blade and stars |
| Necrobinder | Sajin Komamura | His Bankai giant fights beside him: the Osty companion |

Not final until Bike confirms. Change `BLEACH_CHARACTER` in `tools/asset_map.py` and `data/bleach_matches.csv` to swap.

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
| Defend | defect | Mayuri Kurotsuchi | Nemu stepping in front of Mayuri as a shield | `drop/1-every-run/defect/defend_defect.png` |
| Dualcast | defect | Mayuri Kurotsuchi | Mayuri holding two syringes or test tubes | `drop/1-every-run/defect/dualcast.png` |
| Strike | defect | Mayuri Kurotsuchi | Mayuri stabbing with Ashisogi Jizo | `drop/1-every-run/defect/strike_defect.png` |
| Zap | defect | Mayuri Kurotsuchi | Mayuri firing a hidden gadget from his arm or hat | `drop/1-every-run/defect/zap.png` |
| Defend | regent | Byakuya Kuchiki | Byakuya's Senbonzakura petals swirling into a shield | `drop/1-every-run/regent/defend_regent.png` |
| Falling Star | regent | Byakuya Kuchiki | Senbonzakura petals raining down from above | `drop/1-every-run/regent/falling_star.png` |
| Strike | regent | Byakuya Kuchiki | Byakuya drawing Senbonzakura in a single clean slash | `drop/1-every-run/regent/strike_regent.png` |
| Venerate | regent | Byakuya Kuchiki | Byakuya standing calmly with his captain's haori and Kenseikan | `drop/1-every-run/regent/venerate.png` |
| Bodyguard | necrobinder | Sajin Komamura | Kokujo Tengen Myo'o (the giant) standing guard behind Komamura | `drop/1-every-run/necrobinder/bodyguard.png` |
| Defend | necrobinder | Sajin Komamura | Komamura blocking with Tenken's giant armored arm | `drop/1-every-run/necrobinder/defend_necrobinder.png` |
| Strike | necrobinder | Sajin Komamura | Komamura swinging Tenken | `drop/1-every-run/necrobinder/strike_necrobinder.png` |
| Unleash | necrobinder | Sajin Komamura | Komamura calling Bankai as the giant rises | `drop/1-every-run/necrobinder/unleash.png` |
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
| Ball Lightning | defect | Mayuri Kurotsuchi | Mayuri releasing a glowing experimental device | `drop/2-most-runs/defect/ball_lightning.png` |
| Barrage | defect | Mayuri Kurotsuchi | Mayuri's gadgets firing multiple shots | `drop/2-most-runs/defect/barrage.png` |
| Beam Cell | defect | Mayuri Kurotsuchi | A beam from Mayuri's lab equipment | `drop/2-most-runs/defect/beam_cell.png` |
| Boost Away | defect | Mayuri Kurotsuchi | Mayuri escaping on a contraption | `drop/2-most-runs/defect/boost_away.png` |
| Charge Battery | defect | Mayuri Kurotsuchi | Mayuri's lab with sparking machines | `drop/2-most-runs/defect/charge_battery.png` |
| Claw | defect | Mayuri Kurotsuchi | Mayuri's extending arm or blade fingers | `drop/2-most-runs/defect/claw.png` |
| Cold Snap | defect | Mayuri Kurotsuchi | Mayuri freezing a specimen | `drop/2-most-runs/defect/cold_snap.png` |
| Compile Driver | defect | Mayuri Kurotsuchi | Mayuri typing at his giant computer console | `drop/2-most-runs/defect/compile_driver.png` |
| Coolheaded | defect | Mayuri Kurotsuchi | Mayuri calm and smug with arms folded | `drop/2-most-runs/defect/coolheaded.png` |
| Focused Strike | defect | Mayuri Kurotsuchi | Mayuri's precise Ashisogi Jizo thrust | `drop/2-most-runs/defect/focused_strike.png` |
| Go for the Eyes | defect | Mayuri Kurotsuchi | Close-up of Mayuri's yellow eyes | `drop/2-most-runs/defect/go_for_the_eyes.png` |
| Gunk Up | defect | Mayuri Kurotsuchi | Mayuri's sticky paralysis fluid | `drop/2-most-runs/defect/gunk_up.png` |
| Hologram | defect | Mayuri Kurotsuchi | A decoy or clone made by Mayuri | `drop/2-most-runs/defect/hologram.png` |
| Hotfix | defect | Mayuri Kurotsuchi | Mayuri repairing himself with a pill or injection | `drop/2-most-runs/defect/hotfix.png` |
| Leap | defect | Mayuri Kurotsuchi | Mayuri springing out of hiding | `drop/2-most-runs/defect/leap.png` |
| Lightning Rod | defect | Mayuri Kurotsuchi | Mayuri's hat antenna or headpiece crackling | `drop/2-most-runs/defect/lightning_rod.png` |
| Momentum Strike | defect | Mayuri Kurotsuchi | Mayuri charging in with blade raised | `drop/2-most-runs/defect/momentum_strike.png` |
| Sweeping Beam | defect | Mayuri Kurotsuchi | Konjiki Ashisogi Jizo spraying poison breath | `drop/2-most-runs/defect/sweeping_beam.png` |
| TURBO | defect | Mayuri Kurotsuchi | Mayuri injecting a super-drug | `drop/2-most-runs/defect/turbo.png` |
| Uproar | defect | Mayuri Kurotsuchi | Mayuri laughing maniacally | `drop/2-most-runs/defect/uproar.png` |
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
| Afterlife | necrobinder | Sajin Komamura | Komamura's wolf face revealed without the helmet | `drop/2-most-runs/necrobinder/afterlife.png` |
| Blight Strike | necrobinder | Sajin Komamura | Komamura striking with Tenken | `drop/2-most-runs/necrobinder/blight_strike.png` |
| Defile | necrobinder | Sajin Komamura | Komamura in Humanity Technique (beast) form | `drop/2-most-runs/necrobinder/defile.png` |
| Defy | necrobinder | Sajin Komamura | Komamura standing against Tosen | `drop/2-most-runs/necrobinder/defy.png` |
| Drain Power | necrobinder | Sajin Komamura | The giant's armor cracking as Komamura weakens | `drop/2-most-runs/necrobinder/drain_power.png` |
| Fear | necrobinder | Sajin Komamura | The giant looming over a small enemy | `drop/2-most-runs/necrobinder/fear.png` |
| Flatten | necrobinder | Sajin Komamura | Kokujo Tengen Myo'o crushing the ground with its sword | `drop/2-most-runs/necrobinder/flatten.png` |
| Grave Warden | necrobinder | Sajin Komamura | The giant standing like a temple guardian | `drop/2-most-runs/necrobinder/grave_warden.png` |
| Graveblast | necrobinder | Sajin Komamura | Tenken's giant sword slamming down | `drop/2-most-runs/necrobinder/graveblast.png` |
| Invoke | necrobinder | Sajin Komamura | Komamura chanting his Shikai command | `drop/2-most-runs/necrobinder/invoke.png` |
| Negative Pulse | necrobinder | Sajin Komamura | A dark reiatsu shockwave around Komamura | `drop/2-most-runs/necrobinder/negative_pulse.png` |
| Poke | necrobinder | Sajin Komamura | Gonryomaru (Komamura's dog) nudging him | `drop/2-most-runs/necrobinder/poke.png` |
| Pull Aggro | necrobinder | Sajin Komamura | Komamura roaring to draw an enemy's attention | `drop/2-most-runs/necrobinder/pull_aggro.png` |
| Reap | necrobinder | Sajin Komamura | The giant's huge horizontal sword sweep | `drop/2-most-runs/necrobinder/reap.png` |
| Reave | necrobinder | Sajin Komamura | Tenken's giant claw tearing through | `drop/2-most-runs/necrobinder/reave.png` |
| Scourge | necrobinder | Sajin Komamura | Komamura's angry wolf snarl | `drop/2-most-runs/necrobinder/scourge.png` |
| Sculpting Strike | necrobinder | Sajin Komamura | The giant's armor being formed | `drop/2-most-runs/necrobinder/sculpting_strike.png` |
| Snap | necrobinder | Sajin Komamura | The giant's fist snapping shut | `drop/2-most-runs/necrobinder/snap.png` |
| Sow | necrobinder | Sajin Komamura | Komamura kneeling at a grave (Tosen's memory) | `drop/2-most-runs/necrobinder/sow.png` |
| Wisp | necrobinder | Sajin Komamura | A spirit wisp (soul) drifting in Soul Society | `drop/2-most-runs/necrobinder/wisp.png` |

## Wave 3: often (uncommons) (230 cards)

| Card | Pool | Bleach | Look for | File |
|---|---|---|---|---|
| Ashen Strike | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/ashen_strike.png` |
| Battle Trance | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/battle_trance.png` |
| Bloodletting | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/bloodletting.png` |
| Bludgeon | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/bludgeon.png` |
| Bully | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/bully.png` |
| Burning Pact | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/burning_pact.png` |
| Colossus | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/colossus.png` |
| Cruelty | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/cruelty.png` |
| Demonic Shield | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/demonic_shield.png` |
| Dismantle | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/dismantle.png` |
| Drum of Battle | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/drum_of_battle.png` |
| Evil Eye | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/evil_eye.png` |
| Expect a Fight | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/expect_a_fight.png` |
| Feel No Pain | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/feel_no_pain.png` |
| Fight Me! | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/fight_me.png` |
| Flame Barrier | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/flame_barrier.png` |
| Forgotten Ritual | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/forgotten_ritual.png` |
| Hemokinesis | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/hemokinesis.png` |
| Howl from Beyond | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/howl_from_beyond.png` |
| Infernal Blade | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/infernal_blade.png` |
| Inferno | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/inferno.png` |
| Inflame | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/inflame.png` |
| Juggling | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/juggling.png` |
| Pillage | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/pillage.png` |
| Rage | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/rage.png` |
| Rampage | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/rampage.png` |
| Rupture | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/rupture.png` |
| Second Wind | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/second_wind.png` |
| Spite | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/spite.png` |
| Stampede | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/stampede.png` |
| Stomp | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/stomp.png` |
| Stone Armor | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/stone_armor.png` |
| Unrelenting | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/unrelenting.png` |
| Uppercut | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/uppercut.png` |
| Vicious | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/vicious.png` |
| Whirlwind | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/3-often/ironclad/whirlwind.png` |
| Accelerant | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/accelerant.png` |
| Accuracy | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/accuracy.png` |
| Acrobatics | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/acrobatics.png` |
| Backstab | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/backstab.png` |
| Blade Symphony | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/blade_symphony.png` |
| Blur | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/blur.png` |
| Bouncing Flask | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/bouncing_flask.png` |
| Bubble Bubble | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/bubble_bubble.png` |
| Calculated Gamble | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/calculated_gamble.png` |
| Concoct | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/concoct.png` |
| Dash | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/dash.png` |
| Echoing Slash | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/echoing_slash.png` |
| Escape Plan | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/escape_plan.png` |
| Expertise | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/expertise.png` |
| Expose | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/expose.png` |
| Fade | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/fade.png` |
| Finisher | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/finisher.png` |
| Flechettes | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/flechettes.png` |
| Footwork | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/footwork.png` |
| Hand Trick | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/hand_trick.png` |
| Haze | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/haze.png` |
| Hidden Daggers | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/hidden_daggers.png` |
| Infinite Blades | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/infinite_blades.png` |
| Leg Sweep | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/leg_sweep.png` |
| Memento Mori | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/memento_mori.png` |
| Mirage | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/mirage.png` |
| Noxious Fumes | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/noxious_fumes.png` |
| Phantom Blades | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/phantom_blades.png` |
| Pinpoint | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/pinpoint.png` |
| Pounce | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/pounce.png` |
| Precise Cut | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/precise_cut.png` |
| Reflex | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/reflex.png` |
| Skewer | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/skewer.png` |
| Speedster | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/speedster.png` |
| Strangle | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/strangle.png` |
| Tactician | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/tactician.png` |
| Up My Sleeve | silent | Soi Fon | _suggestion coming_ | `drop/3-often/silent/up_my_sleeve.png` |
| Boot Sequence | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/boot_sequence.png` |
| Bulk Up | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/bulk_up.png` |
| Capacitor | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/capacitor.png` |
| Chaos | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/chaos.png` |
| Chill | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/chill.png` |
| Compact | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/compact.png` |
| Darkness | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/darkness.png` |
| Double Energy | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/double_energy.png` |
| Energy Surge | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/energy_surge.png` |
| FTL | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/ftl.png` |
| Feral | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/feral.png` |
| Fight Through | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/fight_through.png` |
| Fusion | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/fusion.png` |
| Genetic Algorithm | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/genetic_algorithm.png` |
| Glacier | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/glacier.png` |
| Glasswork | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/glasswork.png` |
| Hailstorm | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/hailstorm.png` |
| Hibernate | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/hibernate.png` |
| Ignition | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/ignition.png` |
| Iteration | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/iteration.png` |
| Loop | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/loop.png` |
| Null | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/null.png` |
| Overclock | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/overclock.png` |
| Refract | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/refract.png` |
| Rocket Punch | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/rocket_punch.png` |
| Scavenge | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/scavenge.png` |
| Scrape | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/scrape.png` |
| Shadow Shield | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/shadow_shield.png` |
| Skim | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/skim.png` |
| Smokestack | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/smokestack.png` |
| Storm | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/storm.png` |
| Subroutine | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/subroutine.png` |
| Sunder | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/sunder.png` |
| Synchronize | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/synchronize.png` |
| Synthesis | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/synthesis.png` |
| Tempest | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/tempest.png` |
| Tesla Coil | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/tesla_coil.png` |
| Thunder | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/thunder.png` |
| White Noise | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/3-often/defect/white_noise.png` |
| Alignment | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/alignment.png` |
| Black Hole | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/black_hole.png` |
| Bulwark | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/bulwark.png` |
| CHARGE!! | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/charge.png` |
| Child of the Stars | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/child_of_the_stars.png` |
| Conqueror | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/conqueror.png` |
| Constellation | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/constellation.png` |
| Convergence | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/convergence.png` |
| Devastate | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/devastate.png` |
| Furnace | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/furnace.png` |
| Gamma Blast | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/gamma_blast.png` |
| Glimmer | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/glimmer.png` |
| Hegemony | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/hegemony.png` |
| Kingly Kick | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/kingly_kick.png` |
| Kingly Punch | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/kingly_punch.png` |
| Knockout Blow | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/knockout_blow.png` |
| Largesse | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/largesse.png` |
| Lunar Blast | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/lunar_blast.png` |
| Manifest Authority | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/manifest_authority.png` |
| Monologue | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/monologue.png` |
| Orbit | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/orbit.png` |
| Pale Blue Dot | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/pale_blue_dot.png` |
| Parry | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/parry.png` |
| Particle Wall | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/particle_wall.png` |
| Pillar of Creation | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/pillar_of_creation.png` |
| Plot | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/plot.png` |
| Prophesize | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/prophesize.png` |
| Quasar | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/quasar.png` |
| Radiate | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/radiate.png` |
| Reflect | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/reflect.png` |
| Reserves | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/reserves.png` |
| Resonance | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/resonance.png` |
| Royal Gamble | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/royal_gamble.png` |
| Shining Strike | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/shining_strike.png` |
| Spectrum Shift | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/spectrum_shift.png` |
| Stardust | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/stardust.png` |
| Summon Forth | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/summon_forth.png` |
| Supermassive | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/supermassive.png` |
| Terraforming | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/3-often/regent/terraforming.png` |
| Bone Shards | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/bone_shards.png` |
| Borrowed Time | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/borrowed_time.png` |
| Bury | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/bury.png` |
| Calcify | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/calcify.png` |
| Capture Spirit | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/capture_spirit.png` |
| Cleanse | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/cleanse.png` |
| Countdown | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/countdown.png` |
| Danse Macabre | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/danse_macabre.png` |
| Death March | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/death_march.png` |
| Death's Door | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/deaths_door.png` |
| Deathbringer | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/deathbringer.png` |
| Debilitate | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/debilitate.png` |
| Delay | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/delay.png` |
| Dirge | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/dirge.png` |
| Dredge | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/dredge.png` |
| Enfeebling Touch | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/enfeebling_touch.png` |
| Fetch | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/fetch.png` |
| Friendship | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/friendship.png` |
| Haunt | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/haunt.png` |
| High Five | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/high_five.png` |
| Legion of Bone | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/legion_of_bone.png` |
| Lethality | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/lethality.png` |
| Melancholy | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/melancholy.png` |
| No Escape | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/no_escape.png` |
| Pagestorm | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/pagestorm.png` |
| Parse | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/parse.png` |
| Pull from Below | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/pull_from_below.png` |
| Putrefy | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/putrefy.png` |
| Rattle | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/rattle.png` |
| Right Hand Hand | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/right_hand_hand.png` |
| Scavenge | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/scavenge.png` |
| Severance | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/severance.png` |
| Shroud | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/shroud.png` |
| Sic 'Em | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/sic_em.png` |
| Sleight of Flesh | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/sleight_of_flesh.png` |
| Soulbound | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/soulbound.png` |
| Spur | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/spur.png` |
| Underworld | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/underworld.png` |
| Veilpiercer | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/3-often/necrobinder/veilpiercer.png` |
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
| Aggression | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/aggression.png` |
| Barricade | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/barricade.png` |
| Brand | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/brand.png` |
| Cascade | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/cascade.png` |
| Conflagration | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/conflagration.png` |
| Crimson Mantle | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/crimson_mantle.png` |
| Dark Embrace | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/dark_embrace.png` |
| Demon Form | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/demon_form.png` |
| Dominate | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/dominate.png` |
| Feed | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/feed.png` |
| Fiend Fire | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/fiend_fire.png` |
| Hellraiser | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/hellraiser.png` |
| Impervious | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/impervious.png` |
| Juggernaut | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/juggernaut.png` |
| Mangle | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/mangle.png` |
| Midnight | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/midnight.png` |
| Not Yet | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/not_yet.png` |
| Offering | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/offering.png` |
| One-Two Punch | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/one_two_punch.png` |
| Pact's End | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/pacts_end.png` |
| Primal Force | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/primal_force.png` |
| Pyre | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/pyre.png` |
| Stoke | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/stoke.png` |
| Tank | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/tank.png` |
| Tear Asunder | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/tear_asunder.png` |
| Thrash | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/thrash.png` |
| Unmovable | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/4-sometimes/ironclad/unmovable.png` |
| Abrasive | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/abrasive.png` |
| Adrenaline | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/adrenaline.png` |
| Afterimage | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/afterimage.png` |
| Assassinate | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/assassinate.png` |
| Blade of Ink | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/blade_of_ink.png` |
| Bullet Time | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/bullet_time.png` |
| Burst | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/burst.png` |
| Corrosive Wave | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/corrosive_wave.png` |
| Envenom | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/envenom.png` |
| Fan of Knives | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/fan_of_knives.png` |
| Flanking | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/flanking.png` |
| Grand Finale | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/grand_finale.png` |
| Knife Trap | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/knife_trap.png` |
| Malaise | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/malaise.png` |
| Master Planner | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/master_planner.png` |
| Murder | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/murder.png` |
| Nightmare | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/nightmare.png` |
| Outbreak | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/outbreak.png` |
| Serpent Form | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/serpent_form.png` |
| Shadow Step | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/shadow_step.png` |
| Shadowmeld | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/shadowmeld.png` |
| Sneaky | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/sneaky.png` |
| Storm of Steel | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/storm_of_steel.png` |
| The Gambit | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/the_gambit.png` |
| The Hunt | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/the_hunt.png` |
| Tools of the Trade | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/tools_of_the_trade.png` |
| Tracking | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/tracking.png` |
| Well-Laid Plans | silent | Soi Fon | _suggestion coming_ | `drop/4-sometimes/silent/well_laid_plans.png` |
| Adaptive Strike | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/adaptive_strike.png` |
| All for One | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/all_for_one.png` |
| Buffer | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/buffer.png` |
| Consuming Shadow | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/consuming_shadow.png` |
| Coolant | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/coolant.png` |
| Creative AI | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/creative_ai.png` |
| Defragment | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/defragment.png` |
| Echo Form | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/echo_form.png` |
| Flak Cannon | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/flak_cannon.png` |
| Helix Drill | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/helix_drill.png` |
| Hyperbeam | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/hyperbeam.png` |
| Ice Lance | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/ice_lance.png` |
| Imitation Learning | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/imitation_learning.png` |
| Machine Learning | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/machine_learning.png` |
| Meteor Strike | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/meteor_strike.png` |
| Modded | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/modded.png` |
| Multi-Cast | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/multi_cast.png` |
| One for All | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/one_for_all.png` |
| Rainbow | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/rainbow.png` |
| Reboot | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/reboot.png` |
| Shatter | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/shatter.png` |
| Signal Boost | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/signal_boost.png` |
| Spinner | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/spinner.png` |
| Supercritical | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/supercritical.png` |
| Trash to Treasure | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/trash_to_treasure.png` |
| Voltaic | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/4-sometimes/defect/voltaic.png` |
| Arsenal | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/arsenal.png` |
| Beat into Shape | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/beat_into_shape.png` |
| Big Bang | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/big_bang.png` |
| Bombardment | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/bombardment.png` |
| Bundle of Joy | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/bundle_of_joy.png` |
| Comet | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/comet.png` |
| Crash Landing | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/crash_landing.png` |
| Decisions, Decisions | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/decisions_decisions.png` |
| Dying Star | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/dying_star.png` |
| Foregone Conclusion | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/foregone_conclusion.png` |
| GUARDS!!! | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/guards.png` |
| Genesis | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/genesis.png` |
| Hammer Time | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/hammer_time.png` |
| Heavenly Drill | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/heavenly_drill.png` |
| Heirloom Hammer | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/heirloom_hammer.png` |
| I Am Invincible | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/i_am_invincible.png` |
| Make It So | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/make_it_so.png` |
| Monarch's Gaze | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/monarchs_gaze.png` |
| Neutron Aegis | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/neutron_aegis.png` |
| Royalties | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/royalties.png` |
| Seeking Edge | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/seeking_edge.png` |
| Seven Stars | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/seven_stars.png` |
| Sword Sage | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/sword_sage.png` |
| The Smith | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/the_smith.png` |
| Tutor | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/tutor.png` |
| Tyranny | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/tyranny.png` |
| Void Form | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/4-sometimes/regent/void_form.png` |
| Banshee's Cry | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/banshees_cry.png` |
| Cacophony | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/cacophony.png` |
| Call of the Void | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/call_of_the_void.png` |
| Demesne | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/demesne.png` |
| Devour Life | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/devour_life.png` |
| Eidolon | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/eidolon.png` |
| End of Days | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/end_of_days.png` |
| Eradicate | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/eradicate.png` |
| Glimpse Beyond | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/glimpse_beyond.png` |
| Hang | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/hang.png` |
| Misery | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/misery.png` |
| Necro Mastery | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/necro_mastery.png` |
| Neurosurge | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/neurosurge.png` |
| Oblivion | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/oblivion.png` |
| Reanimate | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/reanimate.png` |
| Reaper Form | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/reaper_form.png` |
| Sacrifice | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/sacrifice.png` |
| Seance | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/seance.png` |
| Sentry Mode | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/sentry_mode.png` |
| Shared Fate | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/shared_fate.png` |
| Soul Storm | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/soul_storm.png` |
| Spirit of Ash | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/spirit_of_ash.png` |
| Squeeze | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/squeeze.png` |
| The Scythe | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/the_scythe.png` |
| Time's Up | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/times_up.png` |
| Transfigure | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/transfigure.png` |
| Undeath | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/4-sometimes/necrobinder/undeath.png` |
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
| The Gambit | colorless |  | _suggestion coming_ | `drop/4-sometimes/colorless/the_gambit.png` |
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
| Break | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/5-rare/ironclad/break.png` |
| Corruption | ironclad | Kenpachi Zaraki | _suggestion coming_ | `drop/5-rare/ironclad/corruption.png` |
| Suppress | silent | Soi Fon | _suggestion coming_ | `drop/5-rare/silent/suppress.png` |
| Wraith Form | silent | Soi Fon | _suggestion coming_ | `drop/5-rare/silent/wraith_form.png` |
| Biased Cognition | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/5-rare/defect/biased_cognition.png` |
| Quadcast | defect | Mayuri Kurotsuchi | _suggestion coming_ | `drop/5-rare/defect/quadcast.png` |
| Meteor Shower | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/5-rare/regent/meteor_shower.png` |
| The Sealed Throne | regent | Byakuya Kuchiki | _suggestion coming_ | `drop/5-rare/regent/the_sealed_throne.png` |
| Forbidden Grimoire | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/5-rare/necrobinder/forbidden_grimoire.png` |
| Protector | necrobinder | Sajin Komamura | _suggestion coming_ | `drop/5-rare/necrobinder/protector.png` |
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
