---
layout: page
title: linux/powertop (polski)
description: "Optymalizuje zużycie energii akumulatora."
content_hash: aa79e45e6e4ce13dfac4da790a63b9f487f22c02
related_topics:
  - title: English version
    url: /en/linux/powertop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># powertop

Optymalizuje zużycie energii akumulatora.
Więcej informacji: <https://github.com/fenrus75/powertop>.

- Kalibracja pomiarów zużycia energii

`sudo powertop --calibrate`

- Generowanie raportu zużycia enrgii w HTML w bieżącym katalogu:

`sudo powertop --html=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raport_zużycia_energii.html</span>

- Dostrojenie do optymalnych ustawień:

`sudo powertop --auto-tune`
