---
layout: page
title: linux/chsh (English)
description: "Change user's login shell."
content_hash: 1353f724bfa95676052008b7dc48369423ed3cb1
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# chsh

Change user's login shell.
Part of `util-linux`.
More information: <https://manned.org/chsh>.

- Set a specific login shell for the current user interactively:

`sudo chsh`

- Set a specific login [s]hell for the current user:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Set a login [s]hell for a specific user:

`sudo chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- [l]ist available shells:

`sudo chsh --list-shells`
