---
layout: page
title: linux/pacman-remove (English)
description: "Arch Linux package manager utility."
content_hash: 061ba206489826393a07317fbf3499bdf80830cd
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
---
# pacman --remove

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman.8>.

- Remove a package and its dependencies:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package and both its dependencies and configuration files:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a package without prompting:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Remove a package and all packages that depend on it:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List packages that would be affected (does not remove any packages):

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Display help for this subcommand:

`pacman --remove --help`
