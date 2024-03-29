---
layout: page
title: osx/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: 6b37afedcab0bc85ad709fe988c94fb08492c833
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/dd.html
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

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade_usb</span>

- Clona uma unidade para outra unidade com bloco de 4 MB e ignora erro:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade_origem</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade_destino</span>` bs=4m conv=noerror`

- Gera um arquivo de 100 bytes aleatórios usando o driver aleatório do kernel:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_aleatório</span>` bs=100 count=1`

- Compara o desempenho de gravação de um disco:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_1GB</span>` bs=1024 count=1000000`
