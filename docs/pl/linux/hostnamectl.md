---
layout: page
title: linux/hostnamectl (polski)
description: "Wyświetl lub ustaw nazwę hosta tego komputera."
content_hash: bb4ed23c5218877aea056a04119ca81e4255a258
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/hostnamectl.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/hostnamectl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hostnamectl

Wyświetl lub ustaw nazwę hosta tego komputera.
Więcej informacji: <https://manned.org/hostnamectl>.

- Wyświetl nazwę hosta tego komputera:

`hostnamectl`

- Ustaw nazwę hosta tego komputera:

`sudo hostnamectl set-hostname "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_hosta</span>`"`

- Ustaw ładną nazwę hosta tego komputera:

`sudo hostnamectl set-hostname --static "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_hosta.example.com</span>`" && sudo hostnamectl set-hostname --pretty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_hosta</span>`"`

- Zresetuj nazwę hosta do jej domyślnej wartości:

`sudo hostnamectl set-hostname --pretty ""`
