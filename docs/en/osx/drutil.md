---
layout: page
title: osx/drutil (English)
description: "Interact with DVD burners."
content_hash: 58315725c671c15b78de27f5cd513761b182b060
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/drutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/drutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# drutil

Interact with DVD burners.
More information: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- Eject a disk from the drive:

`drutil eject`

- Burn a directory as an ISO9660 filesystem onto a DVD. Don't verify and eject when complete:

`drutil burn -noverify -eject -iso9660`
