---
layout: page
title: linux/schroot (English)
description: "Run command or start an interactive shell with a different root directory. More customizable than `chroot`."
content_hash: 854aaabbfeb46e6647f19ea5b279f90b575369c5
---
# schroot

Run command or start an interactive shell with a different root directory. More customizable than `chroot`.
More information: <https://wiki.debian.org/Schroot>.

- Run a command in a specific chroot:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command with options in a specific chroot:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_options</span>

- Run a command in all available chroots:

`schroot --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Start an interactive shell within a specific chroot as a specific user:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- List available chroots:

`schroot --list`
