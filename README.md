[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/giandisruw/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/giandisruw/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

# The Funniest Sick-Day Excuse

`main.py` writes one fixed funny sick-day excuse, under 200 characters,
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). The line is a constant string: no randomness, no time, no
network, so every run writes byte-identical output.

**The winning line (111 characters):**

> Sorry, my dentist fitted a temporary crown that whistles every time I lie, so I can't risk the morning standup.

## How it was chosen

Seven candidate lines were written against the bounty's published judge
brief — half believable, fresh idea (no fever, dog, or dead grandmother),
twist landing near the end, sounding like a real person typing a message,
no wasted words — then judged pairwise by a local judge (Caffeine
Inference router) using that same brief. Every pair was judged in both
orders (42 judge calls). Each call gives the picked entry
0.5 + margin/10 (margin 1–5); a game's score is the mean of its two calls.

Tournament table (run 2026-11-25, 42 judge calls, all via the Caffeine
Inference router — no fallback needed; every call returned a verdict):

| # | Candidate | Win rate | Games won |
|---|-----------|----------|-----------|
| 4 | Whistling crown — "Sorry, my dentist fitted a temporary crown that whistles every time I lie, so I can't risk the morning standup." | 0.7667 | 6/6 |
| 3 | Stuck in hoodie — "Can't make it in — I got stuck in my own hoodie this morning and my neighbour had to cut me out with kitchen scissors." | 0.6583 | 4/6 |
| 2 | Cat locks me in bathroom — "Won't be in today, my cat learned to open doors and has locked me in the bathroom until I admit he's the boss." | 0.5083 | 3/6 |
| 5 | Sleep-talking speaker — "Not in today — my smart speaker started sleep-talking in my voice and HR has already logged me as present twice." | 0.4917 | 1/6 |
| 1 | Fridge negotiation — "Sorry, can't come in — my smart fridge locked the kitchen overnight and I've been negotiating with it since 6am." | 0.4667 | 2/6 |
| 6 | Ironed shirt while wearing it — "Can't come in, I tried to iron my shirt while wearing it and now I'm technically part of the laundry." | 0.4083 | 2/6 |
| 7 | Car failed vibe check — "Sorry, my car passed its MOT but failed its vibe check, and the mechanic says it needs a day off too." | 0.2000 | 0/6 |

The whistling crown won every game: the twist lands on the last word
("standup"), it is half believable, and it is the freshest idea of the
set. Full per-call records: `tournament.jsonl`; aggregated table:
`tournament_table.json`; runner: `tournament.py`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty "The Funniest Sick-Day Excuse" ($2, sponsor @zeroxfive).
Referral code: 0txwmf1m
