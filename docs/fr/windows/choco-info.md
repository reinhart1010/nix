---
layout: page
title: windows/choco-info (français)
description: "Afficher des informations détaillées sur un forfait avec Chocolatey."
content_hash: 4337b73a05d305b32b35fad74584e97911c0fdbc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-info.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-info.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-info.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-info.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-info.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-info.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-info.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco info

Afficher des informations détaillées sur un forfait avec Chocolatey.
Plus d'informations : <https://chocolatey.org/docs/commands-info>.

- Afficher des informations sur un package spécifique :

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Afficher les informations pour un package local uniquement :

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --local-only`

- Spécifier une source personnalisée à partir de laquelle recevoir des informations sur les packages :

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom d'utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot de passe</span>
