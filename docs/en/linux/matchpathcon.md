---
layout: page
title: linux/matchpathcon (English)
description: "Lookup the persistent SELinux security context setting of a path."
content_hash: 4d43c7ecb6602fbf0bce5819a51d02652ed103b7
last_modified_at: 2024-09-19
tldri18n_status: 2
---
# matchpathcon

Lookup the persistent SELinux security context setting of a path.
See also: `semanage-fcontext`, `secon`, `chcon`, `restorecon`.
More information: <https://manned.org/matchpathcon.8>.

- Lookup the persistent security context setting of an absolute path:

`matchpathcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- Restrict lookup to settings on a specific file type:

`matchpathcon -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file|dir|pipe|chr_file|blk_file|lnk_file|sock_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- [V]erify that the persistent and current security context of a path agree:

`matchpathcon -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>
