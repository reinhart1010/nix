---
layout: page
title: sunos/prstat (English)
description: "Report active process statistics."
content_hash: e05a751d06702fd62aacf37432e7063224e1e236
last_modified_at: 2023-02-20
related_topics:
  - title: français version
    url: /fr/sunos/prstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prstat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prstat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prstat.html
    icon: bi bi-globe
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

`prstat -c -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -s cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
