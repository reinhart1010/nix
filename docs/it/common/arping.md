---
layout: page
title: common/arping (italiano)
description: "Scopri e interroga host in una rete utilizzando il protocollo ARP."
content_hash: 98b43a6484838ff832601bdcd80c8fffd367daae
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/arping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/arping.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arping

Scopri e interroga host in una rete utilizzando il protocollo ARP.
Utile per scoprire indirizzi MAC.
Maggiori informazioni: <https://github.com/ThomasHabets/arping>.

- Invia un ping ad un host inviando pacchetti ARP request:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_host</span>

- Invia un pint ad un host su una specifica interfaccia:

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaccia</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_host</span>

- Invia un ping ad un host e termina all prima risposta:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_host</span>

- Invia uno specifico numero di ping:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_host</span>

- Invia pacchetti ARP request in broadcast per aggiornare la cache ARP dei vicini:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_da_inviare_in_broadcast</span>

- Rileva indirizzi IP duplicati nella rete inviando richieste ARP con un timeout di 3 secondi:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_da_controllare</span>
