---
layout: page
title: linux/sleep (українська)
description: "Затримка на певний час."
content_hash: ea54b7c75e32350d8fac9ad365a6cdb184239eb0
last_modified_at: 2024-04-20
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sleep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sleep

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
