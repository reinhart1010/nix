---
layout: page
title: common/csvsort (English)
description: "Sorts CSV files."
content_hash: 09f867efcdad4ebf1f0f4e5b3c7e4b6062b2a395
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/csvsort.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvsort

Sorts CSV files.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- Sort a CSV file by column 9:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Sort a CSV file by the "name" column in descending order:

`csvsort -r -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Sort a CSV file by column 2, then by column 4:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Sort a CSV file without inferring data types:

`csvsort --no-inference -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columns</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
