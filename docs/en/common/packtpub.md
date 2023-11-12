---
layout: page
title: common/packtpub (English)
description: "Download freely offered books from packtpub.com."
content_hash: 720e92a0e101e5160c411d23202730b23fecac2c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# packtpub

Download freely offered books from packtpub.com.
More information: <https://github.com/vladimyr/packtpub-cli>.

- Download the daily offer book into the current directory with the specified book format (defaults to `pdf`):

`packtpub download --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf|ebup|mobi</span>

- Download the daily offer book into the specified directory:

`packtpub download --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start an interactive login to packtpub.com:

`packtpub login`

- Log out from packtpub.com:

`packtpub logout`

- Display the daily offer:

`packtpub view-offer`

- Open the daily offer in the default web browser:

`packtpub view-offer`

- Display the currently logged-in user:

`packtpub whoami`
