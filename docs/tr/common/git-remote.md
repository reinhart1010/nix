---
layout: page
title: common/git-remote (Türkçe)
description: "İzlenen depolar dizisini (uzak bağlantıları) yönet."
content_hash: 2cb38d56f66351174159556ab83d1bfb8edc4847
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-remote.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-remote.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-remote.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-remote.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-remote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-remote.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git remote

İzlenen depolar dizisini (uzak bağlantıları) yönet.
Daha fazla bilgi için: <https://git-scm.com/docs/git-remote>.

- Varolan uzak bağlantıların isim ve URL'leriyle bir listesini göster:

`git remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Uzak bağlantı ile ilgili bilgi göster:

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_ismi</span>

- Uzak bağlantı ekle:

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_url'si</span>

- Uzak bağlantının URL'sini değiştir:

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_url</span>

- Uzak bağlantıyı sil:

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_ismi</span>

- Uzak bağlantıyı yeniden adlandır:

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_isim</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_isim</span>
