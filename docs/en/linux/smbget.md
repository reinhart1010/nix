---
layout: page
title: linux/smbget (English)
description: "`wget`-like utility for downloading files from SMB servers."
content_hash: 2ca2070ab3148132cab61a8a056d76de3fa67a94
---
# smbget

`wget`-like utility for downloading files from SMB servers.
More information: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- Download a file from a server:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>

- Download a share or directory recursively:

`smbget --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share</span>

- Connect with a username and password:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username%password</span>

- Require encrypted transfers:

`smbget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb://server/share/file</span>` --encrypt`
