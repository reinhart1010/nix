---
layout: page
title: linux/print (Nederlands)
description: "Een alias voor de `run-mailcap`-actie print."
content_hash: df5c49d9206b8979f470bb3314149bd50c2fc42b
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/linux/print.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/print.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/print.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># print

Een alias voor de `run-mailcap`-actie print.
Oorspronkelijk wordt `run-mailcap` gebruikt om mime-typen/bestanden te verwerken.
Meer informatie: <https://manned.org/print>.

- De print-actie kan worden gebruikt om elk bestand af te drukken met de standaard `run-mailcap`-tool:

`print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Met `run-mailcap`:

`run-mailcap --action=print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>
