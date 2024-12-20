---
layout: page
title: common/vim (українська)
description: "Vim (Vi IMproved), консольний текстовий редактор, надає різні режими для різних маніпуляцій над текстом."
content_hash: 48b4413c55fb530abd60a318f8fbae8998a8cb7d
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

Vim (Vi IMproved), консольний текстовий редактор, надає різні режими для різних маніпуляцій над текстом.
Натиснувши `i` потрапляємо в режим вставки (insert mode). `<Esc>` повертає у нормальний режим (normal mode), який дозволяє користуватися командами Vim.
Більше інформації: <https://www.vim.org>.

- Відкрити файл:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Відкрити файл на визначеноу рядку:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">номер_рядку</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу</span>

- Подивитися допомогу Vim:

`:help<Enter>`

- Зберегти і вийти:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ZZ|:wq<Enter></span>

- Анулювати (undo) останню операцію:

`<Esc>u`

- Знайти паттерн у файлі (натисніть `n`/`N` щоб перейти до наступного/попереднього збігу):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">паттерн_для_пошуку</span>`<Enter>`

- Виконати регексп заміну в цілому файлі:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регексп_вираз</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">заміна</span>`/g<Enter>`

- Показати номери рядків:

`:set nu<Enter>`
