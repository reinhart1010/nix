---
layout: page
title: common/awk (English)
description: "A versatile programming language for working on files."
content_hash: 1a7bcee3395c8fe2a90f232f95def5e052daf457
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awk

A versatile programming language for working on files.
More information: <https://github.com/onetrueawk/awk>.

- Print the fifth column (a.k.a. field) in a space-separated file:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the second column of the lines containing "foo" in a space-separated file:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the last column of each line in a file, using a comma (instead of space) as a field separator:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Sum the values in the first column of a file and print the total:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print every third line starting from the first line:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print different values based on conditions:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print all lines where the 10th column value equals the specified value:

`awk '($10 == value)'`

- Print all the lines which the 10th column value is between a min and a max:

`awk '($10 >= min_value && $10 <= max_value)'`
