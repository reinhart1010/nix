---
layout: page
title: osx/csrutil (português (Brasil))
description: "Gerencia a configuração do System Integrity Protection (SIP)."
content_hash: 5d84e69728fd5242285f21ffb46a7fc6399e659a
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/csrutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/csrutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csrutil

Gerencia a configuração do System Integrity Protection (SIP).
Mais informações: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- Exibe o status do System Integrity Protection:

`csrutil status`

- Desabilita o System Integrity Protection:

`csrutil disable`

- Habilita o System Integrity Protection:

`csrutil enable`

- Exibe a lista de origens permitidas do NetBoot:

`csrutil netboot list`

- Adiciona um endereço IPv4 à lista de origens permitidas do NetBoot:

`csrutil netboot add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_ip</span>

- Reseta o status do System Integrity Protection e limpa a lista do NetBoot:

`csrutil clear`
