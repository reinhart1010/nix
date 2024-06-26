---
layout: page
title: linux/rcp (Nederlands)
description: "Kopieer bestanden tussen lokale en externe systemen."
content_hash: 00facb51e8c0e38505a4800380fdec84753714e1
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/linux/rcp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rcp

Kopieer bestanden tussen lokale en externe systemen.
Het imiteert het gedrag van het `cp`-commando, maar werkt tussen verschillende machines.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rcp-invocation.html>.

- Kopieer een bestand naar een externe host:

`rcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/local_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestemming/</span>

- Kopieer een directory recursief:

`rcp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/local_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestemming/</span>

- Behoud de bestandseigenschappen:

`rcp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/local_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestemming/</span>

- Forceer kopiëren zonder bevestiging:

`rcp -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/local_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestemming/</span>
