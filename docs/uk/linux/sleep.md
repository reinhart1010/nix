---
layout: page
title: linux/sleep (українська)
description: "Затримка на певний час."
content_hash: 05990cc7d9ee5908e244070cfdd234161ccb9331
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/sleep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sleep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sleep

Затримка на певний час.
Більше інформації: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- Затримка в секундах:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">секунди</span>

- Затримка в хвилинах (також можна використовувати інші одиниці ([д]ень, [г]одина, [с]екунда, вічність):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">хвилини</span>`m`

- Затримка на 1 день 3 години:

`sleep 1d 3h`

- Виконати певну команду через 20 хвилин затримки:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
