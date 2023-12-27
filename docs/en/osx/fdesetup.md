---
layout: page
title: osx/fdesetup (English)
description: "Set and retrieve FileVault related information."
content_hash: 4c65bc932e36b36b17d3720a2ae74fb83fec9cbb
last_modified_at: 2023-12-27
related_topics:
  - title: español version
    url: /es/osx/fdesetup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fdesetup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdesetup

Set and retrieve FileVault related information.
More information: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- List current FileVault enabled users:

`sudo fdesetup list`

- Get current FileVault status:

`fdesetup status`

- Add FileVault enabled user:

`sudo fdesetup add -usertoadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1</span>

- Enable FileVault:

`sudo fdesetup enable`

- Disable FileVault:

`sudo fdesetup disable`
