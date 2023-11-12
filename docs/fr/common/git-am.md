---
layout: page
title: common/git-am (français)
description: "Appliquer des fichiers de \"patch\" Git. Utile lorsque l'on reçoit des commits par email."
content_hash: e152fd5f57df8eba9a75d9c10dcb01942a2ee409
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git am

Appliquer des fichiers de "patch" Git. Utile lorsque l'on reçoit des commits par email.
Voir aussi `git format-patch`, pour générer des fichiers de patch.
Plus d'informations : <https://git-scm.com/docs/git-am>.

- Appliquer un fichier de patch :

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.patch</span>

- Annuler l'application d'un fichier de patch :

`git am --abort`

- Appliquer autant de fichiers de correctif que possible, en enregistrant les morceaux échoués pour rejeter le fichier :

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.patch</span>
