---
layout: page
title: osx/ed (русский)
description: "Оригинальный текстовый редактор Unix."
content_hash: e9cfab52d02e16777c880fb99a237eb504b183e5
related_topics:
  - title: English version
    url: /en/osx/ed.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ed

Оригинальный текстовый редактор Unix.
Смотрите также: `awk`, `sed`.
Больше информации: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Запустить интерактивную сессию редактора с пустым документом:

`ed`

- Запустить интерактивную сессию редактора с пустым документом и указанной подсказкой:

`ed -p "> "`

- Запустить интерактивную сессию редактора пустым документом и без диагностики, подсчета байтов и '!' подсказки:

`ed -s`

- Редактировать указанный файл (это показывает количество байт загруженного файла):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/файлу</span>

- Заменить строку указанной на всех строках:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регулярное_выражение</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">замена</span>`/g`
