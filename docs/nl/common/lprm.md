---
layout: page
title: common/lprm (Nederlands)
description: "Annuleer wachtende printtaken van een server."
content_hash: 504a26f9f06a489a276f8cf10f9a8d4b09192505
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/lprm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lprm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lprm

Annuleer wachtende printtaken van een server.
Bekijk ook: `lpq`.
Meer informatie: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- Annuleer de huidige taak op de standaard printer:

`lprm`

- Annuleer een taak van een specifieke server:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server[:poort]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Annuleer meerdere taken met een beveiligde verbinding naar de server:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id1 taak_id2 ...</span>

- Annuleer alle taken:

`lprm -`

- Annuleer de huidige taak van een specifieke printer of klasse:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming[/instantie]</span>
