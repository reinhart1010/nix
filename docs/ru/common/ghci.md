---
layout: page
title: common/ghci (русский)
description: "Интерактивная среда Glasgow Haskell Compiler."
content_hash: b0aa0e41359ae1f0c9ebd4692850c9cad06cf7e4
related_topics:
  - title: English version
    url: /en/common/ghci.html
    icon: bi bi-globe
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

`ghci -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки2</span>
