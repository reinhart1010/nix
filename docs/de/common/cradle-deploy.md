---
layout: page
title: common/cradle-deploy (Deutsch)
description: "Verwalte Cradle Implementierungen."
content_hash: e621556f42adb69b758ac738bad0bcafb776106c
related_topics:
  - title: English version
    url: /en/common/cradle-deploy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-deploy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-deploy.html
    icon: bi bi-globe
---
# cradle deploy

Verwalte Cradle Implementierungen.
Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#deploy>.

- Implementiere Cradle auf einem Server:

`cradle deploy production`

- Implementiere statische Anlagen zu Amazon S3:

`cradle deploy s3`

- Implementiere statische Anlagen inklusive den Yarn Komponenten:

`cradle deploy s3 --include-yarn`

- Implementiere statische Anlagen inklusive dem "upload" Verzeichnis:

`cradle deploy s3 --include-upload`
