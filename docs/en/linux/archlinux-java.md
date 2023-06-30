---
layout: page
title: linux/archlinux-java (English)
description: "Switch between installed Java environments."
content_hash: 1d63733109129cea7b26e4dd734339bceec57b4f
last_modified_at: 2023-06-30
related_topics:
  - title: Deutsch version
    url: /de/linux/archlinux-java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/archlinux-java.html
    icon: bi bi-globe
---
# archlinux-java

Switch between installed Java environments.
More information: <https://wiki.archlinux.org/title/Java#Switching_between_JVM>.

- List installed Java environments:

`archlinux-java status`

- Return the short name of the current default Java environment:

`archlinux-java get`

- Set the default Java environment:

`archlinux-java set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_environment</span>

- Unset the default Java environment:

`archlinux-java unset`

- Fix an invalid/broken default Java environment configuration:

`archlinux-java fix`
