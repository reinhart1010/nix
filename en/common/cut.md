---
layout: page
title: common/cut (English)
description: "Cut out fields from stdin or files."
content_hash: a9ee4764ab1cc1d77062d996ceac691a4a8e6ff0
related_topics:
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
---
# cut

Cut out fields from stdin or files.
More information: <https://www.gnu.org/software/coreutils/cut>.

- Cut out the first sixteen characters of each line of stdin:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>

- Cut out the first sixteen characters of each line of the given files:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Cut out everything from the 3rd character to the end of each line:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>

- Cut out the fifth field of each line, using a colon as a field delimiter (default delimiter is tab):

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Cut out the 2nd and 10th fields of each line, using a semicolon as a delimiter:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,10</span>

- Cut out the fields 3 through to the end of each line, using a space as a delimiter:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>
