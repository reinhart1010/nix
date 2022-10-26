---
layout: page
title: common/cabal (русский)
description: "Интерфейс командной строки для инфраструктуры пакетов Haskell (Cabal)."
content_hash: aa64587e169c48deeabafff3fffd76217f40cebb
related_topics:
  - title: English version
    url: /en/common/cabal.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cabal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cabal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cabal.html
    icon: bi bi-globe
---
# cabal

Интерфейс командной строки для инфраструктуры пакетов Haskell (Cabal).
Управление Haskell-проектами и Cabal-пакетами из репозитория Hackage.
Больше информации: <https://cabal.readthedocs.io/en/latest/intro.html>.

- Искать и вывести список пакетов из Hackage:

`cabal list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка_поиска</span>

- Показать информацию о пакете:

`cabal info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_пакета</span>

- Скачать и установить пакет:

`cabal install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_пакета</span>

- Создать новый Haskell-проект в текущей папке:

`cabal init`

- Собрать проект в текущей папке:

`cabal build`

- Запустить тесты из проекта в текущей папке:

`cabal test`
