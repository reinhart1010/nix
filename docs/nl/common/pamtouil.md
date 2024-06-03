---
layout: page
title: common/pamtouil (Nederlands)
description: "Converteer een PNM of PAM bestand naar een Motif UIL icon bestand."
content_hash: 80fddf1a42908e01ea1140d3ed0d87d995b3717e
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamtouil.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pamtouil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtouil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtouil

Converteer een PNM of PAM bestand naar een Motif UIL icon bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtouil.html>.

- Converteer een PNM of PAM bestand naar een Motif UIL icon bestand:

`pamtouil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm|pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.uil</span>

- Specificeer een voorvoegsel dat in het uitvoer-UIL-bestand moet worden afgedrukt:

`pamtouil -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uilname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm|pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.uil</span>
