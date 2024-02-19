---
layout: page
title: common/boxes (English)
description: "Draw, remove, and repair ASCII art boxes."
content_hash: 237e0adb0eff631eeca6c7d906b337246c19e63b
last_modified_at: 2024-02-19
related_topics:
  - title: فارسی version
    url: /fa/common/boxes.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/boxes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boxes

Draw, remove, and repair ASCII art boxes.
More information: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- Draw a box around a string:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes`

- [r]emove a box from a string:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -r`

- Specify the box [d]esign:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parchment</span>

- Specify the box [s]ize (in columns by lines):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- [a]lign the box text [h]orizonally (at [l]eft, [c]enter or [r]ight):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -a h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">l|c|r</span>

- [a]lign the box text [v]ertically (at [t]op, [c]enter or [b]ottom):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -a v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t|c|b</span>

- [j]ustify the box text (at [l]eft, [c]enter or [r]ight):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" | boxes -a j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">l|c|r</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vt</span>
