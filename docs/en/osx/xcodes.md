---
layout: page
title: osx/xcodes (English)
description: "Download, install and manage multiple Xcode versions."
content_hash: c007bf0cf6127475012bcd72b9d0258fc0c88455
last_modified_at: 2023-10-13
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/xcodes.html
    icon: bi bi-globe
---
# xcodes

Download, install and manage multiple Xcode versions.
See also: `xcodes runtimes`.
More information: <https://github.com/xcodesorg/xcodes>.

- List all installed Xcode versions:

`xcodes installed`

- List all available Xcode versions:

`xcodes list`

- Select an Xcode version by specifying a version number or a path:

`xcodes select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_version|path/to/Xcode.app</span>

- Download and install a specific Xcode version:

`xcodes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_version</span>

- Install the latest Xcode release and select it:

`xcodes install --latest --select`

- Download a specific Xcode version archive to a given directory without installing it:

`xcodes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_version</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
