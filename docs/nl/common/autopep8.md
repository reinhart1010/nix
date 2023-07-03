---
layout: page
title: common/autopep8 (Nederlands)
description: "Formatteer Python-code conform de PEP 8-stijlgids."
content_hash: 843ea5c09e7f6cbeddd77fe38f6e81044ca0f2f3
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/autopep8.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autopep8.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autopep8.html
    icon: bi bi-globe
---
# autopep8

Formatteer Python-code conform de PEP 8-stijlgids.
Meer informatie: <https://github.com/hhatto/autopep8>.

- Formateer een bestand naar `stdout`, met een ingestelde maximale toegestane regellengte:

`autopep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.py</span>` --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lengte</span>

- Formateer een bestand, geef een diff weer met de wijzigingen:

`autopep8 --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.py</span>

- Formatteer het bestand en sla de wijzigingen op:

`autopep8 --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.py</span>

- Formatteer de bestanden recursief in een map en sla deze wijzigingen op:

`autopep8 --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
