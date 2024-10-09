---
layout: page
title: common/nice (Nederlands)
description: "Voer een programma uit met een aangepaste planningsprioriteit (niceness)."
content_hash: 057b3e9b57ed49d8f1a7b91e9ce4d91734598924
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/nice.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nice

Voer een programma uit met een aangepaste planningsprioriteit (niceness).
Niceness-waarden variëren van -20 (de hoogste prioriteit) tot 19 (de laagste).
Meer informatie: <https://www.gnu.org/software/coreutils/nice>.

- Start een programma met een aangepaste prioriteit:

`nice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
