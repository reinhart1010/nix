---
layout: page
title: common/consul-kv (italiano)
description: "Rete distribuita per gestire e configurare servizi tramite database chiave-valore."
content_hash: b436bc42346d18727a204459038d85d4017360ea
related_topics:
  - title: English version
    url: /en/common/consul-kv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/consul-kv.html
    icon: bi bi-globe
---
# consul-kv

Rete distribuita per gestire e configurare servizi tramite database chiave-valore.
Maggiori informazioni: <https://learn.hashicorp.com/consul/getting-started/kv>.

- Leggi il valore di una chiave da un database chiave-valore:

`consul kv get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave</span>

- Memorizza una nuova coppia chiave-valore:

`consul kv put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore</span>

- Elimina una coppia chiave-valore:

`consul kv delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave</span>
