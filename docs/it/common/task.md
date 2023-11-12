---
layout: page
title: common/task (italiano)
description: "Gestore della lista dei TODO."
content_hash: 457ff9ad793d67025eeab495aa7f039f73bd81c1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/task.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># task

Gestore della lista dei TODO.
Maggiori informazioni: <https://taskwarrior.org/docs/>.

- Aggiungere un nuovo task:

`task add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thing_to_do</span>

- Lista dei task:

`task list`

- Contrassegnare un task come completato:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` done`

- Modificare un task:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` modify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_thing_to_do</span>

- Eliminare un task:

`task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>` delete`
