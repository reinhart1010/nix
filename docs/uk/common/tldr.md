---
layout: page
title: common/tldr (українська)
description: "Відображає прості сторінки допомоги для інструментів командного рядка з проекту tldr-pages."
content_hash: 449b627d497fc6871a11b4fc5d36f1502ad61369
last_modified_at: 2023-11-22
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr

Відображає прості сторінки допомоги для інструментів командного рядка з проекту tldr-pages.
Більше інформації: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Показує типове використання команди (підказка: це те, як ви потрапили сюди!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Показує tldr сторінку для команди `cd` на вказаній платформі:

`tldr -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|linux|osx|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cd</span>

- Показує tldr сторінку для підкоманди Git `git checkout`:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git-checkout</span>

- Оновлює локальні tldr сторінки (якщо клієнт підтримує кешування):

`tldr -u`
