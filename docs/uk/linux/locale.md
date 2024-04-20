---
layout: page
title: linux/locale (українська)
description: "Отримайте інформацію, що стосується локалізації."
content_hash: ed0de6923f74db63d93610bec545f9e7704f8a07
last_modified_at: 2024-04-20
related_topics:
  - title: English version
    url: /en/linux/locale.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/locale.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/locale.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># locale

Отримайте інформацію, що стосується локалізації.
Більше інформації: <https://manned.org/locale>.

- Список усіх глобальних змінних середовища, що описують локалізацію користувача:

`locale`

- список всії наявних локалізацій:

`locale --all-locales`

- Показати всі доступні локалізації та пов'язані метадані:

`locale --all-locales --verbose`

- Відображення поточного формату дати:

`locale date_fmt`
