---
layout: page
title: common/nice (Nederlands)
description: "Voer een programma uit met een aangepaste planningsprioriteit (niceness)."
content_hash: 1f01e091e18595dc3ad9134ec8bca65bafa053ac
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/nice.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nice

Voer een programma uit met een aangepaste planningsprioriteit (niceness).
Niceness-waarden variëren van -20 (de hoogste prioriteit) tot 19 (de laagste).
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Start een programma met een aangepaste prioriteit:

`nice -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Definieer de prioriteit met een expliciete optie:

`nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--adjustment</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niceness_waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
