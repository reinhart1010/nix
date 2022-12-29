---
layout: page
title: common/task (italiano)
description: "Gestore della lista dei TODO."
content_hash: 457ff9ad793d67025eeab495aa7f039f73bd81c1
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/common/task.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/task.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
