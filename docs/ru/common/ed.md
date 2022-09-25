---
layout: page
title: common/ed (русский)
description: "Оригинальный текстовый редактор Unix."
content_hash: b1d86e05d5de8eb34909bb45c1a3b4d1c78f70ac
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ed.html
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

`ed --prompt="> "`

- Запустить интерактивную сессию редактора с удобными для пользователя ошибками:

`ed --verbose`

- Запустить интерактивную сессию редактора пустым документом и без диагностики, подсчета байтов и '!' подсказки:

`ed --quiet`

- Запустить интерактивную сессию редактора без изменения статуса выхода при сбое команды:

`ed --loose-exit-status`

- Редактировать указанный файл (это показывает количество байт загруженного файла):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/файлу</span>

- Заменить строку указанной на всех строках:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регулярное_выражение</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">замена</span>`/g`
