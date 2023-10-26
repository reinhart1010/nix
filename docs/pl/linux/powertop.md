---
layout: page
title: linux/powertop (polski)
description: "Optymalizuje zużycie energii akumulatora."
content_hash: 11c818fdcf02fb4d704c6604ccb149bed84890b1
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/linux/powertop.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/powertop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># powertop

Optymalizuje zużycie energii akumulatora.
Więcej informacji: <https://github.com/fenrus75/powertop>.

- Kalibracja pomiarów zużycia energii:

`sudo powertop --calibrate`

- Generowanie raportu zużycia enrgii w HTML w bieżącym katalogu:

`sudo powertop --html=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raport_zużycia_energii.html</span>

- Dostrojenie do optymalnych ustawień:

`sudo powertop --auto-tune`
