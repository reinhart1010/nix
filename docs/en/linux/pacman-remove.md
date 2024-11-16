---
layout: page
title: linux/pacman-remove (English)
description: "Arch Linux package manager utility."
content_hash: a15e65c9d524e098e87d370dcd28561e561c1925
last_modified_at: 2024-11-16
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
  - title: 한국어 version
    url: /ko/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

Arch Linux package manager utility.
See also: `pacman`.
More information: <https://manned.org/pacman.8>.

- [R]emove a package and its dependencies recur[s]ively:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [R]emove a package and its dependencies. Also do [n]ot save backups of configuration files:

`sudo pacman -Rsn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [R]emove a package without prompting:

`sudo pacman -R --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- [R]emove orphan packages (installed as [d]ependencies but no[t] required by any package):

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]emove a package and [c]ascade that to all packages that depend on it:

`sudo pacman -Rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- List and [p]rint packages that would be affected (does not [R]emove any packages):

`pacman -Rp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Display [h]elp:

`pacman -Rh`
