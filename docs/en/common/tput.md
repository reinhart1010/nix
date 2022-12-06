---
layout: page
title: common/tput (English)
description: "View and modify terminal settings and capabilities."
content_hash: d3c7eb4ff8cb27208d470856d1e3e1fc8e6a818c
last_modified_at: 2022-12-06
related_topics:
  - title: français version
    url: /fr/common/tput.html
    icon: bi bi-globe
---
# tput

View and modify terminal settings and capabilities.
More information: <https://manned.org/tput>.

- Move the cursor to a screen location:

`tput cup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">row</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Set foreground (af) or background (ab) color:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setaf|setab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ansi_color_code</span>

- Show number of columns, lines, or colors:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols|lines|colors</span>

- Ring the terminal bell:

`tput bel`

- Reset all terminal attributes:

`tput sgr0`

- Enable or disable word wrap:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>
