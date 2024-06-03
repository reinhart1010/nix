---
layout: page
title: common/ruff-format (Nederlands)
description: "Een extreem snelle Python code formatter."
content_hash: 7fd33677f58426941478b4c968064c2b212b985a
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/ruff-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ruff-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruff format

Een extreem snelle Python code formatter.
Als geen bestanden of mappen zijn gespecificeerd, wordt de huidige map gebruikt.
Meer informatie: <https://docs.astral.sh/ruff/formatter>.

- Formateer opgegeven bestanden of mappen in-place:

`ruff format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Toon welke bestanden aangepast zouden worden en return een niet-nul exit code als er bestanden zijn om te formatteren en anders nul:

`ruff format --check`

- Toon welke veranderingen er gemaakt zouden worden zonder de bestanden aan te passen:

`ruff format --diff`
