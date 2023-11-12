---
layout: page
title: osx/drutil (English)
description: "Interact with DVD burners."
content_hash: c1915f4b53cc77c92bf489920a6a76c46dbfea8c
last_modified_at: 2023-11-12
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
More information: <https://ss64.com/osx/drutil.html>.

- Eject a disk from the drive:

`drutil eject`

- Burn a directory as an ISO9660 filesystem onto a DVD. Don't verify and eject when complete:

`drutil burn -noverify -eject -iso9660`
