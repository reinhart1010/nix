---
layout: page
title: osx/xcode-select (English)
description: "Switch between different versions of Xcode and the included developer tools."
content_hash: 1a03d60fb917c3c3c75aad3af74f4e23ceb73625
last_modified_at: 2023-02-20
related_topics:
  - title: Deutsch version
    url: /de/osx/xcode-select.html
    icon: bi bi-globe
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

`xcode-select --switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Xcode_file.app</span>

- Print the currently selected developer directory:

`xcode-select --print-path`

- Discard any user-specified developer directory so that it will be found via the default search mechanism:

`sudo xcode-select --reset`
