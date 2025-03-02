---
layout: page
title: common/read (Nederlands)
description: "Shell builtin voor het ophalen van data van `stdin`."
content_hash: 3c321751ad188c98650e71f103e761fee9e0070b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/read.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/read.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/read.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/read.html
    icon: bi bi-globe
tldri18n_status: 2
---
# read

Shell builtin voor het ophalen van data van `stdin`.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Sla gegevens op die je van het toetsenbord typt:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Sla elke van de volgende regels die je invoert op als waarden van een array:

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array</span>

- Specificeer het maximale aantal karakters dat gelezen moet worden:

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">character_count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Wijs meerdere waarden toe aan meerdere variabelen:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_ variable1 _ variable2</span>` <<< "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">De achternaam is Bond</span>`"`

- Laat backslash (\\) niet optreden als een escape-teken:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Toon een prompt vóór de invoer:

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Voer je invoer hier in: </span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Echo de ingetikte tekens niet (stille modus):

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Lees `stdin` en voer een actie uit op elke regel:

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/stdin|pad/naar/bestand|...</span>
