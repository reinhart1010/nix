---
layout: page
title: linux/journalctl (українська)
description: "Запити до журналу systemd."
content_hash: 7971d8fcf30b54b61526f2867bad32fc835dfafe
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/linux/journalctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/journalctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># journalctl

Запити до журналу systemd.
Більше інформації: <https://manned.org/journalctl>.

- Показати всі повідомлення з рівнем пріоритету 3 (помилки) від цього завантаження ([b]oot):

`journalctl -b --priority=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Показати всі повідомлення з останнього завантаження:

`journalctl -b -1`

- Видалити записи журналу, які старіші за 2 дні:

`journalctl --vacuum-time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2d</span>

- Слідкувати за новими повідомленнями (як `tail -f` для традиційного syslog):

`journalctl -f`

- Показати всі повідомлення за конкретним блоком ([u]nit):

`journalctl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">блок</span>

- Фільтрувати повідомлення в межах діапазону часу (мітка часу або покажчики місця заповнення, як-от «вчора»):

`journalctl --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">now|today|yesterday|tomorrow</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD HH:MM:SS</span>

- Показати всі повідомлення за певним процесом:

`journalctl _PID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Показати всі повідомлення за певним виконуваним файлом:

`journalctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/виконуваного_файлу</span>