---
layout: page
title: common/if (Nederlands)
description: "Voert voorwaardelijke verwerking uit in shell-scripts."
content_hash: a2c8335222f723ac158cddf2ec512ca6800a875c
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/if.html
    icon: bi bi-globe
tldri18n_status: 2
---
# if

Voert voorwaardelijke verwerking uit in shell-scripts.
Bekijk ook: `test`, `[`.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- Voer de opgegeven commando's uit als de exitstatus van het voorwaardelijke commando nul is:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde_commando</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Voer de opgegeven commando's uit als de exitstatus van het voorwaardelijke commando niet nul is:

`if ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde_commando</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Voer de eerste opgegeven commando's uit als de exitstatus van het voorwaardelijke commando nul is, anders voer de tweede opgegeven commando's uit:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde_commando</span>`; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; else `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is onwaar"</span>`; fi`

- Controleer of een bestand ([f]) bestaat:

`if [[ -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Controleer of een map ([d]) bestaat:

`if [[ -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Controleer of een bestand of map b[e]staat:

`if [[ -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>` ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Controleer of een variabele is gedefinieerd:

`if [[ -n "$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`" ]]; then `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Voorwaarde is waar"</span>`; fi`

- Toon alle mogelijke voorwaarden (`test` is een alias voor `[`; beide worden vaak gebruikt met `if`):

`man [`
