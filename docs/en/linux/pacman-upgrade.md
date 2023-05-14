---
layout: page
title: linux/pacman-upgrade (English)
description: "Arch Linux package manager utility."
content_hash: d4e1c9f22cae3df8ef73fa7e69e4a22baf49b7b0
last_modified_at: 2023-05-14
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
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
---
# pacman --upgrade

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Install one or more packages from files:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package2.pkg.tar.zst</span>

- Install a package without prompting:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Overwrite conflicting files during a package installation:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Install a package, skipping the dependency version checks:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- List packages that would be affected (does not install any packages):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Display help:

`pacman --upgrade --help`
