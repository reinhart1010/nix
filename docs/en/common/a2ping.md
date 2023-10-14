---
layout: page
title: common/a2ping (English)
description: "Convert images into EPS or PDF files."
content_hash: 0694259dc5300cccf98f251f83782f77c91b6771
last_modified_at: 2023-10-14
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># a2ping

Convert images into EPS or PDF files.
More information: <https://manned.org/a2ping>.

- Convert an image to PDF (Note: Specifying an output filename is optional):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- Compress the document using the specified method:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scan HiResBoundingBox if present (Note: It Defaults to yes):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Allow page content below and left of the origin (Note: It defaults to no):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pass extra arguments to `gs:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Pass extra arguments to external program (i.e pdftops):

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`a2ping -h`
