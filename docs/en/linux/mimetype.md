---
layout: page
title: linux/mimetype (English)
description: "Automatically determine the MIME type of a file."
content_hash: 8c323d77b131f2bc2e481a4a712237330b45d6d0
---
# mimetype

Automatically determine the MIME type of a file.
More information: <https://manned.org/mimetype>.

- Print the MIME type of a given file:

`mimetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display only the MIME type, and not the filename:

`mimetype --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a description of the MIME type:

`mimetype --describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Determine the MIME type of stdin (does not check a filename):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | mimetype --stdin`

- Display debug information about how the MIME type was determined:

`mimetype --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display all the possible MIME types of a given file in confidence order:

`mimetype --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Explicitly specify the 2-letter language code of the output:

`mimetype --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
