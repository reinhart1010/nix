---
layout: page
title: linux/ark (français)
description: "Outil d'archive de KDE."
content_hash: ab8b2cb28c027cbcc21dd1c582ff9792c33cbf58
last_modified_at: 2022-12-29
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

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Change le répertoire d'extraction :

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>

- Crée une archive si elle n'existe pas et y ajouter des fichiers :

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier2</span>` ...`
