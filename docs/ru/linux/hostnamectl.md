---
layout: page
title: linux/hostnamectl (русский)
description: "Получение и установка имени хоста компьютера."
content_hash: 4ad0206b3fab95413d0aedbbb6e50ec11d9c386c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/hostnamectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/hostnamectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hostnamectl

Получение и установка имени хоста компьютера.
Больше информации: <https://manned.org/hostnamectl>.

- Получить имя хоста компьютера:

`hostnamectl`

- Задать имя хоста компьютера:

`sudo hostnamectl set-hostname "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_хоста</span>`"`

- Задать красивое (короткое) имя хоста компьютера:

`sudo hostnamectl set-hostname --static "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_хоста.example.com</span>`" && sudo hostnamectl set-hostname --pretty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_хоста</span>`"`

- Сбросить имя хоста компьютера к значению по умолчанию:

`sudo hostnamectl set-hostname --pretty ""`
