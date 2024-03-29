---
layout: page
title: windows/choco-uninstall (français)
description: "Désinstallez un ou plusieurs packages avec Chocolatey."
content_hash: 36fa9ef1f4fc4aacdcb5d212bd63f26a23e9922b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-uninstall.html
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

Désinstallez un ou plusieurs packages avec Chocolatey.
Plus d'informations : <https://chocolatey.org/docs/commands-uninstall>.

- Désinstaller un ou plusieurs packages séparés par des espaces :

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet1 paquet2 ...</span>

- Désinstaller une version spécifique d'un package :

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Confirmer automatiquement toutes les invites :

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --yes`

- Supprimez toutes les dépendances lors de la désinstallation :

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --remove-dependencies`

- Désinstaller tous les packages :

`choco uninstall all`
