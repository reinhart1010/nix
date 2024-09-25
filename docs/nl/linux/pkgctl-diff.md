---
layout: page
title: linux/pkgctl-diff (Nederlands)
description: "Vergelijk pakketbestanden met behulp van verschillende modi."
content_hash: 4d87aef524f3a38541059a95a7c92e29f9555ddc
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pkgctl-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl diff

Vergelijk pakketbestanden met behulp van verschillende modi.
Bekijk ook: `pkgctl`.
Meer informatie: <https://manned.org/pkgctl-diff.1>.

- Vergelijk pakketbestanden in tar-inhoud [l]ijst verschillende modus (standaard):

`pkgctl diff --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in [d]iffoscope verschillende modus:

`pkgctl diff --diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in `.PKGINFO` verschillende modus:

`pkgctl diff --pkginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>

- Vergelijk pakketbestanden in `.BUILDINFO` verschillende modus:

`pkgctl diff --buildinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand|pkgname</span>
