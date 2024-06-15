---
layout: page
title: common/git-am (Deutsch)
description: "Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail."
content_hash: 91aacf3845d7e7257cb130a4d080e80de838dc18
last_modified_at: 2024-06-15
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
  - title: Indonesia version
    url: /id/common/git-am.html
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
tldri18n_status: 2
---
# git am

Patch-Dateien integrieren. Nützlich beim Empfang von Commits per E-Mail.
Siehe auch `git format-patch` zur Erzeugung von Patch-Dateien.
Weitere Informationen: <https://git-scm.com/docs/git-am>.

- Integriere eine Patch-Datei:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.patch</span>

- Herunterladen und Integrieren einer Patch-Datei:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://beispiel.de/datei.patch</span>` | git apply`

- Brich das Integrieren einer Patch-Datei ab:

`git am --abort`

- Integriere so viele Patch-Dateien wie möglich und speichere fehlgeschlagene Teile:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.patch</span>
