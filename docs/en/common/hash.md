---
layout: page
title: common/hash (English)
description: "View cached executable locations."
content_hash: b9a54c1e0859caa18159ade441c5ee88df8d947c
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# hash

View cached executable locations.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-hash>.

- View cached command locations for the current shell:

`hash`

- Clear the hash table:

`hash -r`

- Delete a specific command from the hash table:

`hash -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Print the full path of `command`:

`hash -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
