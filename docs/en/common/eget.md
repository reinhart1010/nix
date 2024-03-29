---
layout: page
title: common/eget (English)
description: "Easily install prebuilt binaries from GitHub."
content_hash: 2936b01a2c4a1c25c2c63f562ea4946c9ca12d1b
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# eget

Easily install prebuilt binaries from GitHub.
More information: <https://github.com/zyedidia/eget>.

- Download a prebuilt binary for the current system from a repository on GitHub:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>

- Download from a URL:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://go.dev/dl/go1.17.5.linux-amd64.tar.gz</span>

- Specify the location to place the downloaded files:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Specify a Git tag instead of using the latest version:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --tag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v2.0.10</span>

- Install the latest pre-release instead of the latest stable version:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --pre-release`

- Only download the asset, skipping extraction:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --download-only`

- Only download if there is a newer release then the currently downloaded version:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --upgrade-only`
