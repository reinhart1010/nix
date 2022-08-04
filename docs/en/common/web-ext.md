---
layout: page
title: common/web-ext (English)
description: "A command-line tool for managing web extension development."
content_hash: c85f56ac1cb4174506890b7c1b038f9afa565fa4
---
# web-ext

A command-line tool for managing web extension development.
More information: <https://github.com/mozilla/web-ext>.

- Run the web extension in the current directory in Firefox:

`web-ext run`

- Run a web extension from a specific directory in Firefox:

`web-ext run --source-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display verbose execution output:

`web-ext run --verbose`

- Run a web extension in Firefox Android:

`web-ext run --target firefox-android`

- Lint the manifest and source files for errors:

`web-ext lint`

- Build and package the extension:

`web-ext build`

- Display verbose build output:

`web-ext build --verbose`

- Sign a package for self-hosting:

`web-ext sign --api-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key</span>` --api-secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_secret</span>
