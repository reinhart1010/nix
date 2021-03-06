---
layout: page
title: common/git-commit-graph (Türkçe)
description: "Git commit-graph dosyalarını yaz ve doğrula."
content_hash: 0ca33fb252a91ae2c7539d27cdab480e9fac5b07
related_topics:
  - title: English version
    url: /en/common/git-commit-graph.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-graph.html
    icon: bi bi-globe
---
# git commit-graph

Git commit-graph dosyalarını yaz ve doğrula.
Daha fazla bilgi: <https://git-scm.com/docs/git-commit-graph>.

- Dizinin yerel `.git` dizinindeki paketlenmiş commit'ler için bir commit-grafik dosyası yaz:

`git commit-graph write`

- Erişilebilen tüm commitleri içeren bir commit-grafik dosyası yaz:

`git show-ref --hash | git commit-graph write --stdin-commits`

- `HEAD`'den erişilebilenlerin yanında mevcut commit-grafik dosyasındaki tüm commit'leri içeren bir commit-grafik dosyası oluştur:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
