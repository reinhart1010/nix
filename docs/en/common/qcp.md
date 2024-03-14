---
layout: page
title: common/qcp (English)
description: "Copy files using the default text editor to define the filenames."
content_hash: d7f5a62f89bebacac0ce3abf8939e8e3f92af3aa
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# qcp

Copy files using the default text editor to define the filenames.
More information: <https://www.nongnu.org/renameutils/>.

- Copy a single file (open an editor with the source filename on the left and the target filename on the right):

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Copy multiple JPEG files:

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Copy files, but swap the positions of the source and the target filenames in the editor:

`qcp --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>
