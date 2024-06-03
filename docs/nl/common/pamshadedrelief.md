---
layout: page
title: common/pamshadedrelief (Nederlands)
description: "Genereer een schaduwwerking van een hoogtekaart."
content_hash: ee1ceb2d4c8f07e1e55e80a94b4c3628765ce3f5
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamshadedrelief.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamshadedrelief.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamshadedrelief

Genereer een schaduwwerking van een hoogtekaart.
Bekijk ook: `pamcrater`, `ppmrelief`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- Genereer een schaduwwerking afbeelding met de invoer-afbeelding als een hoogtekaart:

`pamshadedrelief < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Pas de gamma aan van een afbeelding met de gespecificeerde factor:

`pamshadedrelief -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">factor</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
