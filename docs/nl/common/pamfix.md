---
layout: page
title: common/pamfix (Nederlands)
description: "Repareer errors in PAM, PBM, PGM en PPM bestanden."
content_hash: 78cd99f51901baad1feb3de56acc466844b13ed7
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/pamfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamfix

Repareer errors in PAM, PBM, PGM en PPM bestanden.
Bekijk ook: `pamfile`, `pamvalidate`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Repareer een Netpbm bestand dat zijn laatste deel mist:

`pamfix -truncate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ext</span>

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door de overtredende pixels te verlagen in waarde:

`pamfix -clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ext</span>

- Repareer een Netpbm bestand waar de pixel waardes de afbeelding's `maxval` overschrijden door deze te verhogen:

`pamfix -changemaxval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/corrupt.pam|pbm|pgm|ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam|pbm|pgm|ppm</span>
