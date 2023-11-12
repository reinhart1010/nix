---
layout: page
title: common/ajson (Nederlands)
description: "Voert JSONPath uit op JSON-objecten."
content_hash: 4d2dbd57e36d0058f22a8c1e769b4dd5abe59ba0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ajson.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ajson.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ajson.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ajson.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ajson

Voert JSONPath uit op JSON-objecten.
Meer informatie: <https://github.com/spyzhov/ajson>.

- Lees JSON uit een bestand en voer een opgegeven JSONPath-expressie uit:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.json</span>

- Lees JSON van `stdin` en voer een gespecificeerde JSONPath-expressie uit:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- Lees JSON van een URL en evalueer een opgegeven JSONPath-expressie:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://voorbeeld.com/api/</span>`'`

- Lees wat eenvoudige JSON en bereken een waarde:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
