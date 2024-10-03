---
layout: page
title: windows/cd (português (Brasil))
description: "Exibe o nome o diretório local atual ou altera para um diretório diferente."
content_hash: 0924a720460c347750e1fc587735bd252b619dce
last_modified_at: 2024-10-03
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cd

Exibe o nome o diretório local atual ou altera para um diretório diferente.
No PowerShell, este comando é um apelido de `Set-Location`. Esta documentação é baseada na versão Prompt de Comando (`cmd`) do `cd`.
Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Exibe documentação sobre o comando equivalente do PowerShell:

`tldr set-location`

- Mostra o nome do diretório atual:

`cd`

- Vai para um diretório específico na mesma unidade:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho\para\diretorio</span>

- Vai para um diretório específico em uma unidade diferente:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho\para\diretório</span>

- Vai até o pai do diretório atual:

`cd ..`

- Vai para o diretório base do usuário atual:

`cd %userprofile%`

- Vai para a raiz da unidade atual:

`cd \`
