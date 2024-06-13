---
layout: page
title: common/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: 40f889f53e316caf8b9a19217936a988d2944768
last_modified_at: 2024-06-13
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
  - title: Nederlands version
    url: /nl/common/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Converte e copia um arquivo.
Mais informações: <https://manned.org/dd.1p>.

- Cria um USB drive bootável a partir de um arquivo isohybrid (como uma `archlinux-xxx.iso`):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_drive</span>

- Clona um drive para outro drive com 4 MiB block e ignora erros:

`dd bs=4194304 conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_fonte</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_destino</span>

- Gera um arquivo com um número específico de bytes aleatórios utilizando o kernel random driver:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_random</span>

- Faz o benchmark da performance de escrita de um disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_1GB</span>

- Gera um backup do sistema em um arquivo IMG e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_drive</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.img</span>` status=progress`
