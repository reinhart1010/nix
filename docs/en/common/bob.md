---
layout: page
title: common/bob (English)
description: "Manage and switch between Neovim versions."
content_hash: 71b212ac86156c6b735c227ba3b1e00ae19d5c3e
last_modified_at: 2023-05-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bob

Manage and switch between Neovim versions.
More information: <https://github.com/MordechaiHadad/bob>.

- Install and switch to the specified version of Neovim:

`bob use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- List installed and currently used versions of Neovim:

`bob list`

- Uninstall the specified version of Neovim:

`bob uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nightly|stable|latest|version_string|commit_hash</span>

- Uninstall Neovim and erase any changes `bob` has made:

`bob erase`

- Roll back to a previous nightly version:

`bob rollback`
