---
layout: page
title: common/brew-list (English)
description: "List installed formulae/casks or their files."
content_hash: 667d0fa3a0298f64bc7803f77a986a508b714d2f
last_modified_at: 2023-11-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew list

List installed formulae/casks or their files.
More information: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- List all installed formulae and casks:

`brew list`

- List files belonging to an installed formula:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- List artifacts of a cask:

`brew list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>

- List only formulae:

`brew list --formula`

- List only casks:

`brew list --cask`
