---
layout: page
title: common/boxes (English)
description: "Draw, remove, and repair ASCII art boxes."
content_hash: 58956e07f54e9f3f2c8827cab0b5b57474666265
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# boxes

Draw, remove, and repair ASCII art boxes.
More information: <https://boxes.thomasjensen.com>.

- Draw a box around a string:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes`

- Remove a box from a string:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -r`

- Draw a box with a specific design around a string:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parchment</span>

- Draw a box with a width of 10 and a height of 5:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Draw a box with centered text:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -a c`
