---
layout: page
title: common/su (English)
description: "Switch shell to another user."
content_hash: eac8ae1b528b4a27f8415edde13edd21faabca36
related_topics:
  - title: Türkçe version
    url: /tr/common/su.html
    icon: bi bi-globe
---
# su

Switch shell to another user.

- Switch to superuser (requires the root password):

`su`

- Switch to a given user (requires the user's password):

`su `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Switch to a given user and simulate a full login shell:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Execute a command as another user:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
