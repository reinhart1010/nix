---
layout: page
title: osx/softwareupdate (English)
description: "Update macOS App Store apps."
content_hash: 99fb897110e6e7eddcca1cfb136efae752dd921c
last_modified_at: 2024-01-31
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

- Download and install all recommended updates:

`softwareupdate --install --req`

- Download and install a specific app:

`softwareupdate --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">update_name</span>
