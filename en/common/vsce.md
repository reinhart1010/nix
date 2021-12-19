---
layout: page
title: common/vsce (English)
description: "Extension manager for Visual Studio Code."
content_hash: 9fc0a96165bfe3a667a93077c554cc9f74a1218d
---
# vsce

Extension manager for Visual Studio Code.
More information: <https://github.com/microsoft/vscode-vsce>.

- List all the extensions created by a publisher:

`vsce list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">publisher</span>

- Publish an extension as major, minor or patch version:

`vsce publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">major|minor|patch</span>

- Unpublish an extension:

`vsce unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_id</span>

- Package the current working directory as a `.vsix` file:

`vsce package`

- Show the metadata associated with an extension:

`vsce show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension_id</span>
