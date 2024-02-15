---
layout: page
title: common/androguard (English)
description: "Reverse engineer Android applications. Written in Python."
content_hash: 32b1c4631257510070209bcdc73184b7121a1d0b
last_modified_at: 2024-02-15
related_topics:
  - title: français version
    url: /fr/common/androguard.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/androguard.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# androguard

Reverse engineer Android applications. Written in Python.
More information: <https://github.com/androguard/androguard>.

- Display Android app manifest:

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Display app metadata (version and app ID):

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Decompile Java code from an app:

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
