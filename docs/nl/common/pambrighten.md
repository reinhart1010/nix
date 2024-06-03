---
layout: page
title: common/pambrighten (Nederlands)
description: "Verander de saturatie en waarde van een PAM afbeelding."
content_hash: 43b9518352931ea3f8d2071a99532a77321fa1b2
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pambrighten.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pambrighten.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pambrighten.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pambrighten

Verander de saturatie en waarde van een PAM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- Verhoog de verzadiging van elke pixel met het gespecificeerde percentage:

`pambrighten -saturation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Verhoog de waarde (van de HSV kleurruimte) van elke pixel met het gespecificeerde percentage:

`pambrighten -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percentage</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
