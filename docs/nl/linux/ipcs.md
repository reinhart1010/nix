---
layout: page
title: linux/ipcs (Nederlands)
description: "Toon informatie over het gebruik van System V IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays."
content_hash: 3d732962d9e8999527e183da69cb233198770cfa
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/linux/ipcs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ipcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipcs

Toon informatie over het gebruik van System V IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays.
Bekijk ook: `lsipc` voor een flexibeler tool, `ipcmk` voor het maken van IPC-faciliteiten, en `ipcrm` voor het verwijderen ervan.
Meer informatie: <https://manned.org/ipcs>.

- Toon informatie over alle actieve IPC-faciliteiten:

`ipcs`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>

- Toon volledige details over de resource met een specifieke [i]D:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--shmems|--queues|--semaphores</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_id</span>

- Toon [l]imieten in [b]ytes of in een leesbaar formaat:

`ipcs --limits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--bytes|--human</span>

- Toon s[u]mmary over huidig gebruik:

`ipcs --summary`

- Toon [c]reator's en owner's UIDs en PIDs voor alle IPC-faciliteiten:

`ipcs --creator`

- Toon de [p]ID van de laatste operatoren voor alle IPC-faciliteiten:

`ipcs --pid`

- Toon laatste toegang[s]tijden voor alle IPC-faciliteiten:

`ipcs --time`
