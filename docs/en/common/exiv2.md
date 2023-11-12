---
layout: page
title: common/exiv2 (English)
description: "Image metadata manipulation tool."
content_hash: e0c1463bb2ce0435917cd847809040da95c45660
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# exiv2

Image metadata manipulation tool.
More information: <https://www.exiv2.org/manpage.html>.

- Print a summary of the image Exif metadata:

`exiv2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print all metadata (Exif, IPTC, XMP) with interpreted values:

`exiv2 -P kt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print all metadata with raw values:

`exiv2 -P kv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Delete all metadata from an image:

`exiv2 -d a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Delete all metadata, preserving the file timestamp:

`exiv2 -d a -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Rename the file, prepending the date and time from metadata (not from the file timestamp):

`exiv2 -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'%Y%m%d_%H%M%S_:basename:'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
