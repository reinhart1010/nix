---
layout: page
title: linux/dos2unix (català)
description: "Canvia salts de línia amb format DOS a salts de línia amb format Unix."
content_hash: 32e045467feea647d9aa61dea7567532096e63df
last_modified_at: 2024-08-31
related_topics:
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dos2unix

Canvia salts de línia amb format DOS a salts de línia amb format Unix.
Reemplaça CRLF amb LF.
Més informació: <https://manned.org/dos2unix>.

- Canvia els salts de línia en un arxiu:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_del_arxiu</span>

- Crea una còpia amb salts de línia en format Unix:

`dos2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_del_arxiu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nou_nom_del_arxiu</span>
