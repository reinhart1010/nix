---
layout: page
title: common/aapt (English)
description: "Android Asset Packaging Tool."
content_hash: e2e28e34455acffb5eee57d96ca35958eb4f0fe9
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

Android Asset Packaging Tool.
Compile and package an Android app's resources.
More information: <https://elinux.org/Android_aapt>.

- List files contained in an APK archive:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Display an app's metadata (version, permissions, etc.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Create a new APK archive with files from the specified directory:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
