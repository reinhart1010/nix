---
layout: page
title: common/git-commit-graph (Indonesia)
description: "Tulis dan verifikasi file grafik komit Git."
content_hash: 0336c9ecf448a6e15dc5c1d52ebb182ab2ccc3d0
last_modified_at: 2024-05-04
related_topics:
  - title: English version
    url: /en/common/git-commit-graph.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-graph.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-graph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-graph

Tulis dan verifikasi file grafik komit Git.
Informasi lebih lanjut: <https://git-scm.com/docs/git-commit-graph>.

- Tulis file grafik komit untuk komit yang dikemas di dalam direktori `.git` pada lokal repositori:

`git commit-graph write`

- Tulis file grafik komit yang berisi semua komit yang dapat dijangkau:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Tulis file grafik komit yang berisi semua komit dalam file grafik komit saat ini beserta yang dapat dijangkau dari `HEAD`:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
