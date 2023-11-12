---
layout: page
title: linux/chattr (English)
description: "Change attributes of files or directories."
content_hash: 4615cfc59f80dd788ae9269129154ba64f46069b
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/chattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chattr

Change attributes of files or directories.
More information: <https://manned.org/chattr>.

- Make a file or directory immutable to changes and deletion, even by superuser:

`chattr +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Make a file or directory mutable:

`chattr -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Recursively make an entire directory and contents immutable:

`chattr -R +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
