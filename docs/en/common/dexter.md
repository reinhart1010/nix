---
layout: page
title: common/dexter (English)
description: "Authenticate the `kubectl` users with OpenId Connect."
content_hash: 2deab6a5be9ccb7c42d0756d2556c0d435b92fc6
last_modified_at: 2024-02-15
related_topics:
  - title: italiano version
    url: /it/common/dexter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dexter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dexter

Authenticate the `kubectl` users with OpenId Connect.
More information: <https://github.com/gini/dexter>.

- Create and authenticate a user with Google OIDC:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_id</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_secret</span>

- Override the default kube configuration file location:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_id</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client_secret</span>` --kube-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sample/config</span>
