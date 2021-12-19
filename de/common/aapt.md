---
layout: page
title: common/aapt (Deutsch)
description: "Android Asset Packaging Tool."
content_hash: 89905f75545cfff770e09da5979702ccbb3418f6
related_topics:
  - title: English version
    url: /en/common/aapt.html
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
Kompiliere und verpacke die Resourcen einer Android App.
Weitere Informationen: <https://elinux.org/Android_aapt>.

- Liste alle Dateien eines APK Archivs auf:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/app.apk</span>

- Zeige die Metadaten einer App an (Version, Berechtigungen, usw.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/app.apk</span>

- Erstelle ein neues APK Archiv mit den Dateien eines bestimmten Verzeichnisses:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/app.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>
