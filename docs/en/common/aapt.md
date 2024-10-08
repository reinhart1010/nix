---
layout: page
title: common/aapt (English)
description: "Android Asset Packaging Tool: compile and package an Android app's resources."
content_hash: f827bb08dfc5771a4638a90c5cdb64da4c46e16d
last_modified_at: 2024-09-25
related_topics:
  - title: বাংলা version
    url: /bn/common/aapt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aapt

Android Asset Packaging Tool: compile and package an Android app's resources.
More information: <https://manned.org/aapt>.

- List files contained in an APK archive:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Display an app's metadata (version, permissions, etc.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>

- Create a new APK archive with files from the specified directory:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
