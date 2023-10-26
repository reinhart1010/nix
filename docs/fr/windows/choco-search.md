---
layout: page
title: windows/choco-search (français)
description: "Recherchez un forfait local ou distant avec Chocolatey."
content_hash: 95e54c4d8c85bc85087774b9bd24dca09eb7fdb2
last_modified_at: 2023-10-26
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-search.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-search.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-search.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-search.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-search.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco search

Recherchez un forfait local ou distant avec Chocolatey.
Plus d'information: <https://chocolatey.org/docs/commands-search>.

- Rechercher un forfait :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>

- Rechercher un package localement :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>` --local-only`

- Inclure uniquement les correspondances exactes dans les résultats :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>` --exact`

- Confirmer automatiquement toutes les invites :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>` --yes`

- Spécifiez une source personnalisée dans laquelle rechercher des packages :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requête</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom d'utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot de passe</span>
