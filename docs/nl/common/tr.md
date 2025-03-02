---
layout: page
title: common/tr (Nederlands)
description: "Vertaal tekens: voer vervangingen uit op basis van enkele tekens en tekensets."
content_hash: a3e4fe947e355f410247419a631b35f093e6ee30
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/tr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tr

Vertaal tekens: voer vervangingen uit op basis van enkele tekens en tekensets.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Vervang alle voorkomens van een teken in een bestand en toon het resultaat:

`tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vind_karakter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervang_karakter</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang alle voorkomens van een teken uit de uitvoer van een ander commando:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tekst</span>` | tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vind_karakter</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervang_karakter</span>

- Map elk teken van de eerste set naar het overeenkomstige teken van de tweede set:

`tr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abcd</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jkmn</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verwijder alle voorkomens van de opgegeven set tekens uit de invoer:

`tr -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_karakters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Comprimeer een reeks identieke tekens tot een enkel teken:

`tr -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_karakters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vertaal de inhoud van een bestand naar hoofdletters:

`tr "[:lower:]" "[:upper:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verwijder niet-afdrukbare tekens uit een bestand:

`tr -cd "[:print:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
