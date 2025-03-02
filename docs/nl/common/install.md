---
layout: page
title: common/install (Nederlands)
description: "Kopieer bestanden en stel attributen in."
content_hash: e9701dd9b45cfa6670f90efb3dfc01ebb5aaab11
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# install

Kopieer bestanden en stel attributen in.
Kopieer bestanden (vaak uitvoerbare) naar een systeemlocatie zoals `/usr/local/bin` en geef ze de juiste permissies/eigendom.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Kopieer bestanden naar de bestemming:

`install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>

- Kopieer bestanden naar de bestemming en stel hun eigendom in:

`install --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>

- Kopieer bestanden naar de bestemming en stel hun groepseigendom in:

`install --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>

- Kopieer bestanden naar de bestemming en stel hun `modus` in:

`install --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>

- Kopieer bestanden en pas toegangstijden/wijzigingstijden van de bron toe op de bestemming:

`install --preserve-timestamps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>

- Kopieer bestanden en maak de mappen op de bestemming aan als ze niet bestaan:

`install -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand1 pad/naar/bronbestand2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestemming</span>
