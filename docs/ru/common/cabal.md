---
layout: page
title: common/cabal (русский)
description: "Интерфейс командной строки для инфраструктуры пакетов Haskell (Cabal)."
content_hash: 05b587ce362fb50a59ad731d614b567e8ee7711e
last_modified_at: 2024-05-23
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
tldri18n_status: 2
---
# cabal

Интерфейс командной строки для инфраструктуры пакетов Haskell (Cabal).
Управление Haskell-проектами и Cabal-пакетами из репозитория Hackage.
Больше информации: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

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
