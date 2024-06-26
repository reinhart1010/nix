---
layout: page
title: common/csvsort (English)
description: "Sort CSV files."
content_hash: 8f1b164997532798a65f4bd66546803a5494487f
last_modified_at: 2024-04-26
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

Sort CSV files.
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
