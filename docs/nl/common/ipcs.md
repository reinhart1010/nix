---
layout: page
title: common/ipcs (Nederlands)
description: "Toon informatie over het gebruik van XSI IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays."
content_hash: 6e75892696d9310c07ab77363e000e735d24ce99
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/ipcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipcs

Toon informatie over het gebruik van XSI IPC-faciliteiten: gedeelde geheugensegmenten, berichtenwachtrijen en semafoorarrays.
Meer informatie: <https://manned.org/ipcs.1p>.

- Toon informatie over alle IPC:

`ipcs -a`

- Toon informatie over actieve gedeelde [m]emory-segmenten, berichten[q]ueues of [s]emaphore-sets:

`ipcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|-q|-s</span>

- Toon informatie over de maximaal toegestane grootte in [b]ytes:

`ipcs -b`

- Toon de gebruikersnaam en groepsnaam van de [c]reator voor alle IPC-faciliteiten:

`ipcs -c`

- Toon de [p]ID van de laatste operatoren voor alle IPC-faciliteiten:

`ipcs -p`

- Toon toegang[s]tijden voor alle IPC-faciliteiten:

`ipcs -t`

- Toon [o]utstanding gebruik voor actieve berichtenwachtrijen en gedeelde geheugensegmenten:

`ipcs -o`
