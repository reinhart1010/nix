---
layout: page
title: common/echo (français)
description: "Affiche les paramètres donnés dans la console."
content_hash: 622d7c940f6dfe7f9225cdf631e00a59aa838dee
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
  - title: српски version
    url: /sr/common/echo.html
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

Affiche les paramètres donnés dans la console.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Affiche un message (les guillemets sont facultatifs) :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Affiche un message avec des variables d'environnement :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ma variable PATH est $PATH</span>`"`

- Affiche un message sans retour à la ligne :

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`"`

- Ajoute un message à un fichier :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.txt</span>

- Active l'interprétation des spécificateurs d'échappement :

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Colonne 1\tColonne 2</span>`"`
