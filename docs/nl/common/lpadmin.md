---
layout: page
title: common/lpadmin (Nederlands)
description: "Configureer CUPS printers en klasses."
content_hash: 755fa8460a54640c100d1d01cdc801051858cbc8
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lpadmin.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpadmin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpadmin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpadmin

Configureer CUPS printers en klasses.
Bekijk ook: `lpoptions`.
Meer informatie: <https://www.cups.org/doc/man-lpadmin.html>.

- Stel de standaard printer in:

`lpadmin -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>

- Verwijder een specifieke printer of klasse:

`lpadmin -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer|klasse</span>

- Voeg een printer toe aan een klasse:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klasse</span>

- Verwijder een printer uit een klasse:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klasse</span>
