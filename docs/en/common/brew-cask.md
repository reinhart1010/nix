---
layout: page
title: common/brew-cask (English)
description: "Package manager for macOS applications distributed as binaries."
content_hash: 42f9bb5417bf2a056ddf0cf07fcc4de93779d4ee
related_topics:
  - title: Deutsch version
    url: /de/common/brew-cask.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-cask.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew-cask.html
    icon: bi bi-globe
---
# brew cask

Package manager for macOS applications distributed as binaries.
More information: <https://github.com/Homebrew/homebrew-cask>.

- Search for formulas and casks:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Install a cask:

`brew cask install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- List all installed casks:

`brew list --cask`

- List installed casks that have newer versions available:

`brew outdated --cask`

- Upgrade an installed cask (if no cask name is given, all installed casks are upgraded):

`brew upgrade --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Uninstall a cask:

`brew cask uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Uninstall a cask and remove related settings and files:

`brew cask zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Display information about a given cask:

`brew cask info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>
