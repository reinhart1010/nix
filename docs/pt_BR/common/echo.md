---
layout: page
title: common/echo (português (Brasil))
description: "Imprime os argumentos passados."
content_hash: acef38857314b7a217f3272babf73c5b521a0230
last_modified_at: 2023-11-12
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

Imprime os argumentos passados.
Mais informações: <https://www.gnu.org/software/coreutils/echo>.

- Imprime uma mensagem de texto. Nota: aspas são opcionais:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Olá Mundo</span>`"`

- Imprime uma mensagem com variáveis de ambiente:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Meu caminho é $PATH</span>`"`

- Imprime uma mensagem sem adicionar uma nova linha no final:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Olá Mundo</span>`"`

- Adiciona uma mensagem no arquivo:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Olá Mundo</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.txt</span>

- Habilita interpretação dos códigos de escape após barra invertida (caracteres especiais):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Coluna 1\tColuna 2</span>`"`

- Imprime o status de saída do último comando executado (Nota: no prompt de comando do Windows e no PowerShell, os comandos equivalentes são `echo %errorlevel%` e `$lastexitcode` respectivamente):

`echo $?`
