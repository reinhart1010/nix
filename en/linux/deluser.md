---
layout: page
title: linux/deluser (English)
description: "Delete a user from the system."
content_hash: 19bff6ddb6c339bb1bc26cfc902103c82d969505
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
Note: all commands must be executed as root.
More information: <https://manpages.debian.org/latest/adduser/deluser.html>.

- Remove a user:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user and their home directory:

`deluser --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user and their home, but backup their files into a `.tar.gz` file in the specified directory:

`deluser --backup-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/backup_directory</span>` --remove-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove a user, and all files owned by them:

`deluser --remove-all-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
