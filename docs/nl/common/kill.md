---
layout: page
title: common/kill (Nederlands)
description: "Stuurt een signaal naar een proces, meestal om het proces te stoppen."
content_hash: a62df9b34b3b5309f194fdf58de3ddd3ae43b294
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Stuurt een signaal naar een proces, meestal om het proces te stoppen.
Alle signalen behalve SIGKILL en SIGSTOP kunnen door het proces worden onderschept om een nette afsluiting uit te voeren.
Meer informatie: <https://manned.org/kill.1posix>.

- Beëindig een programma met behulp van het standaard SIGTERM (terminate) signaal:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_id</span>

- Toon beschikbare signalen (te gebruiken zonder het `SIG` voorvoegsel):

`kill -l`

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
