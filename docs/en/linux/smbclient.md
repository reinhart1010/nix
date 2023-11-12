---
layout: page
title: linux/smbclient (English)
description: "FTP-like client to access SMB/CIFS resources on servers."
content_hash: dac6d02ea65f1db494e7f17a1cfe65228f75b356
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/smbclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# smbclient

FTP-like client to access SMB/CIFS resources on servers.
More information: <https://manned.org/smbclient>.

- Connect to a share (user will be prompted for password; `exit` to quit the session):

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>

- Connect with a different username:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Connect with a different workgroup:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --workgroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Connect with a username and password:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username%password</span>

- Download a file from the server:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --command "get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>`"`

- Upload a file to the server:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//server/share</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --command "put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>`"`

- List the shares from a server anonymously:

`smbclient --list=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` --no-pass`
