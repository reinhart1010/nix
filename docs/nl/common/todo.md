---
layout: page
title: common/todo (Nederlands)
description: "Een eenvoudige, op standaarden gebaseerde, opdrachtregel todo manager."
content_hash: 80e419db77dc85afb8fe78f148da83aae69da73f
last_modified_at: 2023-12-01
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todo

Een eenvoudige, op standaarden gebaseerde, opdrachtregel todo manager.
Meer informatie: <https://todoman.readthedocs.io>.

- Toon startbare taken:

`todo list --startable`

- Voeg een nieuwe taak toe aan de werklijst:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ding_om_te_doen</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">werk</span>

- Voeg een locatie toe aan een taak met een gegeven ID:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locatie_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Toon details over een taak:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Markeer taken met de opgegeven IDs als voltooid:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id1 taak_id2 ...</span>

- Verwijder een taak:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Verwijder voltooide taken en reset de IDs van de overgebleven taken:

`todo flush`
