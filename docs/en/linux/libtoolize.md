---
layout: page
title: linux/libtoolize (English)
description: "A tool used in the autotools build system to prepare a package for the use of `libtool`."
content_hash: 581117df53920657eb70276fd530feb45c9df892
last_modified_at: 2023-11-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libtoolize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libtoolize

A tool used in the autotools build system to prepare a package for the use of `libtool`.
It performs various tasks, including generating necessary files and directories to integrate `libtool` seamlessly into a project.
More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtoolize>.

- Initialize a project for `libtool` by copying necessary files (avoiding symbolic links) and overwriting existing files if needed:

`libtoolize --copy --force`
