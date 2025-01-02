---
layout: page
title: common/declare (Nederlands)
description: "Declareer variabelen en geef ze attributen."
content_hash: a2421393aabd67df297e6a663169e1c048b2dd63
last_modified_at: 2025-01-02
related_topics:
  - title: English version
    url: /en/common/declare.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/declare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/declare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# declare

Declareer variabelen en geef ze attributen.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Declareer een string variabele met de gespecificeerde waarde:

`declare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`"`

- Declareer een integer variabele met de gespecificeerde waarde:

`declare -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`"`

- Declareer een array variabele met de gespecificeerde waarde:

`declare -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_a item_b item_c</span>`)`

- Declareer een associatieve array variabele met de gespecificeerde waarde:

`declare -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[sleutel_a]=item_a [sleutel_b]=item_b [sleutel_c]=item_c</span>`)`

- Declareer a readonly string variabele met de gespecificeerde waarde:

`declare -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`"`

- Declareer een globale variabele binnen een functie met de gespecificeerde waarde:

`declare -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>`"`

- Print een functie-definitie:

`declare -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">functie_naam</span>
