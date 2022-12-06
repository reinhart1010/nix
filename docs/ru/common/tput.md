---
layout: page
title: common/tput (русский)
description: "Просмотр и изменение настроек и возможностей терминала."
content_hash: 001fce0413bf237bdfc97a47f18a0b23b5a2047b
last_modified_at: 2022-12-06
related_topics:
  - title: English version
    url: /en/common/tput.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tput.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tput

Просмотр и изменение настроек и возможностей терминала.
Больше информации: <https://manned.org/tput>.

- Переместить курсор в определённое место на экране:

`tput cup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">номер_строки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">номер_столбца</span>

- Установить цвет переднего плана (af) или фона (ab):

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setaf|setab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ansi_код_цвета</span>

- Показать количество столбцов, строк или цветов:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cols|lines|colors</span>

- Подать звуковой сигнал терминала:

`tput bel`

- Сбросить все атрибуты терминала:

`tput sgr0`

- Включить или отключить перенос слов:

`tput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smam|rmam</span>
