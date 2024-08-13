---
layout: page
title: linux/export (Nederlands)
description: "Exporteer shellvariabelen naar child-processen."
content_hash: 178333550530617c81ad1db4dde4fb4b43c4c7b7
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# export

Exporteer shellvariabelen naar child-processen.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Stel een omgevingsvariabele in:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABELE</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>

- Zet een omgevingsvariabele uit:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VARIABELE</span>

- Exporteer een functie naar child-processen:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUNCTIE_NAAM</span>

- Voeg een pad toe aan de omgevingsvariabele `PATH`:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/om/toe_te_voegen</span>

- Toon een lijst van actieve geëxporteerde variabelen in shell-opdrachtvorm:

`export -p`
