---
layout: page
title: common/stat (русский)
description: "Показ информации о файле и файловой системе."
content_hash: f097746cf3185482ca6e638222fdf2fecb6f0284
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

Показ информации о файле и файловой системе.
Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Показать свойства файла, такие как размер, права доступа, даты создания и последнего обращения и другие:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- То же, что и выше, но в сжатой форме:

`stat --terse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать информацию о файловой системе:

`stat --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать только права доступа в восьмеричном виде:

`stat --format="%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать владельца и группу файла:

`stat --format="%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Показать размер файла в байтах:

`stat --format="%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
