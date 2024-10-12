---
layout: page
title: common/awk (українська)
description: "Універсальна мова програмування для роботи з файлами."
content_hash: 7160bb7fcc1e00c3f1104e4b0e71589085c387ad
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awk

Універсальна мова програмування для роботи з файлами.
Більше інформації: <https://github.com/onetrueawk/awk>.

- Вивести п’ятий стовпець (він же поле) у файлі, розділеному пробілами:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести другий стовпець рядків, що містять "foo", у файлі, розділеному пробілами:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести останній стовпець кожного рядка у файлі, використовуючи кому (замість пробілу) як роздільник полів:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Підсумувати значення в першому стовпці файлу та надрукувати підсумок:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести кожен третій рядок, починаючи з першого:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести різні значення залежно від умов:

`awk '{if ($1 == "foo") print "Точний збіг foo"; else if ($1 ~ "bar") print "Частковий збіг bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Вивести всі рядки, значення 10-го стовпця яких знаходиться між min і max:

`awk '($10 >= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">min_value</span>` && $10 <= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_value</span>`)'`

- Вивести таблицю користувачів із UID >=1000 із заголовком і форматуванням, використовуючи двокрапку як роздільник («%-20s» означає: 20 символів рядка з вирівнюванням по лівому краю, «%6s» означає: 6 символів рядка з вирівнюванням по правому краю):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
