---
layout: page
title: linux/lsattr (English)
description: "List file attributes on a Linux filesystem."
content_hash: 0177b636f58b1b1dc59c0923a032e211afffe4bb
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/lsattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsattr

List file attributes on a Linux filesystem.
More information: <https://manned.org/lsattr>.

- Display the attributes of the files in the current directory:

`lsattr`

- List the attributes of files in a particular path:

`lsattr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>

- List file attributes recursively in the current and subsequent directories:

`lsattr -R`

- Show attributes of all the files in the current directory, including hidden ones:

`lsattr -a`

- Display attributes of directories in the current directory:

`lsattr -d`
