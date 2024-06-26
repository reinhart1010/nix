---
layout: page
title: common/cradle-install (English)
description: "Install the Cradle PHP framework components."
content_hash: b0cd10a12b935dc500f4a6d0a45c11d836cbb257
last_modified_at: 2024-04-26
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle install

Install the Cradle PHP framework components.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Install Cradle's components (User will be prompted for further details):

`cradle install`

- Forcefully overwrite files:

`cradle install --force`

- Skip running SQL migrations:

`cradle install --skip-sql`

- Skip running package updates:

`cradle install --skip-versioning`

- Use specific database details:

`cradle install -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
