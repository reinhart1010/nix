---
layout: page
title: linux/gio-trash (English)
description: "Move files to the trash bin."
content_hash: a4c08918843dc22dca207df5dbb73fd3ca8cc63f
last_modified_at: 2024-02-01
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gio-trash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gio trash

Move files to the trash bin.
Used by GNOME to handle trash.
More information: <https://manned.org/gio.1>.

- Move specific files to the trash bin:

`gio trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- List trash bin items:

`gio trash --list`

- Restore a specific item from trash using its ID:

`gio trash trash://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
