---
layout: page
title: windows/mount (English)
description: "Mount Network File System (NFS) network shares."
content_hash: 3ca83190a45e7e379020a7a0a9a23b5ec3629ffd
last_modified_at: 2024-08-20
related_topics:
  - title: italiano version
    url: /it/windows/mount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount

Mount Network File System (NFS) network shares.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- Mount a share to the "Z" drive letter:

`mount \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Mount a share to the next available drive letter:

`mount \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` *`

- Mount a share with a read timeout in seconds (defaults to 0.8, can be 0.9 or 1 to 60):

`mount -o timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Mount a share and retry up to 10 times if it fails:

`mount -o retry=10 \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Mount a share with forced case sensitivity:

`mount -o casesensitive \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Mount a share as an anonymous user:

`mount -o anon \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>

- Mount a share using a specific mount type:

`mount -o mtype=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">soft|hard</span>` \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">share_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Z:</span>
