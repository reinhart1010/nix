---
layout: page
title: linux/deluser (English)
description: "Delete a user from the system."
content_hash: e40c17967b090a377675b88048f485a8054d58d1
related_topics:
  - title: italiano version
    url: /it/linux/deluser.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/deluser.html
    icon: bi bi-globe
---
# deluser

Delete a user from the system.
More information: <https://manpages.debian.org/latest/adduser/deluser.html>.

- Remove a user:

`sudo deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user and their home directory:

`sudo deluser --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user and their home, but backup their files into a `.tar.gz` file in the specified directory:

`sudo deluser --backup-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_directory</span>` --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user, and all files owned by them:

`sudo deluser --remove-all-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
