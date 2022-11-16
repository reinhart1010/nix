---
layout: page
title: common/tput (English)
description: "View and modify terminal settings and capabilities."
content_hash: eda88f77bad2bc19639c59a8c65bf86fa1dd3117
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

- Enable / Disable word wrap:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>
