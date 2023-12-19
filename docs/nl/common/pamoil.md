---
layout: page
title: common/pamoil (Nederlands)
description: "Zet een PAM afbeelding om in een olieschilderij."
content_hash: 5f9eece22db3e760e9c91aeec5aa2576eb1fcc12
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/pamoil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamoil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamoil

Zet een PAM afbeelding om in een olieschilderij.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamoil.html>.

- Zet een PAM afbeelding om in een olieschilderij:

`pamoil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.pam</span>

- Beschouw een omgeving van N pixels voor het "smearing"-effect:

`pamoil -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.pam</span>
