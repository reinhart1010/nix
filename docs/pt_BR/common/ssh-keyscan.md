---
layout: page
title: common/ssh-keyscan (português (Brasil))
description: "Obter as chaves públicas SSH de hosts remotos."
content_hash: cc50344eb29ac4680fe5ca1b650b9530d4a4274f
last_modified_at: 2023-12-28
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

Obter as chaves públicas SSH de hosts remotos.
Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obtém todas as chaves públicas SSH de um host remoto:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Obtém todas as chaves públicas SSH de um host remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Obtém determinados tipos de chaves públicas SSH de um host remoto:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Atualiza manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado host:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` >> ~/.ssh/known_hosts`
