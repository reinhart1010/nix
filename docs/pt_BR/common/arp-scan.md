---
layout: page
title: common/arp-scan (português (Brasil))
description: "Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nome de domínio) em uma rede local, identificando as máquinas ativas de acordo com as respostas."
content_hash: 3110f29f8eafb9dfe76c31d81b7f67c47b671148
related_topics:
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
---
# arp-scan

Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nome de domínio) em uma rede local, identificando as máquinas ativas de acordo com as respostas.
Mais informações: <https://github.com/royhills/arp-scan>.

- Verificar as máquinas da rede local:

`arp-scan --localnet`

- Verificar as máquinas de uma rede IP especificando a máscara de bit:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Verificar as máquinas de uma rede IP que estejam em uma faixa de valores:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- Verificar as máquinas de uma rede IP especificando a máscara de rede:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
