---
layout: page
title: common/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: c7f1d7e75523603ed5d0cff0a6dafa25c9188481
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/dd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/dd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Converte e copia um arquivo.
Mais informações: <https://manned.org/dd.1p>.

- Cria um dispositivo USB inicializável a partir de um arquivo isohybrid (tal como `archlinux-xxx.iso`) e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_usb</span>` status=progress`

- Clona um dispositivo para outro dispositivo com bloco de 4 MiB e descarta escritas antes que o comando termine:

`dd bs=4194304 conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_origem</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_destino</span>

- Gera um arquivo com um número específico de bytes aleatórios utilizando o driver random do kernel:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_aleatório</span>

- Faz análise do desempenho da escrita sequencial de um disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_1GB</span>

- Cria um backup do sistema, salva-o em arquivo IMG (pode ser restaurado posteriormente trocando `if` e `of`) e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.img</span>` status=progress`
