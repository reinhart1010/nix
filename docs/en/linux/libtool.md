---
layout: page
title: linux/libtool (English)
description: "A generic library support script that hides the complexity of using shared libraries behind a consistent, portable interface."
content_hash: 6ed1827ce548850c1541f597c5183a4440181c92
last_modified_at: 2023-11-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libtool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libtool

A generic library support script that hides the complexity of using shared libraries behind a consistent, portable interface.
More information: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compile a source file into a `libtool` object:

`libtool --mode=compile gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.lo</span>

- Create a library or an executable:

`libtool --mode=link gcc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.lo</span>

- Automatically set the library path so that another program can use uninstalled `libtool` generated programs or libraries:

`libtool --mode=execute gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program</span>

- Install a shared library:

`libtool --mode=install cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.la</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/installation_directory</span>

- Complete the installation of `libtool` libraries on the system:

`libtool --mode=finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/installation_dir</span>

- Delete installed libraries or executables:

`libtool --mode=uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/installed_library.la</span>

- Delete uninstalled libraries or executables:

`libtool --mode=clean rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/library.la</span>
