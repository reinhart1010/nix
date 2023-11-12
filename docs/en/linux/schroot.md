---
layout: page
title: linux/schroot (English)
description: "Run a command or start an interactive shell with a different root directory. More customizable than `chroot`."
content_hash: 1fb09cda3a0a34ba3d348cf1c40f96c0c51c570a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# schroot

Run a command or start an interactive shell with a different root directory. More customizable than `chroot`.
More information: <https://wiki.debian.org/Schroot>.

- List available chroots:

`schroot --list`

- Run a command in a specific chroot:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command with options in a specific chroot:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_options</span>

- Run a command in all available chroots:

`schroot --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Start an interactive shell within a specific chroot as a specific user:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Begin a new session (a unique session ID is returned on `stdout`):

`schroot --begin-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>

- Connect to an existing session:

`schroot --run-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_id</span>

- End an existing session:

`schroot --end-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_id</span>
