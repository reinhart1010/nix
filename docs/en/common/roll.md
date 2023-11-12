---
layout: page
title: common/roll (English)
description: "Rolls a user-defined dice sequence."
content_hash: 6628dfbb294524fd3d71240cd894c96d1c70d300
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# roll

Rolls a user-defined dice sequence.
More information: <https://manned.org/roll>.

- Roll 3 6-sided dice and sums the results:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3d</span>

- Roll 1 8-sided die, add 3 and sum the results:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d8 + 3</span>

- Roll 4 6-sided dice, keep the 3 highest results and sum the results:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4d6h3</span>

- Roll 2 12-sided dice 2 times and show every roll:

`roll --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2{2d12}</span>

- Roll 2 20-sided dice until the result is bigger than 10:

`roll "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2d20>10</span>`"`

- Roll 2 5-sided dice 3 times and show the total sum:

`roll --sum-series `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3{2d5}</span>
