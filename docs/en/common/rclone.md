---
layout: page
title: common/rclone (English)
description: "Copy, synchronize or move files and directories to and from many cloud services."
content_hash: a15388d52ed76fbedda327fa5f38f6e5fb4ff8d1
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# rclone

Copy, synchronize or move files and directories to and from many cloud services.
More information: <https://rclone.org>.

- Launch an interactive menu to setup rclone:

`rclone config`

- List contents of a directory on an rclone remote:

`rclone lsf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Copy a file or directory from the local machine to the remote destination:

`rclone copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Copy files changed within the past 24 hours to a remote from the local machine, asking the user to confirm each file:

`rclone copy --interactive --max-age 24h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_directory</span>` `

- Mirror a specific file or directory (Note: Unlike copy, sync removes files from the remote if it does not exist locally):

`rclone sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Delete a remote file or directory (Note: `--dry-run` means test, remove it from the command to actually delete):

`rclone --dry-run delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Mount rclone remote (experimental):

`rclone mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>

- Unmount rclone remote if CTRL-C fails (experimental):

`fusermount -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mount_point</span>
