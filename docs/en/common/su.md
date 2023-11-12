---
layout: page
title: common/su (English)
description: "Switch shell to another user."
content_hash: b6f8625754abe9e60849584c14049a6d572bc2ee
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/su.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/su.html
    icon: bi bi-globe
tldri18n_status: 2
---
# su

Switch shell to another user.
More information: <https://manned.org/su>.

- Switch to superuser (requires the root password):

`su`

- Switch to a given user (requires the user's password):

`su `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Switch to a given user and simulate a full login shell:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Execute a command as another user:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
