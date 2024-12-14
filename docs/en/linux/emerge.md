---
layout: page
title: linux/emerge (English)
description: "Gentoo Linux package manager utility."
content_hash: 45b03653b952a73acaceb08152b199c4459a18ae
last_modified_at: 2024-12-14
related_topics:
  - title: 한국어 version
    url: /ko/linux/emerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emerge

Gentoo Linux package manager utility.
For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
More information: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Synchronize all packages:

`sudo emerge --sync`

- Update all packages, including dependencies:

`sudo emerge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-avuDN|--ask --verbose --update --deep --newuse</span>` @world`

- Resume a failed updated, skipping the failing package:

`sudo emerge --resume --skipfirst`

- Install a new package, with confirmation:

`sudo emerge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-av|--ask --verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package and its dependencies with confirmation:

`sudo emerge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-avc|--ask --verbose --depclean</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove orphaned packages (installed as dependencies but no longer required by any package):

`sudo emerge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-avc|--ask --verbose --depclean</span>

- Search the package database for a keyword:

`emerge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--searchdesc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
