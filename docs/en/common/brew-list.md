---
layout: page
title: common/brew-list (English)
description: "List installed formulae/casks or their files."
content_hash: 96064f65001c4a79fd979f8ce918fb1e3982066a
last_modified_at: 2024-12-04
related_topics:
  - title: Indonesia version
    url: /id/common/brew-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew list

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

- List only pinned formulae:

`brew list --pinned`
