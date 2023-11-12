---
layout: page
title: common/ant (Deutsch)
description: "Apache Ant."
content_hash: 59f888e9e60cc364c3204ef964697b94a6df5b66
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant.
Tool zum Bauen und Verwalten von Projekten, die auf Java basieren.
Weitere Informationen: <https://ant.apache.org>.

- Baue ein Projekt mit der Standard build-Datei `build.xml`:

`ant`

- Baue ein Projekt mit einer anderen build-Datei als `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- Zeige Informationen über mögliche targets für dieses Projekt:

`ant -p`

- Zeige Debugging-Informationen:

`ant -d`

- Führe alle targets aus, die nicht von fehlgeschlagenen targets abhängen:

`ant -k`
