---
layout: page
title: linux/compsize (English)
description: "Calculate the compression ratio of a set of files on a btrfs filesystem."
content_hash: 438d2ff8782af98be60f3231102dc96854a6ef1c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# compsize

Calculate the compression ratio of a set of files on a btrfs filesystem.
See also `btrfs filesystem` for recompressing a file by defragmenting it.
More information: <https://github.com/kilobyte/compsize>.

- Calculate the current compression ratio for a file or directory:

`sudo compsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Don't traverse filesystem boundaries:

`sudo compsize --one-file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show raw byte counts instead of human-readable sizes:

`sudo compsize --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
