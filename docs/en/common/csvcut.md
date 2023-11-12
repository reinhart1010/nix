---
layout: page
title: common/csvcut (English)
description: "Filter and truncate CSV files. Like Unix's `cut` command, but for tabular data."
content_hash: 5b53ffed8bce87ca6fa2c49469ccd8dd7e6115cd
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/csvcut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvcut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvcut

Filter and truncate CSV files. Like Unix's `cut` command, but for tabular data.
Included in csvkit.
More information: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- Print indices and names of all columns:

`csvcut -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Extract the first and third columns:

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Extract all columns **except** the fourth one:

`csvcut -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Extract the columns named "id" and "first name" (in that order):

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id,"first name"</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
