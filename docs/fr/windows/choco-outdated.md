---
layout: page
title: windows/choco-outdated (français)
description: "Vérifiez les packages obsolètes avec Chocolatey."
content_hash: e8aa829919a81e1d7384e8fa917dc66778a4233e
last_modified_at: 2023-12-27
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
tldri18n_status: 2
---
# choco outdated

Vérifiez les packages obsolètes avec Chocolatey.
Plus d'informations : <https://chocolatey.org/docs/commands-outdated>.

- Afficher une liste des packages obsolètes sous forme de tableau :

`choco outdated`

- Ignorer les packages épinglés dans la sortie :

`choco outdated --ignore-pinned`

- Spécifiez une source personnalisée à partir de laquelle vérifier les packages :

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Fournir un nom d'utilisateur et un mot de passe pour l'authentification :

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>
