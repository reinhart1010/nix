---
layout: page
title: linux/fakeroot (English)
description: "Run a command in an environment faking root privileges for file manipulation."
content_hash: 40a189e0963386872d9502288e1ccb9933df286d
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# fakeroot

Run a command in an environment faking root privileges for file manipulation.
More information: <https://manned.org/fakeroot.1>.

- Start the default shell as fakeroot:

`fakeroot`

- Run a command as fakeroot:

`fakeroot -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Run a command as fakeroot and save the environment to a file on exit:

`fakeroot -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Load a fakeroot environment and run a command as fakeroot:

`fakeroot -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Run a command keeping the real ownership of files instead of pretending they are owned by root:

`fakeroot --unknown-is-real -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Display help:

`fakeroot --help`
