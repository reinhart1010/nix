---
layout: page
title: common/nmap (italiano)
description: "Nmap è un tool per port scanning ed esplorazione di rete."
content_hash: e7121a8b72d3b143c656d629474bb462d6747503
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmap

Nmap è un tool per port scanning ed esplorazione di rete.
Alcune funzionalità diventano attive solamente con privilegi d'amministratore.
Maggiori informazioni: <https://nmap.org>.

- Controlla se un indirizzo IP è attivo, e indovina il suo sistema operativo:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nome_host</span>

- Cerca di determinare se gli host specificati sono attivi e quali sono i loro nomi:

`nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nome_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opzionale_altro_indirizzo</span>

- Come sopra, ma esegui una scansione della porta TCP predefinita 1000 se l'host sembra attivo:

`nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nome_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opzionale_altro_indirizzo</span>

- Attiva scripts, segnalazione di servizi, OS fingerprinting e traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Velocizza esecuzione dando per scontato una buona connessione di rete:

`nmap -T4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Scansiona una specifica lista di porte (usa `-p-` per tutte le porte `1-65535`):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta1,porta2,…,portaN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Esegui scansione TCP e UDP (usa `-sU` per usare solo UDP, `-sZ` per SCTP, `-sO` per IP):

`nmap -sSU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Determina vulnerabilità e informazioni di un host eseguendo una scansione di tutte le porte, servizi e versioni con tutti gli script di default NSE attivi:

`nmap -sC -sV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>
