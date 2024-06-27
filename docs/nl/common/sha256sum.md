---
layout: page
title: common/sha256sum (Nederlands)
description: "Bereken SHA256 cryptografische checksums."
content_hash: 75b0fc6d521ce914f3ddeb22851a1e0bf6cabb06
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/sha256sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha256sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha256sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha256sum

Bereken SHA256 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Bereken de SHA256 checksum voor één of meer bestanden:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van SHA256 checksums op in een bestand:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha256</span>

- Bereken een SHA256 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | sha256sum`

- Lees een bestand met SHA256 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`sha256sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha256</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`sha256sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha256</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`sha256sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.sha256</span>
