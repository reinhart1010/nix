---
layout: page
title: linux/dex (français)
description: "DesktopEntry Execution est un programme servant à générer et à exécuter des fichiers DesktopEntry de type Application"
content_hash: 8c99742cf75eefbb6b838031af4700dfd6f5317c
related_topics:
  - title: English version
    url: /en/linux/dex.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dex

DesktopEntry Execution est un programme servant à générer et à exécuter des fichiers DesktopEntry de type Application
Plus d'information : <https://github.com/jceb/dex>.

- Exécute tous les programmes dans les dossiers de démarrage automatique :

`dex --autostart`

- Exécute tous les programmes dans les dossiers spécifiés :

`dex --autostart --search-paths `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chermin/vers/dossier3</span>`:`

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique spécifique à GNOME :

`dex --autostart --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GNOME</span>

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique standard :

`dex --autostart --dry-run`

- Prévisualise la valeur de la propriété `Name` de DesktopEntry :

`dex -- property `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.desktop</span>

- Crée une DesktopEntry pour un programme dans le dossier courant :

`dex --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.destkop</span>

- Exécute un programme (avec `Terminal=true` dans le fichier Desktop) dans le terminal donné :

`dex --term `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.desktop</span>
