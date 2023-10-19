---
layout: page
title: common/alex (Nederlands)
description: "Een tool die ongevoelig, onattent schrijven opvangt."
content_hash: 5e73d4ac6a41777b8c6b5a6677604306522cc096
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
---
# alex

Een tool die ongevoelig, onattent schrijven opvangt.
Het helpt je bij het vinden van genderbegunstigende, polariserende, rasgerelateerde, onachtzame religie of andere ongelijke bewoordingen in de tekst.
Meer informatie: <https://github.com/get-alex/alex>.

- Analyseer tekst van `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zijn netwerk ziet er goed uit</span>` | alex --stdin`

- Analyseer alle bestanden in de huidige map:

`alex`

- Analyseer een specifiek bestand:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tekstbestand.md</span>

- Analyseer alle Markdown-bestanden behalve `voorbeeld.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.md</span>
