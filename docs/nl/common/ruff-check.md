---
layout: page
title: common/ruff-check (Nederlands)
description: "Een extreem snelle Python linter. `check` is het standaard commando - het kan overal weggelaten worden."
content_hash: 9baa34e5b3cd38a072e9effce5c4dcf1bcccb393
last_modified_at: 2024-06-04
related_topics:
  - title: English version
    url: /en/common/ruff-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruff check

Een extreem snelle Python linter. `check` is het standaard commando - het kan overal weggelaten worden.
Als geen bestanden of mappen zijn gespecificeerd, wordt de huidige map gebruikt.
Meer informatie: <https://docs.astral.sh/ruff/linter>.

- Voer de linter uit op de opgegeven bestanden of mappen:

`ruff check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Voer de gesuggereerde fixes uit en pas de bestanden in-place aan:

`ruff check --fix`

- Voer de linter uit en re-lint op iedere wijziging:

`ruff check --watch`

- Zet alleen de gespecificeerde regels (of alle regels) aan en negeer het configuratie bestand:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ALL|regelcode1,regelcode2,...</span>

- Zet additioneel de gespecificeerde regels aan:

`ruff check --extend-select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelcode1,regelcode2,...</span>

- Zet de gespecificeerde regels uit:

`ruff check --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelcode1,regelcode2,...</span>

- Negeer alle bestaande schendingen van een regel door `# noqa` toe te voegen aan alle regels die de regel breken:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelcode</span>` --add-noqa`
