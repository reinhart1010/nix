---
layout: page
title: common/passwd (English)
description: "Change a user's password."
content_hash: 689e38c78e3adf2a10625cdf12bb30d5e8a2a924
last_modified_at: 2024-09-04
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

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--status</span>

- Make the password of the account blank (it will set the named account passwordless):

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>
