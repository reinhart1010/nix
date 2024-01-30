---
layout: page
title: linux/pacman-key (English)
description: "Wrapper script for GnuPG used to manage pacman's keyring."
content_hash: 00018acb7efdf6c23ede8941860bd46425bdbfa4
last_modified_at: 2024-01-30
related_topics:
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman-key

Wrapper script for GnuPG used to manage pacman's keyring.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman-key>.

- Initialize the `pacman` keyring:

`sudo pacman-key --init`

- Add the default Arch Linux keys:

`sudo pacman-key --populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archlinux</span>

- List keys from the public keyring:

`pacman-key --list-keys`

- Add the specified keys:

`sudo pacman-key --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyfile.gpg</span>

- Receive a key from a key server:

`sudo pacman-key --recv-keys "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- Print the fingerprint of a specific key:

`pacman-key --finger "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- Sign an imported key locally:

`sudo pacman-key --lsign-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`

- Remove a specific key:

`sudo pacman-key --delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|name|email</span>`"`
