---
layout: page
title: common/killall (Nederlands)
description: "Verstuur een kill-signaal naar alle instanties van een proces op naam (moet exact overeenkomen)."
content_hash: d8dd871dd9f33b486d7a5f11cf3a7ac1822e97b7
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/killall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# killall

Verstuur een kill-signaal naar alle instanties van een proces op naam (moet exact overeenkomen).
Alle signalen behalve SIGKILL en SIGSTOP kunnen door het proces worden onderschept, waardoor een nette afsluiting mogelijk is.
Meer informatie: <https://manned.org/killall>.

- Beëindig een proces met behulp van het standaard SIGTERM (terminate) signaal:

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>

- [l]ijst beschikbare signaalnamen (te gebruiken zonder het 'SIG'-voorvoegsel):

`killall -l`

- Vraag interactief om bevestiging voordat het proces wordt beëindigd:

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>

- Beëindig een proces met het SIGINT (interrupt) signaal, hetzelfde signaal dat wordt verzonden door `Ctrl + C` in te drukken:

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>

- Forceer het beëindigen van een proces:

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_naam</span>
