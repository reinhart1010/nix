---
layout: page
title: common/b2sum (Nederlands)
description: "Bereken BLAKE2 cryptografische checksums."
content_hash: 6d8a4f95789fdb9f448e3aafed3170dc0260d3fb
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b2sum

Bereken BLAKE2 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Bereken de BLAKE2 checksum voor een of meerdere bestanden:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van BLAKE2 checksums op in een bestand:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.b2</span>

- Bereken de BLAKE2 checksum voor `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | b2sum`

- Lees een bestand van BLAKE2 sums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.b2</span>

- Toon alleen een melding voor missende bestanden of als verificatie faalt:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.b2</span>

- Toon alleen een melding als een verificatie faalt en negeer missende bestanden:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.b2</span>

- Controleer een bekende BLAKE2 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_blake2_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | b2sum --check`
