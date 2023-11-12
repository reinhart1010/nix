---
layout: page
title: windows/where (русский)
description: "Показ расположения файлов, удовлетворяющих шаблону поиска."
content_hash: 795eb40cd59cb910b0ab09a84adc55e34fcd7250
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/where.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
tldri18n_status: 2
---
# where

Показ расположения файлов, удовлетворяющих шаблону поиска.
По умолчанию поиск производится в текущей папке и по путям в переменной окружения PATH.
Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>.

- Отобразить расположение файлов, соответствующих шаблону:

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_файла</span>

- Отобразить расположение файлов, соответствующих шаблону, вместе с размером и датой:

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_файла</span>

- Рекурсивно искать файлы, соответствующие шаблону, по указанному пути:

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_файла</span>

- Только вернуть код возврата для результата поиска файла по шаблону:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_файла</span>
