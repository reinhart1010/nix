---
layout: page
title: common/sha224sum (Nederlands)
description: "Bereken SHA224 cryptografische checksums."
content_hash: 3f30fc2a6b91e2f9d6faf107d1e782cae1296578
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/sha224sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha224sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha224sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha224sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha224sum

Bereken SHA224 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA224 checksum voor één of meer bestanden:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van SHA224 checksums op in een bestand:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha224</span>

- Bereken een SHA224 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sha224sum`

- Lees een bestand met SHA224 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha224sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha224</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha224sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha224</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha224sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha224</span>

- Controleer een bekende SHA224 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_sha224_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | sha224sum --check`
