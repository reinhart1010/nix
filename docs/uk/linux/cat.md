---
layout: page
title: linux/cat (українська)
description: "Зчитування та об'єднання файлів."
content_hash: 84a9cd445d973a0e8db8910ac8c2d2bb22366bbd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Зчитування та об'єднання файлів.
Більше інформації: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Вивести вміст файлу в `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Об’єднати кілька файлів у вихідний файл:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/вихідного_файлу</span>

- Додайте кілька файлів до вихідного файлу:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/вихідного_файлу</span>

- Записати `stdin` у файл:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Пронумерувати всі вихідні рядки:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Відобразити недруковані символи та пробіли (з префіксом `M-`, якщо не ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>
