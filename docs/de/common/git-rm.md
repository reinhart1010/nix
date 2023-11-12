---
layout: page
title: common/git-rm (Deutsch)
description: "Entferne Dateien aus dem Index des Repositories und vom lokalen Dateisystem."
content_hash: a26a01453b65c32e32508e19c0c74c378d4c99b3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rm

Entferne Dateien aus dem Index des Repositories und vom lokalen Dateisystem.
Weitere Informationen: <https://git-scm.com/docs/git-rm>.

- Entferne eine Datei aus dem Index und vom lokalen Dateisystem:

`git rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Entferne ein Verzeichnis:

`git rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Entferne eine Datei aus dem Index des Repositories, aber behalte sie lokal:

`git rm --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
