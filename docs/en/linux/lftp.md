---
layout: page
title: linux/lftp (English)
description: "Sophisticated file transfer program."
content_hash: 4b757d426062e336c399124a0269b96d23f5f859
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lftp

Sophisticated file transfer program.
More information: <https://lftp.yar.ru/lftp-man.html>.

- Connect to an FTP server:

`lftp --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.example.com</span>

- Download multiple files (glob expression):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/*.png</span>

- Upload multiple files (glob expression):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/*.zip</span>

- Delete multiple files on the remote server:

`mrm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/*.txt</span>

- Rename a file on the remote server:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>

- Download or update an entire directory:

`mirror `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_output_dir</span>

- Upload or update an entire directory:

`mirror -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/local_dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/remote_output_dir</span>
