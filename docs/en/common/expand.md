---
layout: page
title: common/expand (English)
description: "Convert tabs to spaces."
content_hash: 52f114995f39e1c753aff88ae362f885afec8887
last_modified_at: 2022-12-04
related_topics:
  - title: italiano version
    url: /it/common/expand.html
    icon: bi bi-globe
---
# expand

Convert tabs to spaces.
More information: <https://www.gnu.org/software/coreutils/expand>.

- Convert tabs in each file to spaces, writing to standard output:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert tabs to spaces, reading from standard input:

`expand`

- Do not convert tabs after non blanks:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Have tabs a certain number of characters apart, not 8:

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use a comma separated list of explicit tab positions:

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
