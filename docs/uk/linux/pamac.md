---
layout: page
title: linux/pamac (українська)
description: "Утиліта командного рядка для GUI менеджера пакетів pamac."
content_hash: f8be51eda926e844e0b5bf27935c81a7e1a98bf9
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/linux/pamac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pamac

Утиліта командного рядка для GUI менеджера пакетів pamac.
Якщо ви не можете побачити пакети AUR, увімкніть його `/etc/pamac.conf` або в GUI.
Більше інформації: <https://wiki.manjaro.org/index.php/Pamac>.

- Встановити новий пакет:

`pamac install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_пакета</span>

- Видалити пакет і його непотрібні залежності (сироти):

`pamac remove --orphans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_пакета</span>

- Шукати пакет в базі даних пакетів:

`pamac search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_пакета</span>

- Перелічити встановлені пакети:

`pamac list --installed`

- Перевірити наявність оновлень пакетів:

`pamac checkupdates`

- Оновити всі пакети:

`pamac upgrade`
