---
layout: page
title: linux/dd (português (Brasil))
description: "Converte e copia um arquivo."
content_hash: 1fdee7aec767a7353318bea84f0c3ae30b15828e
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/linux/dd.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Converte e copia um arquivo.
Mais informações: <https://www.gnu.org/software/coreutils/dd>.

- Cria um dispositivo USB inicializável a partir de um arquivo isohybrid (como `archlinux-xxx.iso`), e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_usb</span>` status=progress`

- Clona um dispositivo para outro dispositivo com blocos de 4MiB e salva em disco antes de o comando finalizar a execução:

`dd bs=4M conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_origem</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_destino</span>

- Gera uma arquivo com um número específico de bytes aleatórios, usando o dispositivo aleatório do kernel:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_aleatorio</span>

- Cria um benchmark do desempenho de escrita de um disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_1GB</span>

- Cria uma cópia de segurança do sistema, salva em um arquivo IMG (pode ser restaurado depois trocando o valor de `if` com o de `of`), e mostra o progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dispositivo_de_origem</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.img</span>` status=progress`

- Verifica o progresso de uma operação `dd` que está acontecendo (execute esse comando em outro terminal):

`kill -USR1 $(pgrep -x dd)`
