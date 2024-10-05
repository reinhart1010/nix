---
layout: page
title: common/tlmgr (English)
description: "Manage packages and configuration options of an existing TeX Live installation."
content_hash: 1565600df138a713391849fc012ca6fb55e9d165
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/tlmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr

Manage packages and configuration options of an existing TeX Live installation.
Some subcommands such as `paper` have their own usage documentation.
More information: <https://www.tug.org/texlive/tlmgr.html>.

- Install a package and its dependencies:

`tlmgr install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies:

`tlmgr remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display information about a package:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Update all packages:

`tlmgr update --all`

- Show possible updates without updating anything:

`tlmgr update --list`

- Start a GUI version of tlmgr:

`tlmgr gui`

- List all TeX Live configurations:

`tlmgr conf`
