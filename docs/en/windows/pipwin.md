---
layout: page
title: windows/pipwin (English)
description: "A tool to install unofficial Python package binaries on Windows."
content_hash: 392789056b8e352c34442b990c1aaf7431c650a0
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pipwin

A tool to install unofficial Python package binaries on Windows.
More information: <https://github.com/lepisma/pipwin>.

- List all available packages for download:

`pipwin list`

- Search packages:

`pipwin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partial_name|name</span>

- Install a package:

`pipwin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Uninstall a package:

`pipwin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Download a package to a specific directory:

`pipwin download --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Install packages according to `requirements.txt`:

`pipwin install --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/requirements.txt</span>
