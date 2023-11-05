---
layout: page
title: common/brew-upgrade (English)
description: "Upgrade outdated formulae and casks."
content_hash: 73d10b636ce39cdbf09ffa23e573c2fc00716a5c
last_modified_at: 2023-11-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew upgrade

Upgrade outdated formulae and casks.
More information: <https://docs.brew.sh/Manpage#upgrade-options-outdated_formulaoutdated_cask->.

- Upgrade all outdated casks and formulae:

`brew upgrade`

- Upgrade a specific formula/cask:

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- Print what would be upgraded, but don't actually upgrade anything:

`brew upgrade --dry-run`
