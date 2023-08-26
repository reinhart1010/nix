---
layout: page
title: windows/pipwin (English)
description: "A tool to install unofficial Python package binaries on Windows."
content_hash: cbfd9a61b4b9148feaad2a11e2079079da6f2e33
last_modified_at: 2023-08-26
---
# pipwin

A tool to install unofficial Python package binaries on Windows.
More information: <https://github.com/lepisma/pipwin>.

- List all available packages for download:

`pipwin list`

- Search packages:

`pipwin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partial_name|name</span>

- Install a package:

`pipwin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Uninstall a package:

`pipwin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Download a package to a specific directory:

`pipwin download --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Install packages according to `requirements.txt`:

`pipwin install --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\requirements.txt</span>
