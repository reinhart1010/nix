---
layout: page
title: common/tlmgr (English)
description: "Manages packages and configuration options of an existing TeX Live installation."
content_hash: 41dfa212e85d66cdf09632749779624e36e92da1
related_topics:
  - title: Deutsch version
    url: /de/common/tlmgr.html
    icon: bi bi-globe
---
# tlmgr

Manages packages and configuration options of an existing TeX Live installation.
Some subcommands such as `tlmgr paper` have their own usage documentation.
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
