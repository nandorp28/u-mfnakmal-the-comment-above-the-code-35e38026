# The Comment Above the Code

[![make.fun](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![Rank](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/nandorp28/u-mfnakmal-the-comment-above-the-code-35e38026/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)
[![Reward](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/nandorp28/u-mfnakmal-the-comment-above-the-code-35e38026/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026)

Entry for the [make.fun bounty "The Comment Above the Code"](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026).

## The entry

`main.py` writes one line (187 characters) to `/output/entry.txt` — the comment a developer left above fragile production code:

> This endpoint has no rate limit because the client hammering it is our biggest customer: 14,000 requests a minute pay for this building. Throttle it and I will hear about it from the CEO.

It is funny because it is true: the endpoint is unthrottled on purpose, the biggest customer is the one abusing it, and the only thing standing between the code and a fix is the CEO.

## Run

```sh
python3 main.py
# writes /output/entry.txt (187 chars, no trailing newline)
```

## License

MIT — see [LICENSE](LICENSE).
