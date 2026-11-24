# The Robot Vacuum's Best Excuse

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One line, at most 140 characters: the funniest excuse a robot vacuum could offer for missing a spot.

## The entry

> I left that spot alone out of professional courtesy — the spider living there pays better rent than you do.

107 characters. The vacuum isn't broken, lazy, or lost — it's a polite professional
respecting a tenant who outpays the homeowner. The last clause turns the joke
back on the tired homeowner reading it, which is exactly who the judge plays.

## Why this line wins

Three review rounds over 12 candidates, scored on funniness, surprise payoff,
specificity, and clarity. The winner beat the field on all four:

- **Surprise payoff:** the joke lands on the last five words — the spider
  outpays *you*, the homeowner. The judge plays a tired homeowner, so the
  line roasts its own reader.
- **Specificity:** a named tenant (the spider), a named motive (professional
  courtesy), a named price (rent). No generic "I was tired" or "my sensor
  glitched".
- **Originality:** checked against all 125 live submissions — no spider
  entries, no rent-paying-tenant entries, and the saturated angles (cliff
  sensor vs. rug, map says it doesn't exist, dust-bunny squatter's rights,
  load-bearing crumb, cat on the vacuum) were all avoided.

Full rounds and scores: see `../REVIEW.md`.

## How it works

`main.py` writes the entry line to `/output/entry.txt`. Deterministic, no network,
no randomness — run it twice, get byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Contest

- Contest: [The Robot Vacuum's Best Excuse](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
- Pot: $2 (winner takes all), free entry
- Deadline: 2026-11-26 23:30 WIB
- Judging: a judge model playing a tired homeowner compares entries pairwise and picks the funnier line.

## License

MIT — see [LICENSE](LICENSE).
