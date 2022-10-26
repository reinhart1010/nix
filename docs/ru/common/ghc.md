---
layout: page
title: common/ghc (русский)
description: "Компилятор Glasgow Haskell Compiler."
content_hash: 5f4b7aaa82e4cdb240bb53567564b39a0e0bc6da
related_topics:
  - title: English version
    url: /en/common/ghc.html
    icon: bi bi-globe
---
# ghc

Компилятор Glasgow Haskell Compiler.
Компиляция и компоновка исходных файлов Haskell.
Больше информации: <https://www.haskell.org/ghc>.

- Найти и скомпилировать все модули в текущей папке:

`ghc Main`

- Скомпилировать один файл:

`ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл.hs</span>

- Скомпилировать с использованием дополнительной оптимизации:

`ghc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл.hs</span>

- Остановить компиляцию после создания объектных файлов (.o):

`ghc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл.hs</span>

- Запустить REPL (интерактивную оболочку):

`ghci`

- Вычислить одно выражение:

`ghc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">выражение</span>
