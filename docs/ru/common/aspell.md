---
layout: page
title: common/aspell (русский)
description: "Интерактивная проверка орфографии."
content_hash: bf0c4602aad7dd40322c76b458190903bab2e148
last_modified_at: 2024-08-14
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aspell

Интерактивная проверка орфографии.
Больше информации: <http://aspell.net/>.

- Проверить орфографию в одном файле:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Вывести список неверно написанных слов из стандартного ввода:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>` | aspell list`

- Показать доступные словари:

`aspell dicts`

- Запустить `aspell` с использованием другого языка (двухсимвольный код согласно ISO 639):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Вывести список неверно написанных слов из стандартного ввода, игнорируя слова из персонального списка:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">персональный_список_слов.pws</span>` list`
