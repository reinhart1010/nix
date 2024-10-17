---
layout: page
title: common/ssh-keyscan (português (Brasil))
description: "Obter as chaves públicas SSH de servidores remotos."
content_hash: 637e7b5453f3f61ccefdfca6fc0b67cf7c6afcee
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keyscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-keyscan

Obter as chaves públicas SSH de servidores remotos.
Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obtém todas as chaves públicas SSH de um servidor remoto:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>

- Obtém todas as chaves públicas SSH de um servidor remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>

- Obtém determinados tipos de chaves públicas SSH de um servidor remoto:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>

- Atualiza manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado servidor:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` >> ~/.ssh/known_hosts`
