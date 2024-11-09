---
layout: page
title: linux/qrcp (English)
description: "A file transfer tool."
content_hash: a6c06f254bc433c2f88514ca4471e3191b4a171c
last_modified_at: 2024-11-09
tldri18n_status: 2
---
# qrcp

A file transfer tool.
More information: <https://github.com/claudiodangelis/qrcp>.

- Send a file or directories:

`qrcp send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory path/to/file_directory ...</span>

- Receive files:

`qrcp receive`

- Compress content before transferring:

`qrcp send --zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Use a specific [p]ort:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- Use a specific network [i]nterface:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Keep the server alive:

`qrcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">send|receive</span>` --keep-alive`
