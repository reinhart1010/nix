---
layout: page
title: linux/chsh (English)
description: "Change the user's login shell."
content_hash: b2bd19ae84ce6cba61f9d182d5ebb5f2336e9d34
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chsh

Change the user's login shell.
More information: <https://manned.org/chsh>.

- Change the current user's login shell interactively:

`chsh`

- Change the current user's login shell:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>

- Change the login shell for a given user:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List available shells:

`chsh --list-shells`
