---
layout: page
title: osx/xcodes (English)
description: "Download, install and manage multiple Xcode versions."
content_hash: 127583126cdbd33cb38a7c2629466e9917a1824b
last_modified_at: 2023-09-15
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcodes

Download, install and manage multiple Xcode versions.
See also: `xcodes runtimes`.
More information: <https://github.com/xcodesorg/xcodes>.

- List all installed Xcode versions:

`xcodes installed`

- List all available Xcode versions:

`xcodes list`

- Select an Xcode version by specifying a version number or a path:

`xcodes select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode-version|path/to/Xcode.app</span>

- Download and install a specific Xcode version:

`xcodes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode-version</span>

- Install the latest Xcode release and select it:

`xcodes install --latest --select`

- Download a specific Xcode version archive to a given directory without installing it:

`xcodes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode-version</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
