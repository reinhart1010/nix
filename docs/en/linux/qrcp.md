---
layout: page
title: linux/qrcp (English)
description: "A file transfer tool."
content_hash: b3a864596ba90899da0eb4a95e59588d1ffb4c80
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qrcp

A file transfer tool.
More information: <https://github.com/claudiodangelis/qrcp>.

- Send a file or directories:

`qrcp send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory path/to/file_directory ...</span>

- Receive files:

`qrcp receive`

- Compress content before transferring:

`qrcp send --zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Specify a [p]ort to use:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Specify the network [i]nterface to use:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --interface interface`

- Keep the server alive:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --keep-alive`
