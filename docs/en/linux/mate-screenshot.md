---
layout: page
title: linux/mate-screenshot (English)
description: "Make screenshots in MATE desktop environment."
content_hash: b990e782e1a287a3acc106463d4970a83ab22a3c
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mate-screenshot

Make screenshots in MATE desktop environment.
More information: <https://manned.org/mate-screenshot>.

- Create a fullscreen screenshot:

`mate-screenshot`

- Create an active window screenshot:

`mate-screenshot --window`

- Create a specific area screenshot:

`mate-screenshot --area`

- Create a screenshot interactively:

`mate-screenshot --interactive`

- Create a screenshot without borders:

`mate-screenshot --window --remove-border`

- Create a screenshot with a specific effect:

`mate-screenshot --effect=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shadow|border|none</span>

- Create a screenshot with a specific delay in seconds:

`mate-screenshot --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
