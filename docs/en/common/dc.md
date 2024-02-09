---
layout: page
title: common/dc (English)
description: "An arbitrary precision calculator. Uses reverse polish notation (RPN)."
content_hash: f5d6d0e9ec638c938999293b2c513b2026a9e544
last_modified_at: 2024-02-09
related_topics:
  - title: italiano version
    url: /it/common/dc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dc

An arbitrary precision calculator. Uses reverse polish notation (RPN).
See also: `bc`.
More information: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>.

- Start an interactive session:

`dc`

- Execute a script:

`dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.dc</span>

- Calculate an expression with the specified scale:

`dc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 3 /</span>` p'`

- Calculate 4 times 5 (4 5 *), subtract 17 (17 -), and [p]rint the output:

`dc --expression='4 5 * 17 - p'`

- Specify the number of decimal places to 7 (7 k), calculate 5 divided by -3 (5 _3 /) and [p]rint:

`dc --expression='7 k 5 _3 / p'`

- Calculate the golden ratio, phi: set number of decimal places to 100 (100 k), square root of 5 (5 v) plus 1 (1 +), divided by 2 (2 /), and [p]rint result:

`dc --expression='100 k 5 v 1 + 2 / p'`
