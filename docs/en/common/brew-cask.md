---
layout: page
title: common/brew-cask (English)
description: "CLI workflow for the administration of macOS applications distributed as binaries."
content_hash: c459d3b4dbdba401d7fa9600b666d300513a3606
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
# brew --cask

CLI workflow for the administration of macOS applications distributed as binaries.
This command was previously called `brew cask`, it has been deprecated in favor of the `brew --cask` flag.
More information: <https://github.com/Homebrew/homebrew-cask>.

- Search for formulas and casks:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Install a cask:

`brew install --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- List all installed casks:

`brew list --cask`

- List installed casks that have newer versions available:

`brew outdated --cask`

- Upgrade an installed cask (if no cask name is given, all installed casks are upgraded):

`brew upgrade --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Uninstall a cask:

`brew uninstall --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Uninstall a cask and remove related settings and files:

`brew zap --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>

- Display information about a given cask:

`brew info --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask_name</span>
