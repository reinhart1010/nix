---
layout: page
title: common/rm (русский)
description: "Удалить файлы или каталоги."
content_hash: 0f7cacd16c1acfbd3a1a388fd56967873969d296
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

Удалить файлы или каталоги.
Больше информации: <https://www.gnu.org/software/coreutils/rm>.

- Удалить файлы из определённых мест:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/другого_файла</span>

- Рекурсивно удалить каталог и все его подкаталоги:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/директории</span>

- Принудительно удалить каталог без запроса подтверждения или отображения сообщений об ошибках:

`rm -r -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/директории</span>

- Интерактивное удаление нескольких файлов с запросом перед каждым удалением:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла1 путь/до/файла2 ...</span>

- Удаление файлов с подробным выводом, печать сообщения для каждого удаленного файла:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/директории/*</span>
