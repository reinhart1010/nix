---
layout: page
title: common/echo (Nederlands)
description: "Toont gegeven argumenten."
content_hash: a3e01c905c1ae6ad86412f45f11ec732f7a5979f
last_modified_at: 2024-06-19
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
tldri18n_status: 2
---
# echo

Toont gegeven argumenten.
Meer informatie: <https://www.gnu.org/software/coreutils/echo>.

- Toon een tekstbericht. Let op: aanhalingstekens zijn optioneel:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`"`

- Toon een bericht met omgevingsvariabelen:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mijn pad is $PATH</span>`"`

- Toont een bericht zonder te volgen met een nieuwe regel:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`"`

- Voeg een bericht aan een bestand toe:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo Wereld</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.txt</span>

- Interpretatie van backslash-escapes (speciale tekens) inschakelen:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kolom 1\kolom 2</span>`"`

- Toon de afsluitstatus van de laatst uitgevoerde opdracht (Let op: in Windows Command Prompt en PowerShell zijn de equivalente opdrachten respectievelijk `echo %errorlevel%` en `$lastexitcode`):

`echo $?`
