---
layout: page
title: common/qmv (English)
description: "Move files and directories using the default text editor to define the filenames."
content_hash: bc18a489a7b7f9d8947519a1911cbd76db178372
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# qmv

Move files and directories using the default text editor to define the filenames.
More information: <https://www.nongnu.org/renameutils/>.

- Move a single file (open an editor with the source filename on the left and the target filename on the right):

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Move multiple JPEG files:

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Move multiple directories:

`qmv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory3</span>

- Move all files and directories inside a directory:

`qmv --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Move files, but swap the positions of the source and the target filenames in the editor:

`qmv --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Rename all files and folders in the current directory, but show only target filenames in the editor (you can think of it as a kind of simple mode):

`qmv --format=do .`
