---
layout: page
title: common/ruff-format (Nederlands)
description: "Een extreem snelle Python code formatter."
content_hash: 7fd33677f58426941478b4c968064c2b212b985a
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/ruff-format.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruff format

Een extreem snelle Python code formatter.
Als geen bestanden of mappen zijn gespecificeerd, wordt de huidige map gebruikt.
Meer informatie: <https://docs.astral.sh/ruff/formatter>.

- Formateer opgegeven bestanden of mappen in-place:

`ruff format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Toon welke bestanden aangepast zouden worden en return een niet-nul exit code als er bestanden zijn om te formatteren en anders nul:

`ruff format --check`

- Toon welke veranderingen er gemaakt zouden worden zonder de bestanden aan te passen:

`ruff format --diff`
