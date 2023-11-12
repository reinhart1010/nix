---
layout: page
title: osx/airport (português (Brasil))
description: "Utilitário de configuração de rede sem fio."
content_hash: b1a44c5548681d4b8472cacaca00461db55659d7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/airport.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/airport.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/airport.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/airport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airport

Utilitário de configuração de rede sem fio.
Mais informações: <https://ss64.com/osx/airport.html>.

- Mostrar informações de status da rede sem fio atual:

`airport --getinfo`

- Farejar tráfego de rede sem fio no canal 1:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Procurar redes sem fio disponíveis:

`airport --scan`

- Desassociar da rede airport atual:

`sudo airport --disassociate`
