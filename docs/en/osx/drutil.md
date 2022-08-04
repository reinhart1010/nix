---
layout: page
title: osx/drutil (English)
description: "Interact with DVD burners."
content_hash: c1915f4b53cc77c92bf489920a6a76c46dbfea8c
related_topics:
  - title: 中文 version
    url: /zh/osx/drutil.html
    icon: bi bi-globe
---
# drutil

Interact with DVD burners.
More information: <https://ss64.com/osx/drutil.html>.

- Eject a disk from the drive:

`drutil eject`

- Burn a directory as an ISO9660 filesystem onto a DVD. Don't verify and eject when complete:

`drutil burn -noverify -eject -iso9660`
