---
layout: page
title: linux/chage (English)
description: "Change user account and password expiry information."
content_hash: 2c94e3f55de58ea8046506fb8bd610b6e7f88dfb
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/chage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/chage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chage

Change user account and password expiry information.
More information: <https://manned.org/chage>.

- List password information for the user:

`chage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Enable password expiration in 10 days:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Disable password expiration:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Set account expiration date:

`sudo chage --expiredate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Force user to change password on next log in:

`sudo chage --lastday `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
