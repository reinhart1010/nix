---
layout: page
title: common/mcs (русский)
description: "Mono компилятор C#."
content_hash: 405a88353b56c3af03695bcf1eb10adbe06d0a94
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mcs

Mono компилятор C#.
Больше информации: <https://manned.org/mcs.1>.

- Скомпилировать указанные файлы:

`mcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/входному_файлу1.cs путь/к/входному_файлу2.cs ...</span>

- Указать имя выходной программы:

`mcs -out:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/файлу.exe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/входному_файлу1.cs путь/к/входному_файлу2.cs ...</span>

- Указать тип выходной программы:

`mcs -target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exe|winexe|library|module</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/входному_файлу1.cs путь/к/входному_файлу2.cs ...</span>
