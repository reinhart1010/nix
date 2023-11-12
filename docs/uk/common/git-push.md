---
layout: page
title: common/git-push (українська)
description: "Надсилає коміти до віддаленого репозиторію."
content_hash: 1bd2f0ce3e5ec58a05f151da13e2835539787a75
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git push

Надсилає коміти до віддаленого репозиторію.
Більше інформації: <https://git-scm.com/docs/git-push>.

- Надіслати локальні зміни у поточній гілці до її типового віддаленого відповідника:

`git push`

- Надіслати зміни із вказаної локальної гілки до її віддаленого відповідника:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локальна_гілка</span>

- Надіслати зміни із вказаної локальної гілки до її віддаленого відповідника та встановити цю віддалену гілку як типову для дій надсилання і стягування:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локальна_гілка</span>

- Надіслати зміни із вказаної локальної гілки до вказаної віддаленої:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локальна_гілка</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">віддалена_гілка</span>

- Надіслати зміни з усіх локальних гілок до їх відповідників у вказаному віддаленому репозиторії:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>

- Видалити гілку у віддаленому репозиторії:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">віддалена_гілка</span>

- Видалити віддалену гілку, що не містить локального відповідника:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>

- Надіслати мітки, що відсутні у віддаленому репозиторії:

`git push --tags`
