---
layout: page
title: common/passwd (English)
description: "Passwd is a tool used to change a user's password."
content_hash: d9a720c294990860ae4656582606b9407d35c877
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/passwd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# passwd

Passwd is a tool used to change a user's password.
More information: <https://manned.org/passwd>.

- Change the password of the current user interactively:

`passwd`

- Change the password of a specific user:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Get the current status of the user:

`passwd -S`

- Make the password of the account blank (it will set the named account passwordless):

`passwd -d`
