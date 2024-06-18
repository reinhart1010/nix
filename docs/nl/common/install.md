---
layout: page
title: common/install (Nederlands)
description: "Kopieer bestanden en stel attributen in."
content_hash: 3737e1124f475760735c514ff61fc2d651e0945a
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># install

Kopieer bestanden en stel attributen in.
Kopieer bestanden (vaak uitvoerbare) naar een systeemlocatie zoals `/usr/local/bin` en geef ze de juiste permissies/eigendom.
Meer informatie: <https://www.gnu.org/software/coreutils/install>.

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
