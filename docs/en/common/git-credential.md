---
layout: page
title: common/git-credential (English)
description: "Retrieve and store user credentials."
content_hash: 07c11010c5e50b7c8aa3e59b523803dee510e096
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-credential.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git credential

Retrieve and store user credentials.
More information: <https://git-scm.com/docs/git-credential>.

- Display credential information, retrieving the username and password from configuration files:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential fill`

- Send credential information to all configured credential helpers to store for later use:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential approve`

- Erase the specified credential information from all the configured credential helpers:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential reject`
