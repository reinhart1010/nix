---
layout: page
title: common/git-commit-tree (Türkçe)
description: "Commit cisimleri oluşturmaya yarayan düşük seviyeli araç."
content_hash: 9c4d228365d85c3251de57e1e2aa61f0f7910a98
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-commit-tree.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-tree

Commit cisimleri oluşturmaya yarayan düşük seviyeli araç.
Ayrıca `git commit` sayfasına bakılması önerilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-commit-tree>.

- Belirtilen mesaj ile bir commit cismi oluştur:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağaç</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>`"`

- Bir dosyadan mesaj okuyan bir commit cismi oluştur (`stdin` için `-` ekini kullan):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağaç</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- GPG anahtarıyla imzalanmış bir commit cismi oluştur:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağaç</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>`" --gpg-sign`

- Belirtilen ana commit cismi ile bir commit cismi oluştur:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağaç</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mesaj</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ana_commit_sha</span>
