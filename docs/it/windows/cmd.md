---
layout: page
title: windows/cmd (italiano)
description: "L'interprete dei comandi di Windows."
content_hash: e555c120a7ddf222f78d3bbe82ba48cd3b6a5978
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
---
# cmd

L'interprete dei comandi di Windows.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Lancia una nuova istanza dell'interprete dei comandi:

`cmd`

- Esegue il comando specificato e poi esce:

`cmd /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Esegue il comando specificato e poi apre una shell interattiva:

`cmd /k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Disabilita l'uso di `echo` nell'output di un comando:

`cmd /q`

- Abilita o disabilita le estensioni ai comandi:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Abilita o disabilita l'autocompletamento dei nomi di file e directory:

`cmd /f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Abilita o disabilita l'espansione delle variabili d'ambiente:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Forza l'encoding delle stringhe in Unicode per l'output:

`cmd /u`
