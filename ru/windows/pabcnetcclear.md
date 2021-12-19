---
layout: page
title: windows/pabcnetcclear (русский)
description: "Предобрабатывает и компилирует PascalABC.NET исходные файлы."
content_hash: f7f87da277f308e0cd41090021a0c8e33c9f8773
related_topics:
  - title: English version
    url: /en/windows/pabcnetcclear.html
    icon: bi bi-globe
---
# pabcnetcclear

Предобрабатывает и компилирует PascalABC.NET исходные файлы.
Больше информации: <http://pascalabc.net>.

- Компилирует исходный файл в запускаемое приложение с тем же именем:

`pabcnetcclear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.pas</span>

- Компилирует исходный файл в запускаемое приложение с тем же именем вместе с отладочной информацией:

`pabcnetcclear /Debug:1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.pas</span>

- Разрешает искать модули в указанной папке во время компиляции исходного файла в запускаемое приложение с тем же именем:

`pabcnetcclear /SearchDir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.pas</span>
