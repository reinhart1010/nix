---
layout: page
title: common/sha512sum (Nederlands)
description: "Bereken SHA512 cryptografische checksums."
content_hash: 8f902d0ae32db6fcb589bc4b1f18ddcb0d33cb87
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha512sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha512sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha512sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha512sum

Bereken SHA512 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA512 checksum voor één of meer bestanden:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van SHA512 checksums op in een bestand:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha512</span>

- Bereken een SHA512 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sha512sum`

- Lees een bestand met SHA512 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha512</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha512</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha512sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha512</span>

- Controleer een bekende SHA512 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_sha512_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | sha512sum --check`
