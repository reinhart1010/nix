---
layout: page
title: osx/airport (italiano)
description: "Strumento di configurazione delle reti senza fili."
content_hash: 7d161c72d1f8334f6b8aa62f91b62d84b8f1bda8
last_modified_at: 2023-11-12
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

`airport -I`

- Intercetta il traffico delle connessioni senza fili sul primo canale:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Ricerca le reti senza fili disponibili:

`airport -s`

- Disassocia dalla rete airport corrente:

`sudo airport -z`
