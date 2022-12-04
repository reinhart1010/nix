---
layout: page
title: common/comm (English)
description: "Select or reject lines common to two files. Both files must be sorted."
content_hash: 29b5283df552f88b544d244d28e1e8be4ef7f10c
last_modified_at: 2022-12-04
related_topics:
  - title: italiano version
    url: /it/common/comm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/comm.html
    icon: bi bi-globe
---
# comm

Select or reject lines common to two files. Both files must be sorted.
More information: <https://www.gnu.org/software/coreutils/comm>.

- Produce three tab-separated columns: lines only in first file, lines only in second file and common lines:

`comm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Print only lines common to both files:

`comm -12 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Print only lines common to both files, reading one file from `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` | comm -12 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Get lines only found in first file, saving the result to a third file:

`comm -23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1_only</span>

- Print lines only found in second file, when the files aren't sorted:

`comm -13 <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>`) <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>`)`
