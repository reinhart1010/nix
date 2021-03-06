---
layout: page
title: common/git-branch (Türkçe)
description: "Dallar ile çalışmak için kullanılan ana Git komutu."
content_hash: e4c67382ee182b9b7f2750376f5ae3bf29de5d97
related_topics:
  - title: Deutsch version
    url: /de/common/git-branch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-branch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
---
# git branch

Dallar ile çalışmak için kullanılan ana Git komutu.
Daha fazla bilgi: <https://git-scm.com/docs/git-branch>.

- Yerel dalları göster. Mevctu dal `*` ile vurgulanır:

`git branch`

- Tüm dalları (yerel ve uzak bağlantıda olan) göster:

`git branch -a`

- Mevcut dalın ismini göster:

`git branch --show-current`

- Mevcut commit'e dayanarak yeni bir dal oluştur:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilen commit'e dayanarak yeni bir dal oluştur:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bir dalı yeniden adlandır:

`git branch -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dal_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dal_ismi</span>

- Yerel bir dalı sil:

`git branch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Uzaktaki bir dalı sil:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_dal_ismi</span>
