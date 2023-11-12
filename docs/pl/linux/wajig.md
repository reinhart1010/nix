---
layout: page
title: linux/wajig (polski)
description: "Uproszczone narzędzie do zarządzania pakietami dla systemów oparych na Debianie."
content_hash: 2a6189c4937102acc6d60d1d0f8398da739ca343
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/wajig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wajig

Uproszczone narzędzie do zarządzania pakietami dla systemów oparych na Debianie.
Więcej informacji: <https://wajig.togaware.com>.

- Aktualizacja listy dostępnych pakietów i ich wersji:

`wajig update`

- Instalacja pakietu lub aktualizacja do najnowszej wersji:

`wajig install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Usunięcie pakietu i jego plików konfiguracyjnych:

`wajig purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>

- Wykonanie update, a następnie dist-upgrade:

`wajig daily-upgrade`

- Wyświetlenie rozmiaru zainstalowanych pakietów:

`wajig sizes`

- Lista wersji i dystrybucji dla wszystkich zainstalowanych pakietów:

`wajig versions`

- Lista wersji pakietów możliwych do aktualizacji:

`wajig toupgrade`

- Wyświetlenie pakietów, które posiadają zaleność od podanego pakietu:

`wajig dependents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>
