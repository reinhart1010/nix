---
layout: page
title: linux/etckeeper (English)
description: "Track system configuration files in Git."
content_hash: af9fd206762d797511224b643a3e39e02a1251dd
---
# etckeeper

Track system configuration files in Git.
More information: <http://etckeeper.branchable.com/>.

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
