---
layout: page
title: common/passwd (English)
description: "Change a user's password."
content_hash: c4290adeafea716d48301774cf639fd7216d8ad3
last_modified_at: 2023-11-15
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

Change a user's password.
More information: <https://manned.org/passwd>.

- Change the password of the current user interactively:

`passwd`

- Change the password of a specific user:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Get the current status of the user:

`passwd -S`

- Make the password of the account blank (it will set the named account passwordless):

`passwd -d`
