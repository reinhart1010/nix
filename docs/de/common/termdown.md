---
layout: page
title: common/termdown (Deutsch)
description: "Command-line Countdown-Timer."
content_hash: 41442dfa94d5fca43ef7c038b623c50f0109cbb8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/termdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# termdown

Command-line Countdown-Timer.
Weitere Informationen: <https://github.com/trehn/termdown>.

- Starte Stoppuhr:

`termdown`

- Starte einen Countdown von 1 Minute 30 Sekunden:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>

- Starte einen Countdown von 1 Minute 30 Sekunden. Nach ablauf der Zeit blinkt das Terminal:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>` --blink`

- Countdown mit Titel über der abgelaufenen Zeit:

`termdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1m30s</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Interesting title</span>`"`

- Zeige aktuelle Zeit:

`termdown --time`
