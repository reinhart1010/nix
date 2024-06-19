---
layout: page
title: linux/kill (Nederlands)
description: "Stuurt een signaal naar een proces, meestal om het proces te stoppen."
content_hash: 0d94222c3589d990c1371339f7eea16c00423c90
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Stuurt een signaal naar een proces, meestal om het proces te stoppen.
Alle signalen behalve SIGKILL en SIGSTOP kunnen door het proces worden onderschept om een nette afsluiting uit te voeren.
Meer informatie: <https://manned.org/kill>.

- Beëindig een programma met behulp van het standaard SIGTERM (terminate) signaal:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Lijst signaalwaarden en hun overeenkomstige namen op (te gebruiken zonder het `SIG` voorvoegsel):

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--table</span>

- Beëindig een achtergrondtaak:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Beëindig een programma met behulp van het SIGHUP (hang up) signaal. Veel daemons zullen herladen in plaats van beëindigen:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Beëindig een programma met behulp van het SIGINT (interrupt) signaal. Dit wordt meestal geïnitieerd door de gebruiker die `Ctrl + C` indrukt:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Signaleer het besturingssysteem om een programma onmiddellijk te beëindigen (het programma krijgt geen kans om het signaal te onderscheppen):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Signaleer het besturingssysteem om een programma te pauzeren totdat een SIGCONT ("continue") signaal wordt ontvangen:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Stuur een `SIGUSR1` signaal naar alle processen met de gegeven GID (groeps-ID):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_id</span>
