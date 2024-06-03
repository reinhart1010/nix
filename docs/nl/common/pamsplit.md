---
layout: page
title: common/pamsplit (Nederlands)
description: "Split een Netpbm bestand met meerdere afbeeldingen in meerdere Netpbm bestanden met een enkele afbeelding."
content_hash: 7594e067ed7dd4ff10970af3881708d30ed6cf06
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamsplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamsplit

Split een Netpbm bestand met meerdere afbeeldingen in meerdere Netpbm bestanden met een enkele afbeelding.
Bekijk ook: `pamfile`, `pampick`, `pamexec`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

- Split een Netpbm bestand met meerdere afbeeldingen in meerdere Netpbm bestanden met een enkele afbeelding:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>

- Specificeer een patroon voor de benaming van de uitvoerbestanden:

`pamsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_%d.pam</span>
