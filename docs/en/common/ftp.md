---
layout: page
title: common/ftp (English)
description: "Tools to interact with a server via File Transfer Protocol."
content_hash: 0f00136ac70be9abbd14ad1dcc4e9b32d5cd0391
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Tools to interact with a server via File Transfer Protocol.
More information: <https://manned.org/ftp>.

- Connect to an FTP server:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.example.com</span>

- Connect to an FTP server specifying its IP address and port:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Switch to binary transfer mode (graphics, compressed files, etc):

`binary`

- Transfer multiple files without prompting for confirmation on every file:

`prompt off`

- Download multiple files (glob expression):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Upload multiple files (glob expression):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Delete multiple files on the remote server:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Rename a file on the remote server:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>
