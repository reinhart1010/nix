---
layout: page
title: common/git-am (Deutsch)
description: "Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail."
content_hash: c4546f38b0b0fa16b31cf45754661debf10ad496
related_topics:
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
---
# git am

Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail.
Siehe auch `git format-patch` zur Erzeugung von Patch-Dateien.
Weitere Informationen: <https://git-scm.com/docs/git-am>.

- Integriere eine Patch-Datei:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.patch</span>

- Brich das Integrieren einer Patch-Datei ab:

`git am --abort`

- Integriere so viele Patch-Dateien wie möglich und speichere fehlgeschlagene Teile:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.patch</span>
