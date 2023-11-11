---
layout: page
title: common/androguard (Nederlands)
description: "Reverse engineering tool voor Android applicaties, geschreven in Python."
content_hash: cc7627167172ac1542af99b97d2e7ef7283b1a86
last_modified_at: 2023-11-11
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># androguard

Reverse engineering tool voor Android applicaties, geschreven in Python.
Meer informatie: <https://github.com/androguard/androguard>.

- Toon Android app manifest:

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Toon app metadata (versie en app ID):

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Decompileer Java code van een applicatie:

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
