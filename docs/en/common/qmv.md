---
layout: page
title: common/qmv (English)
description: "Move files and directories using the default text editor to define the filenames."
content_hash: b978973ce3bc9140e27ccd431488ffbfbb03e9a1
---
# qmv

Move files and directories using the default text editor to define the filenames.
More information: <https://www.nongnu.org/renameutils/>.

- Move a single file (open an editor with the source filename on the left and the target filename on the right):

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Move multiple JPG files:

`qmv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Move multiple directories:

`qmv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory3</span>

- Move all files and directories inside a directory:

`qmv --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Move files, but swap the positions of the source and the target filenames in the editor:

`qmv --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>
