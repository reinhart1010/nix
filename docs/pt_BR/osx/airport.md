---
layout: page
title: osx/airport (português (Brasil))
description: "Utilitário de configuração de rede sem fio."
content_hash: ff57436827d1bdd237b60239bb35288066e47f66
last_modified_at: 2024-01-31
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
Mais informações: <https://keith.github.io/xcode-man-pages/airport.1.html>.

- Mostra informações de status da rede sem fio atual:

`airport --getinfo`

- Fareja tráfego de rede sem fio no canal 1:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Procura redes sem fio disponíveis:

`airport --scan`

- Desassocia da rede airport atual:

`sudo airport --disassociate`
