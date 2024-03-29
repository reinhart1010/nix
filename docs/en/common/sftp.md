---
layout: page
title: common/sftp (English)
description: "Secure File Transfer Program."
content_hash: 6f97b1e672d892c8eec52f6f48c725c48d157fb8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sftp

Secure File Transfer Program.
Interactive program to copy files between hosts over SSH.
For non-interactive file transfers, see `scp` or `rsync`.
More information: <https://manned.org/sftp>.

- Connect to a remote server and enter an interactive command mode:

`sftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Connect using an alternate port:

`sftp -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- Connect using a predefined host (in `~/.ssh/config`):

`sftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Transfer remote file to the local system:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/remote_file</span>

- Transfer local file to the remote system:

`put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/local_file</span>

- Transfer remote directory to the local system recursively (works with `put` too):

`get -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/remote_directory</span>

- Get list of files on local machine:

`lls`

- Get list of files on remote machine:

`ls`
