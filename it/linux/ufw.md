---
layout: page
title: linux/ufw (italiano)
description: "ufw (Uncomplicated Firewall) - Firewall Semplice."
content_hash: 58612d3484ea7db22be6bd640c913d71113fec19
related_topics:
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
---
# ufw

ufw (Uncomplicated Firewall) - Firewall Semplice.
Frontend per iptables per semplificare la configurazione di un firewall.
Maggiori informazioni: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Accendi ufw:

`ufw enable`

- Spegni ufw:

`ufw disable`

- Mostra le regole di ufw, con i numeri corrispondenti:

`ufw status numbered`

- Aperto al traffico in entrata sulla porta 5432, con un commento che identifica il servizio:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servizio</span>`"`

- Aperto solo al traffico TCP da 192.168.0.4 a qualsiasi indirizzo su questo host, sulla porta 22:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Blocchi traffico su porta 80 su questo host:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Nega tutto il traffico UDP alla porta 22:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Elimina una regola particolare. Il numero della regola può essere trovato con "ufw status numbered":

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_della_regola</span>
