---
layout: page
title: linux/archlinux-java (Deutsch)
description: "Ein Helferskript, das Funktionen für Java-Umgebungen bereitstellt."
content_hash: e714e1edc52e63cee381135ed2330cc602a2242b
last_modified_at: 2024-01-08
related_topics:
  - title: English version
    url: /en/linux/archlinux-java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/archlinux-java.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># archlinux-java

Ein Helferskript, das Funktionen für Java-Umgebungen bereitstellt.
Weitere Informationen: <https://wiki.archlinux.org/title/Java#Switching_between_JVM>.

- Liste installierte Java-Umgebungen:

`archlinux-java status`

- Setze die default Java-Umgebung:

`archlinux-java set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_environment</span>

- Entferne die default Java-Umgebung:

`archlinux-java unset`

- Setze die default Java-Umgebung automatisch:

`archlinux-java fix`
