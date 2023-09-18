---
layout: page
title: common/ssh-keyscan (português (Brasil))
description: "Obter as chaves públicas SSH de hosts remotos."
content_hash: a1a624f99891ec32cf727485ebcf8c17f66e6acb
last_modified_at: 2023-09-18
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ssh-keyscan

Obter as chaves públicas SSH de hosts remotos.
Mais informações: <https://man.openbsd.org/ssh-keyscan>.

- Obter todas as chaves públicas SSH de um host remoto:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Obter todas as chaves públicas SSH de um host remoto que esteja ouvindo em uma porta específica:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Obter determinados tipos de chaves públicas SSH de um host remoto:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Atualizar manualmente o arquivo known_hosts do SSH com a impressão digital de um determinado host:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` >> ~/.ssh/known_hosts`
