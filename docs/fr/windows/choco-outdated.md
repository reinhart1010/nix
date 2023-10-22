---
layout: page
title: windows/choco-outdated (français)
description: "Vérifiez les packages obsolètes avec Chocolatey."
content_hash: 1cb7c2331826009b5dc7b6958a0a0a4f47773307
last_modified_at: 2023-10-22
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-outdated.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco outdated

Vérifiez les packages obsolètes avec Chocolatey.
Plus d'information: <https://chocolatey.org/docs/commands-outdated>.

- Afficher une liste des packages obsolètes sous forme de tableau :

`choco outdated`

- Ignorer les packages épinglés dans la sortie :

`choco outdated --ignore-pinned`

- Spécifiez une source personnalisée à partir de laquelle vérifier les packages :

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe}</span>
