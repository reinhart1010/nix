---
layout: page
title: linux/pacman-upgrade (English)
description: "Arch Linux package manager utility."
content_hash: e26c30853c70f19e20003d2aaceecb3ed3aa8b84
last_modified_at: 2024-12-26
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://manned.org/pacman.8>.

- Install one or more packages from files:

`sudo pacman -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package2.pkg.tar.zst</span>

- Install a package without prompting:

`sudo pacman -U --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Overwrite conflicting files during a package installation:

`sudo pacman -U --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Install a package, skipping the dependency [(d)] version checks:

`sudo pacman -Ud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Fetch and [p]rint packages that would be affected by upgrade (does not install any packages):

`pacman -Up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Display help:

`pacman -U --help`
