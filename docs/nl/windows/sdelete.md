---
layout: page
title: windows/sdelete (Nederlands)
description: "Verwijder veilig een bestand/map van de schijf, of maak de vrije ruimte op een volume/fysieke schijf schoon."
content_hash: a66015709a448681ebf1c495e2d52d3a21edc52e
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/windows/sdelete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/sdelete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdelete

Verwijder veilig een bestand/map van de schijf, of maak de vrije ruimte op een volume/fysieke schijf schoon.
Meer informatie: <https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete>.

- Verwijder bestanden met 3 [p]asses:

`sdelete -p 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1 pad\naar\bestand2 ...</span>

- Verwijder mappen en de [s]ubmappen met 1 pass (default):

`sdelete -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map1 pad\naar\map2 ...</span>

- Maak de vrije ruimte schoon van volume D: met 3 [p]asses:

`sdelete -p 3 D:`

- Maak de vrije ruimte schoon met nullen ([z]) van fysieke schijf 2, welke geen volumes meer mag bevatten die opgeschoond kunnen worden:

`sdelete -z 2`
