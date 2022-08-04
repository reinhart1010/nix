---
layout: page
title: windows/cmd (português (Brasil))
description: "O interpretador de comandos do Windows."
content_hash: 270ace42b4fa72cdfc96e36e4ea7f121e7d050f8
related_topics:
  - title: English version
    url: /en/windows/cmd.html
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
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
---
# cmd

O interpretador de comandos do Windows.
Mais informações: <https://docs.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Iniciar nova instância do interpretador de comandos:

`cmd`

- Executar o comando especificado e sair do interpretador:

`cmd /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Executar o comando especificado e entrar no shell interativo:

`cmd /k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Desabilitar o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Habilitar ou desabilitar extensão de comandos:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Habilitar ou desabilitar a ferramenta que completa automaticamente o nome de arquivos ou diretórios:

`cmd /f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Habilitar ou desabilitar a expansão de variáveis de ambiente:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Forçar que a saída de comandos use o padrão Unicode:

`cmd /u`
