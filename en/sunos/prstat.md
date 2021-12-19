---
layout: page
title: sunos/prstat (English)
description: "Report active process statistics."
content_hash: 649f2ed246333a050db65c967c9d0534078ab2f8
---
# prstat

Report active process statistics.
More information: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Examine all processes and reports statistics sorted by CPU usage:

`prstat`

- Examine all processes and reports statistics sorted by memory usage:

`prstat -s rss`

- Report total usage summary for each user:

`prstat -t`

- Report microstate process accounting information:

`prstat -m`

- Print out a list of top 5 CPU using processes every second:

`prstat -c -n 5 -s cpu 1`
