---
layout: page
title: linux/e2undo (English)
description: "Replay undo logs for an ext2/ext3/ext4 filesystem."
content_hash: 33dcdfdc9bf378ba2b76459b85a4aba711314a22
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# e2undo

Replay undo logs for an ext2/ext3/ext4 filesystem.
This can be used to undo a failed operation by an e2fsprogs program.
More information: <https://man7.org/linux/man-pages/man8/e2undo.8.html>.

- Display information about a specific undo file:

`e2undo -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/undo_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Perform a dry-run and display the candidate blocks for replaying:

`e2undo -nv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/undo_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Perform an undo operation:

`e2undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/undo_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Perform an undo operation and display verbose information:

`e2undo -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/undo_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Write the old contents of the block to an undo file before overwriting a file system block:

`e2undo -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.e2undo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/undo_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
