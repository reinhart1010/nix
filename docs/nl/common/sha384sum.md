---
layout: page
title: common/sha384sum (Nederlands)
description: "Bereken SHA384 cryptografische checksums."
content_hash: 46c3077b5ada4828df293c90afcc026658b01286
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/common/sha384sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha384sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha384sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha384sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha384sum

Bereken SHA384 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA384 checksum voor één of meer bestanden:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van SHA384 checksums op in een bestand:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha384</span>

- Bereken een SHA384 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sha384sum`

- Lees een bestand met SHA384 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha384sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha384</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha384sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha384</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha384sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha384</span>

- Controleer een bekende SHA384 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_sha384_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | sha384sum --check`
