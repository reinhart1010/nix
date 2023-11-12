---
layout: page
title: common/csvstat (English)
description: "Print descriptive statistics for all columns in a CSV file."
content_hash: ca7eacd88d17da257a1adfe39e8d4036705017c5
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/csvstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvstat

Print descriptive statistics for all columns in a CSV file.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- Show all stats for all columns:

`csvstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Show all stats for columns 2 and 4:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Show sums for all columns:

`csvstat --sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Show the max value length for column 3:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Show the number of unique values in the "name" column:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
