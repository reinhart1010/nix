---
layout: page
title: common/glib-compile-resources (English)
description: "Compiles resource files (e.g. images) into a binary resource bundle."
content_hash: 2b1a4c67251e7237ff0eaea5c17e4a7958c4eaea
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# glib-compile-resources

Compiles resource files (e.g. images) into a binary resource bundle.
These may be linked into GTK applications using the GResource API.
More information: <https://manned.org/glib-compile-resources>.

- Compile resources referenced in `file.gresource.xml` to a .gresource binary:

`glib-compile-resources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.gresource.xml</span>

- Compile resources referenced in `file.gresource.xml` to a C source file:

`glib-compile-resources --generate-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.gresource.xml</span>

- Compile resources in `file.gresource.xml` to a chosen target file, with `.c`, `.h` or `.gresource` extension:

`glib-compile-resources --generate --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.gresource.xml</span>

- Print a list of resource files referenced in `file.gresource.xml`:

`glib-compile-resources --generate-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.gresource.xml</span>
