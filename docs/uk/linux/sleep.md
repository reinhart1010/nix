---
layout: page
title: linux/sleep (українська)
description: "Затримка на певний час."
content_hash: ea54b7c75e32350d8fac9ad365a6cdb184239eb0
last_modified_at: 2024-04-21
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sleep

Затримка на певний час.
Більше інформації: <https://www.gnu.org/software/coreutils/sleep>.

- Затримка в секундах:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">секунди</span>

- Затримка в хвилинах (також можна використовувати інші одиниці ([д]ень, [г]одина, [с]екунда, вічність):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">хвилини</span>`m`

- Затримка на 1 день 3 години:

`sleep 1d 3h`

- Виконати певну команду через 20 хвилин затримки:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
