---
layout: page
title: common/lpadmin (Nederlands)
description: "Configureer CUPS printers en klasses."
content_hash: 8b5b944f33e3639338a6fbb62d09d1be29afd33d
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/lpadmin.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpadmin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpadmin

Configureer CUPS printers en klasses.
Bekijk ook: `lpoptions`.
Meer informatie: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- Stel de standaard printer in:

`lpadmin -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>

- Verwijder een specifieke printer of klasse:

`lpadmin -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer|klasse</span>

- Voeg een printer toe aan een klasse:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klasse</span>

- Verwijder een printer uit een klasse:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klasse</span>
