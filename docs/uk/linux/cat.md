---
layout: page
title: linux/cat (українська)
description: "Зчитування та об'єднання файлів."
content_hash: 942f4791ae2280553f70bc0805ab38d07d2f88c2
last_modified_at: 2024-04-21
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Зчитування та об'єднання файлів.
Більше інформації: <https://www.gnu.org/software/coreutils/cat>.

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
