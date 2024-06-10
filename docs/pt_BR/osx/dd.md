---
layout: page
title: osx/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: 80eb04701445988183e8875bb0cc8dfa4418555d
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dd

Converte e copia um arquivo.
Mais informações: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Cria uma unidade USB inicializável a partir de um arquivo isohybrid (tal como `archlinux-xxx.iso`):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidade_usb</span>

- Clona uma unidade para outra unidade com bloco de 4 MB e ignora qualquer erro:

`dd bs=4m conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidade_origem</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/unidade_destino</span>

- Gera um arquivo de número específico de bytes aleatórios usando o driver aleatório do kernel:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_aleatório</span>

- Compara o desempenho de gravação de um disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_1GB</span>
