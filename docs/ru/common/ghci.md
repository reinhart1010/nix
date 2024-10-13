---
layout: page
title: common/ghci (русский)
description: "Интерактивная среда Glasgow Haskell Compiler."
content_hash: abd59a08c406730e67e0bb51754463990cc310af
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/ghci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghci

Интерактивная среда Glasgow Haskell Compiler.
Больше информации: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- Запустить REPL (интерактивную оболочку):

`ghci`

- Запустить REPL и загрузить указанный исходный файл Haskell:

`ghci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">исходный_файл.hs</span>

- Запустить REPL и включить опцию языка:

`ghci -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">опция_языка</span>

- Запустить REPL и включить определённый уровень предупреждений компилятора (например, `all` или `compact`):

`ghci -W`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">уровень_предупреждений</span>

- Запустить REPL со списком папок, разделённых двоеточием, в которых нужно искать исходные файлы:

`ghci -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки1:путь/до/папки2:...</span>
