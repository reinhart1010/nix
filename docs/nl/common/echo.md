---
layout: page
title: common/echo (Nederlands)
description: "Drukt gegeven argumenten af."
content_hash: 5f7186084c83efcea42d3e8b3deedc2fb2a8bbe7
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
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

Drukt gegeven argumenten af.
Meer informatie: <https://www.gnu.org/software/coreutils/echo>.

- Druk een tekstbericht af. Let op: aanhalingstekens zijn optimaal:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`"`

- Druk een bericht af met omgevingsvariabelen:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mijn pad is $PATH</span>`"`

- Drukt een bericht af zonder te volgen met een nieuwe regel:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`"`

- Voeg een bericht aan een bestand toe:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.txt</span>

- Schakel interpretatie van backslash ontkoming in (speciale karakters):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kolom 1\kolom 2</span>`"`
