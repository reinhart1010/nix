---
layout: page
title: common/echo (српски)
description: "Prikazuje date argumente."
content_hash: fd0882e41391be002c7b88ac9854255149398a65
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/echo.html
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
  - title: русский version
    url: /ru/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># echo

Prikazuje date argumente.
Više informacija na: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Prikazuje tekstualnu poruku. Napomena: navodnici su opcionalni:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zdravo Svete</span>`"`

- Prikazuje poruku sa promenljivom:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Moja lokacija je $PATH</span>`"`

- Prikazuje poruku bez dodatne linije:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zdravo Svete</span>`"`

- Dodaje poruku u fajl:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zdravo Svete</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fajl.txt</span>

- Omogućava interpretaciju posebnih karektera (prethodi im "\\"):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Kolona 1\tKolona 2</span>`"`
