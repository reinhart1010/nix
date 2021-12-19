---
layout: page
title: linux/addpart (Deutsch)
description: "Informiert den Linux-Kernel über die Existenz der angegebenen Partition."
content_hash: dd506e3c79e75b3b4722fc0f4d3021f85a0d1e54
related_topics:
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addpart.html
    icon: bi bi-globe
---
# addpart

Informiert den Linux-Kernel über die Existenz der angegebenen Partition.
Dieser Befehl ist ein einfacher Wrapper um den `add partition` ioctl.
Mehr Informationen: <https://manned.org/addpart>.

- Informiere den Kernel über die Existenz der angegebenen Partition:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gerät</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">länge</span>
