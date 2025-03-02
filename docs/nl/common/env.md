---
layout: page
title: common/env (Nederlands)
description: "Toon de omgeving of voer een programma uit in een aangepaste omgeving."
content_hash: 321bf2da101bd925d31e6c58c285878de4d49007
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/env.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/env.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/env.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/env.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/env.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# env

Toon de omgeving of voer een programma uit in een aangepaste omgeving.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Toon de environment:

`env`

- Voer een programma uit. Meestal gebruikt in scripts na de shebang (#!) voor het opzoeken van het pad naar het programma:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Wis de omgeving en voer een programma uit:

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Verwijder een variable van de omgeving en voer een programma uit:

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Zet een variable en voer een programma uit:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Zet meerdere variablen en voer een programma uit:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable3</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waarde</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>
