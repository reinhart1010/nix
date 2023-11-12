---
layout: page
title: osx/csrutil (português (Brasil))
description: "Gerencia a configuração do System Integrity Protection (SIP)."
content_hash: 6b61d2a3577aaee374fd312248e219f068733ba0
last_modified_at: 2023-11-12
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
Mais informações: <https://ss64.com/osx/csrutil.html>.

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
