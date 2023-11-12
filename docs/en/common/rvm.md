---
layout: page
title: common/rvm (English)
description: "A tool for easily installing, managing, and working with multiple ruby environments."
content_hash: 29cd8d77e46f96d2f89afe4335a013a842a4a720
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/rvm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rvm

A tool for easily installing, managing, and working with multiple ruby environments.
More information: <https://rvm.io>.

- Install one or more space-separated versions of Ruby:

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version(s)</span>

- Display a list of installed versions:

`rvm list`

- Use a specific version of Ruby:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set the default Ruby version:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Upgrade a version of Ruby to a new version:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_version</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_version</span>

- Uninstall a version of Ruby and keep its sources:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Remove a version of Ruby and its sources:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Show specific dependencies for your OS:

`rvm requirements`
