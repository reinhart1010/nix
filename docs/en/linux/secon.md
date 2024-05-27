---
layout: page
title: linux/secon (English)
description: "Get the SELinux security context of a file, pid, current execution context, or a context specification."
content_hash: 99cc748341fcf38e99dc9ec6cb823a7c37d4bbe1
last_modified_at: 2024-05-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/secon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># secon

Get the SELinux security context of a file, pid, current execution context, or a context specification.
See also: `semanage`, `runcon`, `chcon`.
More information: <https://manned.org/man/secon>.

- Get the security context of the current execution context:

`secon`

- Get the current security context of a process:

`secon --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Get the current security context of a file, resolving all intermediate symlinks:

`secon --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Get the current security context of a symlink itself (i.e. do not resolve):

`secon --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- Parse and explain a context specification:

`secon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_u:system_r:container_t:s0:c899,c900</span>
