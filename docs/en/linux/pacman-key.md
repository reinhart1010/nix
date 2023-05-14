---
layout: page
title: linux/pacman-key (English)
description: "Wrapper script for GnuPG used to manage pacman's keyring."
content_hash: 43b50cc38ef1c83503b87a73c9379b7643ab7442
last_modified_at: 2023-05-14
related_topics:
  - title: français version
    url: /fr/linux/pacman-key.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-key.html
    icon: bi bi-globe
---
# pacman-key

Wrapper script for GnuPG used to manage pacman's keyring.
See also: `pacman`.
More information: <https://man.archlinux.org/man/pacman-key>.

- Initialize the pacman keyring:

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
