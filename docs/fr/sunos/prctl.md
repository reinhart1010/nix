---
layout: page
title: sunos/prctl (français)
description: "Obtenir ou définir les contrôles de ressources des processus, tâches et projets en cours d'exécution."
content_hash: c356096557284fee2beff0153bf7c0c177f42546
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prctl

Obtenir ou définir les contrôles de ressources des processus, tâches et projets en cours d'exécution.
Plus d'information : <https://www.unix.com/man-page/sunos/1/prctl>.

- Examiner les limites et les autorisations des processus :

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Examiner les limites et les autorisations de processus dans un format analysable par machine :

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Obtenir une limite spécifique pour un processus en cours d'exécution :

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
