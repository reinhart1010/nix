---
layout: page
title: linux/atool (English)
description: "Manage archives of various formats."
content_hash: 83b23e783bbd3dd82ff549fd8442102e0ecac7e6
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/atool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atool

Manage archives of various formats.
More information: <https://www.nongnu.org/atool/>.

- List files in a zip archive:

`atool --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Unpack a tar.gz archive into a new subdirectory (or current directory if it contains only one file):

`atool --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.tar.gz</span>

- Create a new 7zip archive with two files:

`atool --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Extract all zip and rar archives in the current directory:

`atool --each --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip *.rar</span>
