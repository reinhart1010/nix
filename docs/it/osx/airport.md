---
layout: page
title: osx/airport (italiano)
description: "Strumento di configurazione delle reti senza fili."
content_hash: dc6074d3f88c87aba01a07fff889abcc208f8f9b
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/osx/airport.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/airport.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/airport.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/airport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airport

Strumento di configurazione delle reti senza fili.
Maggiori informazioni: <https://ss64.com/osx/airport.html>.

- Mostra le informazioni relative allo stato attuale delle connessioni senza fili:

`airport --getinfo`

- Intercetta il traffico delle connessioni senza fili sul primo canale:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Ricerca le reti senza fili disponibili:

`airport --scan`

- Disassocia dalla rete airport corrente:

`sudo airport --disassociate`
