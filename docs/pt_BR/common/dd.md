---
layout: page
title: common/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: 7b9f16c93916366b20543a680706022656687c55
related_topics:
  - title: Deutsch version
    url: /de/common/dd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dd

Converte e copia um arquivo.
Mais informações: <https://www.gnu.org/software/coreutils/dd>.

- Cria um USB drive bootável a partir de um arquivo isohybrid (como uma archlinux-xxx.iso) e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb_drive</span>` status=progress`

- Clona um drive para outro drive com 4 MiB block, ignora erros e mostra o progresso:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_fonte</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drive_destino</span>` bs=4M conv=noerror status=progress`

- Gera um arquivo com 100 bytes aleatórios utilizando o kernel random driver:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_random</span>` bs=100 count=1`

- Faz o benchmark da performance de escrita de um disco:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_1GB</span>` bs=1024 count=1000000`

- Gera um backup do sistema em um arquivo IMG e mostra o progresso:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo_drive</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.img</span>` status=progress`

- Restaura um drive a partir de um arquivo IMG e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.img</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo_drive</span>` status=progress`

- Checa o progresso de um processo dd rodando (rode esse comando de outro shell):

`kill -USR1 $(pgrep ^dd)`