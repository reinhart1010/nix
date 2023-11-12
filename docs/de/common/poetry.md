---
layout: page
title: common/poetry (Deutsch)
description: "Verwalte Python-Pakete und -Abhängigkeiten."
content_hash: b2db894f28997cafc8f554b28ef6e5360269301f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/poetry.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/poetry.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># poetry

Verwalte Python-Pakete und -Abhängigkeiten.
Weitere Informationen: <https://python-poetry.org/docs/cli/>.

- Erstelle ein neues Poetry-Projekt im Verzeichnis mit dem angegebenem Namen:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">projekt_name</span>

- Installiere eine Abhängigkeit und alle Unterabhängigkeiten:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abhängigkeit</span>

- Installiere eine Entwicklungsabhängigkeit und alle Unterabhängigkeiten:

`poetry add --dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abhängigkeit</span>

- Initialisiere ein neues Poetry-Projekt interaktiv im aktuellen Verzeichnis:

`poetry init`

- Aktualisiere alle Abhängigkeiten und `poetry.lock`:

`poetry update`

- Führe einen Befehl innerhalb der virtuellen Umgebung des Projekts aus:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Erhöhe die Minor-Version des Projekts in `pyproject.toml`:

`poetry version minor`

- Liste alle poetry Unterbefehle auf:

`poetry list`
