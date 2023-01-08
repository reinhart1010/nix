---
layout: page
title: common/eslint (Deutsch)
description: "Ein erweiterbarer Linter für JavaScript und JSX."
content_hash: bf88c0cb87643b10a779553fb5b494cd1ff9b84e
last_modified_at: 2022-12-21
related_topics:
  - title: English version
    url: /en/common/eslint.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/eslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/eslint.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># eslint

Ein erweiterbarer Linter für JavaScript und JSX.
Weitere Informationen: <https://eslint.org>.

- Erstelle eine ESLint-Konfigurationsdatei:

`eslint --init`

- Linte Dateien:

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1.js pfad/zu/datei2.js ...</span>

- Behebe Lintingfehler:

`eslint --fix`

- Linte mit einer Konfigurationsdatei:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfigurationsdatei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quellordner}`