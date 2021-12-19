---
layout: page
title: common/vim (українська)
description: "Vim (Vi IMproved), консольний текстовий редактор, надає різні режими для різних маніпуляцій над текстом."
content_hash: c027d0ce4bdf35ccf006f60fa28d7edb1d20094b
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
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
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

`:wq<Enter>`

- Анулювати (undo) останню операцію:

`u`

- Знайти паттерн у файлі (натисніть `n`/`N` щоб перейти до наступного/попереднього збігу):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">паттерн_для_пошуку</span>`<Enter>`

- Виконати регексп заміну в цілому файлі:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">регексп_вираз</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">заміна</span>`/g<Enter>`

- Показати номери рядків:

`:set nu<Enter>`
