---
layout: page
title: common/stat (русский)
description: "Показ информации о файле и файловой системе."
content_hash: f3ef312830fdc55777b8b433304902ef91b2b58e
related_topics:
  - title: English version
    url: /en/common/stat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stat

Показ информации о файле и файловой системе.
Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Показать свойства файла, такие как размер, права доступа, даты создания и последнего обращения и другие:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- То же, что и выше, но в сжатой форме:

`stat -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать информацию о файловой системе:

`stat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать только права доступа в восьмеричном виде:

`stat -c "%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать владельца и группу файла:

`stat -c "%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать размер файла в байтах:

`stat -c "%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
