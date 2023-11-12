---
layout: page
title: windows/ftp (English)
description: "Interactively transfer files between a local and remote FTP server."
content_hash: 28ddc48b3e826f6fb069ae6e1a5ce8d157aa0d9c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/ftp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Interactively transfer files between a local and remote FTP server.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Connect to a remote FTP server interactively:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Log in as an anonymous user:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Disable automatic login upon initial connection:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Run a file containing a list of FTP commands:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Download multiple files (glob expression):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Upload multiple files (glob expression):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Delete multiple files on the remote server:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Display detailed help:

`ftp --help`
