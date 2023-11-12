---
layout: page
title: common/qcp (English)
description: "Copy files using the default text editor to define the filenames."
content_hash: 550a63155e7431accc63a5a860700f28a9166968
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# qcp

Copy files using the default text editor to define the filenames.
More information: <https://www.nongnu.org/renameutils/>.

- Copy a single file (open an editor with the source filename on the left and the target filename on the right):

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Copy multiple JPG files:

`qcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Copy files, but swap the positions of the source and the target filenames in the editor:

`qcp --option swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>
