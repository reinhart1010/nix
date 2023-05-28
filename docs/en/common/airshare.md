---
layout: page
title: common/airshare (English)
description: "Transfer data between two machines in a local network."
content_hash: bdb768f0cf8b8a03e77b73380e9ed9c267c412bc
last_modified_at: 2023-05-28
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airshare

Transfer data between two machines in a local network.
More information: <https://airshare.rtfd.io/en/latest/cli.html>.

- Share files or directories:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Receive a file:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Host a receiving server (use this to be able to upload files using the web interface):

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Send files or directories to a receiving server:

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Send files whose paths have been copied to the clipboard:

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Receive a file and copy it to the clipboard:

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>
