---
layout: page
title: common/tput (English)
description: "View and modify terminal settings and capabilities."
content_hash: b376bd1ea52ea311519eba99a56147803459ebc8
last_modified_at: 2025-03-02
related_topics:
  - title: français version
    url: /fr/common/tput.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tput.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tput.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tput

View and modify terminal settings and capabilities.
More information: <https://manned.org/tput>.

- Move the cursor to a screen location:

`tput cup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">row</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Set foreground (af) or background (ab) color:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setaf|setab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ansi_color_code</span>

- Reverse text and background colors:

`tput rev`

- Reset all terminal text attributes:

`tput sgr0`

- Show number of columns, lines, or colors:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols|lines|colors</span>

- Enable or disable word wrap:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>

- Hide or show the terminal cursor:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">civis|cnorm</span>

- Save or restore terminal text status (smcup also captures scroll wheel events):

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smcup|rmcup</span>
