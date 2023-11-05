---
layout: page
title: linux/pkgctl-diff (Nederlands)
description: "Vergelijk pakketbestanden met behulp van verschillende modi."
content_hash: 21bd7d33d26089d53ae4f2aa77a117e22934712b
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/pkgctl-diff.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pkgctl diff

Vergelijk pakketbestanden met behulp van verschillende modi.
Bekijk ook: `pkgctl`.
Meer informatie: <https://man.archlinux.org/man/pkgctl-diff.1>.

- Vergelijk pakketbestanden in tar-inhoud [l]ijst verschillende modus (standaard):

`pkgctl diff --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in [d]iffoscope verschillende modus:

`pkgctl diff --diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in `.PKGINFO` verschillende modus:

`pkgctl diff --pkginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in `.BUILDINFO` verschillende modus:

`pkgctl diff --buildinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>
