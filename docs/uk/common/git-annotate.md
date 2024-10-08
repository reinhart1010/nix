---
layout: page
title: common/git-annotate (українська)
description: "Показує хеш коміту і останнього автора на кожному рядку у файлі."
content_hash: 7c9283f607083133dfd1275e3cecfe1d9ca3934c
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-annotate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-annotate.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annotate

Показує хеш коміту і останнього автора на кожному рядку у файлі.
Дивіться `git blame`, якій варто віддати перевагу над `git annotate`.
`git annotate` призначена для тих, хто знайомий із іншими системами контролю версій.
Більше інформації: <https://git-scm.com/docs/git-annotate>.

- Виводить файл з ім'ям автора та хешем коміту доданими поперед кожного рядку:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Виводить файл з електронною поштою автора та хешем коміту доданими поперед кожного рядку:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Виводить лише рядки, які відповідають регулярному виразу:

`git annotate -L :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регулярний_вираз</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>
