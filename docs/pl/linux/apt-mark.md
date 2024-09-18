---
layout: page
title: linux/apt-mark (polski)
description: "Narzędzie do zmiany statusu zainstalowanych pakietów."
content_hash: d86822d22cb16759206ab12a87a749a3713deb31
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Narzędzie do zmiany statusu zainstalowanych pakietów.
Więcej informacji: <https://manned.org/apt-mark.8>.

- Oznacz pakiet jako zainstalowany automatycznie:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zatrzymaj pakiet w bieżącej wersji i zapobiegaj jego aktualizacjom:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Zezwól, aby pakiet znowu był aktualizowany:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Pokaż pakiety zainstalowane ręcznie:

`apt-mark showmanual`

- Pokaż zatrzymane pakiety, które nie są aktualizowane:

`apt-mark showhold`
