---
layout: page
title: linux/ark (français)
description: "Outil d'archive de KDE."
content_hash: 9e25da66db761b7a5a2e30904a8ed94496a387cb
last_modified_at: 2023-05-23
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ark.html
    icon: bi bi-globe
---
# ark

Outil d'archive de KDE.
Plus d'informations : <https://docs.kde.org/stable5/en/ark/ark/>.

- Extrait une archive dans le répertoire courant :

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive</span>

- Change le répertoire d'extraction :

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive</span>

- Crée une archive si elle n'existe pas et y ajouter des fichiers :

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1 chemin/vers/fichier2 ...</span>
