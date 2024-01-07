---
layout: page
title: windows/cmd (português (Brasil))
description: "O interpretador de comandos do Windows."
content_hash: b6ff6759af8b2d00d5c3d192fe6e48fd6615342a
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmd

O interpretador de comandos do Windows.
Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia uma sessão do interpretador de comandos:

`cmd`

- Executa os [c]omandos especificados:

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Olá Mundo</span>

- Executa um script específico:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.bat</span>

- Executa o comando especificado e entra em um shell interativo:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Olá Mundo</span>

- Entra em um shell interativo e desabilita o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Entra em um shell interativo com ou a expansão de [v]ariáveis de ambiente habilitada ou desabilitada:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Entra em um shell interativo com a extensão de comandos habilitada ou desabilitada:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Entra em um shell interativo com a saída de comandos no padrão Unicode:

`cmd /u`
