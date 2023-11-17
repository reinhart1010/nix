---
layout: page
title: common/androguard (Nederlands)
description: "Reverse engineering tool voor Android applicaties, geschreven in Python."
content_hash: cc7627167172ac1542af99b97d2e7ef7283b1a86
last_modified_at: 2023-11-17
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/androguard.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># androguard

Reverse engineering tool voor Android applicaties, geschreven in Python.
Meer informatie: <https://github.com/androguard/androguard>.

- Toon Android app manifest:

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Toon app metadata (versie en app ID):

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>

- Decompileer Java code van een applicatie:

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/app.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
