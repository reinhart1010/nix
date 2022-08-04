---
layout: page
title: osx/xcode-select (English)
description: "Switch between different versions of Xcode and the included developer tools."
content_hash: 2ddbc2ad1f49c75754365271e56138ad8ad1af6e
---
# xcode-select

Switch between different versions of Xcode and the included developer tools.
Also used to update the path to Xcode if it is moved after installation.
More information: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Install Xcode's command-line tools:

`xcode-select --install`

- Select a given path as the active developer directory:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Xcode.app/Contents/Developer</span>

- Select a given Xcode instance and use its developer directory as the active one:

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Xcode.app</span>

- Print the currently selected developer directory:

`xcode-select --print-path`

- Discard any user-specified developer directory so that it will be found via the default search mechanism:

`sudo xcode-select --reset`
