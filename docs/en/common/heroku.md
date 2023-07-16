---
layout: page
title: common/heroku (English)
description: "Create and manage Heroku apps."
content_hash: 8caceaa5d097f1ded2decbcf8a95c6ab7b06631f
last_modified_at: 2023-07-16
related_topics:
  - title: 中文 version
    url: /zh/common/heroku.html
    icon: bi bi-globe
---
# heroku

Create and manage Heroku apps.
More information: <https://www.heroku.com/>.

- Log in to your Heroku account:

`heroku login`

- Create a Heroku app:

`heroku create`

- Show logs for an app:

`heroku logs --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Run a one-off process inside a dyno (Heroku virtual machine):

`heroku run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- List dynos (Heroku virtual machines) for an app:

`heroku ps --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>

- Permanently destroy an app:

`heroku destroy --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>
