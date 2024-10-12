---
layout: page
title: linux/etckeeper (English)
description: "Track system configuration files in Git."
content_hash: 3e3ed4fd9ab6b5c127f636368e042e6252b3c7bd
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# etckeeper

Track system configuration files in Git.
More information: <https://etckeeper.branchable.com/>.

- Set up a Git repo and perform various setup tasks (run from `/etc`):

`sudo etckeeper init`

- Commit all changes in `/etc`:

`sudo etckeeper commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Run arbitrary Git commands:

`sudo etckeeper vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>

- Check if there are uncommitted changes (only returns an exit code):

`sudo etckeeper unclean`

- Destroy existing repo and stop tracking changes:

`sudo etckeeper uninit`
