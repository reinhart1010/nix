---
layout: page
title: linux/fuser (English)
description: "Display process IDs currently using files or sockets."
content_hash: b25e7d15fd830e7358d4f965116d97f833520822
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fuser

Display process IDs currently using files or sockets.
More information: <https://manned.org/fuser>.

- Find which processes are accessing a file or directory:

`fuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show more fields (`USER`, `PID`, `ACCESS` and `COMMAND`):

`fuser --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Identify processes using a TCP socket:

`fuser --namespace tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Kill all processes accessing a file or directory (sends the `SIGKILL` signal):

`fuser --kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Find which processes are accessing the filesystem containing a specific file or directory:

`fuser --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Kill all processes with a TCP connection on a specific port:

`fuser --kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>`/tcp`
