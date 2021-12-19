---
layout: page
title: common/fc-cache (English)
description: "Scan font directories to build font cache files."
content_hash: e47f9310531dd885a40bce5e481fc69fa7908a6c
related_topics:
  - title: 中文 version
    url: /zh/common/fc-cache.html
    icon: bi bi-globe
---
# fc-cache

Scan font directories to build font cache files.
More information: <https://manned.org/fc-cache>.

- Generate font cache files:

`fc-cache`

- Force a rebuild of all font cache files, without checking if cache is up-to-date:

`fc-cache -f`

- Erase font cache files, then generate new font cache files:

`fc-cache -r`
