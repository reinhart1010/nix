---
layout: page
title: common/aspell (русский)
description: "Интерактивная проверка орфографии."
content_hash: bf0c4602aad7dd40322c76b458190903bab2e148
last_modified_at: 2024-08-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

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
