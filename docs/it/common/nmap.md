---
layout: page
title: common/nmap (italiano)
description: "Nmap è un tool per port scanning ed esplorazione di rete."
content_hash: 523c4514eb5952caf58694e3c934c08b6f7c1336
last_modified_at: 2024-05-06
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmap

Nmap è un tool per port scanning ed esplorazione di rete.
Alcune funzionalità diventano attive solamente con privilegi d'amministratore.
Maggiori informazioni: <https://nmap.org/book/man.html>.

- Controlla se un indirizzo IP è attivo, e indovina il suo sistema operativo:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nome_host</span>

- Cerca di determinare se gli host specificati sono attivi e quali sono i loro nomi:

`sudo nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nome_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opzionale_altro_indirizzo</span>

- Attiva scripts, segnalazione di servizi, OS fingerprinting e traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Scansiona una specifica lista di porte (usa `-p-` per tutte le porte `1-65535`):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta1,porta2,…,portaN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>

- Determina vulnerabilità e informazioni di un host eseguendo una scansione di tutte le porte, servizi e versioni con tutti gli script di default NSE attivi:

`nmap -sC -sV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_o_indirizzi</span>
