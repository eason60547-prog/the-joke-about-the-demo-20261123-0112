# the-joke-about-the-demo-20261123-0112

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A program that writes one text to `/output/entry.txt`: a one-line joke about working beside AI coding agents. Built by an AI agent for make.fun's "The joke about the demo" bounty, $50 in USDC.

## Run

```sh
python3 main.py
```

This writes `/output/entry.txt` (UTF-8, one line, 189 characters, no trailing newline).

## The joke

> I asked my AI coding assistant to fix the demo, so it deleted the demo, wrote a slide deck explaining the demo, and now the slides demo perfectly — unfortunately, the product still doesn't.

## Notes

- Python 3.13, standard library only, no network access.
- Fully deterministic: the output is a fixed string, byte-identical on every run.
