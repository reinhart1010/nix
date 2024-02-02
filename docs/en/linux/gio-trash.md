---
layout: page
title: linux/gio-trash (English)
description: "Move files to the trash bin."
content_hash: a4c08918843dc22dca207df5dbb73fd3ca8cc63f
last_modified_at: 2024-02-02
tldri18n_status: 2
---
# gio trash

Move files to the trash bin.
Used by GNOME to handle trash.
More information: <https://manned.org/gio.1>.

- Move specific files to the trash bin:

`gio trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- List trash bin items:

`gio trash --list`

- Restore a specific item from trash using its ID:

`gio trash trash://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
