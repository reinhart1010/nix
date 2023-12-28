---
layout: page
title: common/arp-scan (português (Brasil))
description: "Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nome de domínio) em uma rede local, identificando as máquinas ativas de acordo com as respostas."
content_hash: 43db2691f4f7cba83cb3f516cc6b70fe4be53cae
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/arp-scan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp-scan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arp-scan

Envia pacotes ARP para máquinas (identificadas por endereço IP ou por nome de domínio) em uma rede local, identificando as máquinas ativas de acordo com as respostas.
Mais informações: <https://github.com/royhills/arp-scan>.

- Verifica as máquinas da rede local:

`arp-scan --localnet`

- Verifica as máquinas de uma rede IP especificando a máscara de bit:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Verifica as máquinas de uma rede IP que estão em uma faixa de valores:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- Verifica as máquinas de uma rede IP especificando a máscara de rede:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
