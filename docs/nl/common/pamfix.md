---
layout: page
title: common/pamfix (Nederlands)
description: "Repareer errors in PAM, PBM, PGM en PPM bestanden."
content_hash: 78cd99f51901baad1feb3de56acc466844b13ed7
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamfix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfix

Repareer errors in PAM, PBM, PGM en PPM bestanden.
Bekijk ook: `pamfile`, `pamvalidate`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Repareer een Netpbm bestand dat zijn laatste deel mist:

`pamfix -truncate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ext</span>

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door de overtredende pixels te verlagen in waarde:

`pamfix -clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ext</span>

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door deze te verhogen:

`pamfix -changemaxval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.pam|pbm|pgm|ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam|pbm|pgm|ppm</span>
