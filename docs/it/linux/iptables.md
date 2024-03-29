---
layout: page
title: linux/iptables (italiano)
description: "Programma che permette di configurare tabelle, catene e regole fornite dal firewall del kernel Linux."
content_hash: 32665effa371109e8c8efd4e5f5abb6369613e9f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/iptables.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/iptables.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># iptables

Programma che permette di configurare tabelle, catene e regole fornite dal firewall del kernel Linux.
Maggiori informazioni: <https://manned.org/iptables>.

- Visualizza catene, regole e contatori di pacchetti/byte per la tabella dei filtri:

`sudo iptables -vnL`

- Imposta regola ad una catena:

`sudo iptables -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">catena</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regola</span>

- Appendi regola ad una catena di policy per IP:

`sudo iptables -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">catena</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regola</span>

- Appendi regola ad una catena di policy per IP considerando protocollo e porta:

`sudo iptables -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">catena</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocollo</span>` --dport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regola</span>

- Cancella regola da una catena:

`sudo iptables -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">catena</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_linea_della_regola</span>

- Salva la configurazione di ip tables di una specifica tabella in un file:

`sudo iptables-save -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome tabella</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_iptables</span>

- Ripristina la configurazione di iptables da un file:

`sudo iptables-restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_iptables</span>
