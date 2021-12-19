---
layout: page
title: linux/pacman-key (English)
description: "Wrapper script for GnuPG used to manage pacman's keyring."
content_hash: 16375ea39996f23c50d5d3e4a742c2855782d1e2
related_topics:
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
---
# pacman-key

Wrapper script for GnuPG used to manage pacman's keyring.
More information: <https://man.archlinux.org/man/pacman-key>.

- Initialize the pacman keyring:

`sudo pacman-key --init`

- Add the default ArchLinux keys:

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
