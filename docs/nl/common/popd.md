---
layout: page
title: common/popd (Nederlands)
description: "Verwijder een map van de directory stack die is geplaatst met de ingebouwde pushd-opdracht van de shell."
content_hash: 5f8dab14bfac787a7188d7446c8239dcf7bd8977
last_modified_at: 2024-09-21
related_topics:
  - title: dansk version
    url: /da/common/popd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/popd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/popd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/popd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># popd

Verwijder een map van de directory stack die is geplaatst met de ingebouwde pushd-opdracht van de shell.
Zie ook `pushd` om een map op de stapel te plaatsen en `dirs` om de inhoud van de stapel weer te geven.
Meer informatie: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Verwijder de bovenste map van de stapel en ga ernaartoe:

`popd`

- Verwijder de N-de map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd +N`

- Verwijder de N-de map (beginnend vanaf nul van rechts, uit de lijst die met `dirs` wordt weergegeven):

`popd -N`

- Verwijder de eerste map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd -n`
