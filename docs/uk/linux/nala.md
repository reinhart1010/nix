---
layout: page
title: linux/nala (українська)
description: "Утиліта керування пакетами з кращим форматуванням."
content_hash: ec5947478335c7bc6c10879d338cfad3c44305d7
last_modified_at: 2024-04-21
related_topics:
  - title: English version
    url: /en/linux/nala.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nala

Утиліта керування пакетами з кращим форматуванням.
Фронтенд для API `python-apt`.
Більше інформації: <https://gitlab.com/volian/nala>.

- Встановити пакет або оновити його до останньої версії:

`sudo nala install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет:

`sudo nala remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет та його конфігураційні файли:

`nala purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Пошук назв пакетів і описів за допомогою слова, регулярного виразу (за замовчуванням) або glob:

`nala search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">паттерн</span>`"`

- Оновити список доступних пакетів та оновити систему:

`sudo nala upgrade`

- Видалити усі невикористовувані пакети та залежності з вашої системи:

`sudo nala autoremove`

- Отримати швидші дзеркала, щоб покращити швидкість завантаження:

`sudo nala fetch`

- Показати історію всіх транзакцій:

`nala history`
