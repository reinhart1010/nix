---
layout: page
title: common/echo (Deutsch)
description: "Gib angegebene Argumente aus."
content_hash: e31312d3e82447c2ce1d1f436b65109e7e350ae8
related_topics:
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
---
# echo

Gib angegebene Argumente aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/echo>.

- Gib einen Text aus. (Hinweis: Anführungszeichen sind optional):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Welt</span>`"`

- Gib einen Text mit Umgebungsvariablen aus:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Liste aller Systempfade: $PATH</span>`"`

- Gib einen Text ohne darauffolgenden Zeilenumbruch aus:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Welt</span>`"`

- Füge einen Text in eine Datei ein:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Welt</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.txt</span>

- Ermögliche Interpretation von Fluchtsymbolen (backslash escape):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Spalte 1\tSpalte 2</span>`"`
