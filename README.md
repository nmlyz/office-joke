[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/nmlyz/office-joke/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/nmlyz/office-joke/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

# office-joke

A one-line office joke, delivered as a plain text file.

## The joke

> I asked IT for a second monitor and they sent me a mirror with a sticky note saying 'reflect on your priorities.'

## How it works

`main.py` uses only the Python standard library. It checks the joke against
the entry rules — a single line, between 1 and 200 characters, ending with a
period — and writes it to `entry.txt`.

The output goes to `/output/entry.txt` by default. Set the
`MAKEFUN_OUTPUT_DIR` environment variable to write it somewhere else instead.

## Running it

```sh
python3 main.py
```

The script prints the path it wrote and exits with status 0 on success.
Running it twice produces a byte-identical file. If the text ever broke a
rule, or the file could not be written, the script would report the problem
on stderr and exit with a non-zero status instead of writing a bad file.

## License

MIT. See [LICENSE](LICENSE).
