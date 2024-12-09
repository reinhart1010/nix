---
layout: page
title: common/sha1sum (Nederlands)
description: "Bereken SHA1 cryptografische checksums."
content_hash: f038d696d0acce32139161fd6661e3267f37f4cf
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/sha1sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha1sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha1sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha1sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha1sum

Bereken SHA1 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/sha1sum>.

- Bereken de SHA1 checksum voor één of meer bestanden:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van SHA1 checksums op in een bestand:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha1</span>

- Bereken een SHA1 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sha1sum`

- Lees een bestand met SHA1 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha1sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha1</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha1sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha1</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha1sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha1</span>

- Controleer een bekende SHA1 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_sha1_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | sha1sum --check`
