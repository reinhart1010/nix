---
layout: page
title: common/transfersh (English)
description: "An unofficial command-line client for transfer.sh."
content_hash: 15fa21bf1531b96b980c6859d275ec1f385e70a1
---
# transfersh

An unofficial command-line client for transfer.sh.
More information: <https://github.com/AlpixTM/transfersh>.

- Upload a file to transfer.sh:

`transfersh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Upload a file showing a progress bar (requires Python package `requests_toolbelt`):

`transfersh --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Upload a file using a different file name:

`transfersh --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Upload a file to a custom transfer.sh server:

`transfersh --servername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upload.server.name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Upload all files from a directory recursively:

`transfersh --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/</span>

- Upload a specific directory as an uncompressed tar:

`transfersh -rt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
