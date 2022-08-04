---
layout: page
title: linux/fakeroot (English)
description: "Run a command in an environment faking root privileges for file manipulation."
content_hash: 209f48ce0826b8db3783773ed4d2b1ba8788e333
---
# fakeroot

Run a command in an environment faking root privileges for file manipulation.
More information: <https://manpages.debian.org/latest/fakeroot/fakeroot.1.html>.

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
