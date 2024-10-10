---
layout: page
title: common/npm-query (Nederlands)
description: "Print een array van afhankelijkheidsobjecten met behulp van CSS-achtige selectors."
content_hash: 4a61c4377c24c8de81576929a32b2596119a44fa
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/common/npm-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm query

Print een array van afhankelijkheidsobjecten met behulp van CSS-achtige selectors.
Meer informatie: <https://docs.npmjs.com/cli/commands/npm-query>.

- Print directe afhankelijkheden:

`npm query ':root > *'`

- Print alle directe productie-/ontwikkelingsafhankelijkheden:

`npm query ':root > .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prod|dev</span>`'`

- Print afhankelijkheden met een specifieke naam:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`'`

- Print afhankelijkheden met een specifieke naam en binnen een semantische versie range:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">semantische_versie</span>`'`

- Print afhankelijkheden die geen andere afhankelijkheden hebben:

`npm query ':empty'`

- Zoek alle afhankelijkheden met postinstall-scripts en verwijder ze:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- Zoek alle Git-afhankelijkheden en print welke applicatie ze vereist:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
