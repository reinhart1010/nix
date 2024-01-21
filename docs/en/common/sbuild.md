---
layout: page
title: common/sbuild (English)
description: "Build a Debian binary package in a clean `chroot` environment."
content_hash: 219215edfa896fa63f2a1502e141a322d1511f3e
last_modified_at: 2024-01-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sbuild.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sbuild

Build a Debian binary package in a clean `chroot` environment.
More information: <https://wiki.debian.org/sbuild>.

- Build the package in the current directory:

`sbuild`

- Build the given package:

`sbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Build for a certain distribution:

`sbuild --dist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>

- Build using custom dependencies (if a directory is passed, all files ending with `.deb` are used):

`sbuild --extra-package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Run a shell in case of build failure to further investigate:

`sbuild --build-failed-commands=%SBUILD_SHELL`

- Cross build for a certain architecture:

`sbuild --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>

- Build for the given native architecture:

`sbuild --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">architecture</span>
