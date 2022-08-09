---
layout: page
title: common/autojump (français)
description: "Accède rapidement aux dossiers que vous visitez le plus."
content_hash: cad83c3557446015815771e44e8241639afcf1b1
related_topics:
  - title: English version
    url: /en/common/autojump.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autojump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autojump

Accède rapidement aux dossiers que vous visitez le plus.
Les alias comme j or jc sont fournis pour simplifier leurs utilisation.
Plus d'informations : <https://github.com/wting/autojump>.

- Accède à un dossier qui contiens le motif suivant :

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>

- Accède à un sous-dossier (enfant) du repertoire courant qui contiens the motif suivant :

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>

- Ouvre le dossier qui contiens the motif suivant dans le gestionnaire de fichier du système d'exploitation :

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motif</span>

- Enlève les dossiers qui n'existent plus de la base de données de autojump :

`j --purge`

- Affiche les entrées dans la base de données de autojump :

`j -s`
