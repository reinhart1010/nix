---
layout: page
title: common/xev (English)
description: "Print contents of X events."
content_hash: 8102380fa096774945987fd38854421eda7e6823
---
# xev

Print contents of X events.
More information: <https://gitlab.freedesktop.org/xorg/app/xev>.

- Monitor all occurring X events:

`xev`

- Monitor all X events of the root window instead of creating a new one:

`xev -root`

- Monitor all X events of a particular window:

`xev -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">window_id</span>

- Monitor X events from a given category (can be specified multiple times):

`xev -event `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_category</span>
