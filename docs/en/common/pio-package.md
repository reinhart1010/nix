---
layout: page
title: common/pio-package (English)
description: "Manage packages in the registry."
content_hash: 0a1fce7ee30a148a168c805159b1edd55362059c
---
# pio package

Manage packages in the registry.
Packages can only be removed within 72 hours (3 days) from the date that they are published.
More information: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Create a package tarball from the current directory:

`pio package pack --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.tar.gz</span>

- Create and publish a package tarball from the current directory:

`pio package publish`

- Publish the current directory and restrict public access to it:

`pio package publish --private`

- Publish a package:

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.tar.gz</span>

- Publish a package with a custom release date (UTC):

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.tar.gz</span>` --released-at "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-04-08 21:15:38</span>`"`

- Remove all versions of a published package from the registry:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Remove a specific version of a published package from the registry:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Undo the removal, putting all versions or a specific version of the package back into the registry:

`pio package unpublish --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
