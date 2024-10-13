---
layout: page
title: common/git-branch (Türkçe)
description: "Dallar ile çalışmak için kullanılan ana Git komutu."
content_hash: ce3c22c1fab6d98af4568e5dc49c523b4e185f0f
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-branch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-branch.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-branch.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git branch

Dallar ile çalışmak için kullanılan ana Git komutu.
Daha fazla bilgi için: <https://git-scm.com/docs/git-branch>.

- Tüm dalları (yerel ve uzak bağlantıda olan) göster:

`git branch --all`

- Mevcut dalın ismini göster:

`git branch --show-current`

- Mevcut commit'e dayanarak yeni bir dal oluştur:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilen commit'e dayanarak yeni bir dal oluştur:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bir dalı yeniden adlandır:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--move</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dal_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dal_ismi</span>

- Yerel bir dalı sil:

`git branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Uzaktaki bir dalı sil:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_dal_ismi</span>
