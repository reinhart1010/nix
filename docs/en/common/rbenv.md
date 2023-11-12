---
layout: page
title: common/rbenv (English)
description: "A tool to easily install Ruby versions and manage application environments."
content_hash: eb925338c133ef7fd81756a5b0125b0f521a5843
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/common/rbenv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rbenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rbenv

A tool to easily install Ruby versions and manage application environments.
More information: <https://github.com/rbenv/rbenv>.

- Install a Ruby version:

`rbenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display a list of the latest stable versions for each Ruby:

`rbenv install --list`

- Display a list of installed Ruby versions:

`rbenv versions`

- Use a specific Ruby version across the whole system:

`rbenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Use a specific Ruby version for an application/project directory:

`rbenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display the currently selected Ruby version:

`rbenv version`

- Uninstall a Ruby version:

`rbenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display all Ruby versions that contain the specified executable:

`rbenv whence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>
