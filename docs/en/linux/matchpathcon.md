---
layout: page
title: linux/matchpathcon (English)
description: "Lookup the persistent SELinux security context setting of a path."
content_hash: 2662096d1f9af4d2e9d340b2f7619d4a6a8815bc
last_modified_at: 2024-05-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/matchpathcon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># matchpathcon

Lookup the persistent SELinux security context setting of a path.
See also: `semanage-fcontext`, `secon`, `chcon`, `restorecon`.
More information: <https://manned.org/man/matchpathcon.8>.

- Lookup the persistent security context setting of an absolute path:

`matchpathcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- Restrict lookup to settings on a specific file type:

`matchpathcon -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file|dir|pipe|chr_file|blk_file|lnk_file|sock_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>

- [V]erify that the persistent and current security context of a path agree:

`matchpathcon -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>
