---
layout: page
title: common/dokku (English)
description: "Docker powered mini-Heroku (PaaS)."
content_hash: 37a8bbcef70f97b8fd4f32d5d77f1a82ea93ffb5
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/dokku.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dokku.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/dokku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dokku

Docker powered mini-Heroku (PaaS).
Easily deploy multiple apps to your server in different languages using a single `git-push` command.
More information: <https://github.com/dokku/dokku>.

- List running apps:

`dokku apps`

- Create an app:

`dokku apps:create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Remove an app:

`dokku apps:destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Install plugin:

`dokku plugin:install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">full_repo_url</span>

- Link database to an app:

`dokku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db</span>`:link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>
