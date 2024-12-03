---
layout: page
title: common/printenv (English)
description: "Print values of all or environment variables."
content_hash: 1a3317f981e82eb50e95df35207d899ba4538d50
last_modified_at: 2024-12-03
related_topics:
  - title: 한국어 version
    url: /ko/common/printenv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/printenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# printenv

Print values of all or environment variables.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/printenv-invocation.html>.

- Display key-value pairs of all environment variables:

`printenv`

- Display the value of a specific variable:

`printenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>

- Display the value of a variable and end with NUL instead of newline:

`printenv --null `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HOME</span>
