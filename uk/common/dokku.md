---
layout: page
title: common/dokku (українська)
description: "Міні-Heroku на основі Docker (PaaS)."
content_hash: 751e5cb399c5bfcfbf6aacb4bd3d84b5c86ab6b4
related_topics:
  - title: English version
    url: /en/common/dokku.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dokku.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dokku.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dokku

Міні-Heroku на основі Docker (PaaS).
Легко розгортає кілька програм на власному сервері різними мовами за допомогою однієї команди `git-push`.
Більше інформації: <https://github.com/dokku/dokku>.

- Показати запущені програми:

`dokku apps`

- Створити програму:

`dokku apps:create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_програми</span>

- Видалити програму:

`dokku apps:destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_програми</span>

- Встановити плагін:

`dokku plugin:install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повний_url_на_репозиторій</span>

- Зв'язати базу даних із програмою:

`dokku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db</span>`:link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_бази_даних</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_програми</span>
