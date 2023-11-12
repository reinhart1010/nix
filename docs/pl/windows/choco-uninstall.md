---
layout: page
title: windows/choco-uninstall (polski)
description: "Odinstalowanie jednego lub więcej pakietów zarządzanych przez Chocolatey."
content_hash: b35b41bbe633c5c031fbe205fb89acef54c0f61f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco uninstall

Odinstalowanie jednego lub więcej pakietów zarządzanych przez Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-uninstall>.

- Odinstalowanie jednego lub więcej pakietów (oddzielonych spacją):

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{pakiet(pakietów)</span>

- Odinstalowanie konkretnej wersji pakietu:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wersja</span>

- Automatyczna akceptacja wszystkich monitów podczas deinstalacji pakietu:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --yes`

- Odinstalowanie wszystkich zależności podczas procesu deinstalacji danego pakietu/pakietów:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakiet</span>` --remove-dependencies`

- Odinstalowanie wszystkich pakietów:

`choco uninstall all`
