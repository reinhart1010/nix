---
layout: page
title: common/ghcup (русский)
description: "Установщик набора инструментов Haskell."
content_hash: f5017022401576aaa6274b41061bc65416ff4f12
related_topics:
  - title: English version
    url: /en/common/ghcup.html
    icon: bi bi-globe
---
# ghcup

Установщик набора инструментов Haskell.
Установка, управление и обновление наборов инструментов Haskell.
Больше информации: <https://gitlab.haskell.org/haskell/ghcup-hs>.

- Запустить интерактивный текстовый интерфейс:

`ghcup tui`

- Вывести список доступных версий GHC/cabal:

`ghcup list`

- Установить рекомендуемую версию GHC:

`ghcup install ghc`

- Установить указанную версию GHC:

`ghcup install ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">версия</span>

- Задать "активную" версию GHC:

`ghcup set ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">версия</span>

- Установить инструмент cabal-install:

`ghcup install cabal`

- Обновить сам `ghcup`:

`ghcup upgrade`
