---
layout: page
title: osx/softwareupdate (English)
description: "Update macOS App Store apps."
content_hash: 6afa1553b0ede3dee83f8e776f8add8b58cd6a82
last_modified_at: 2024-02-01
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/osx/softwareupdate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/softwareupdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# softwareupdate

Update macOS App Store apps.
More information: <https://keith.github.io/xcode-man-pages/softwareupdate.8.html>.

- List all available updates:

`softwareupdate --list`

- Download and install all updates:

`softwareupdate --install --all`

- Download and install all [r]ecommended updates:

`softwareupdate --install --recommended`

- Download and install a specific app:

`softwareupdate --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">update_name</span>
