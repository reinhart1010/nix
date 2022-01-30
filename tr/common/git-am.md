---
layout: page
title: common/git-am (Türkçe)
description: "Yama dosyalarını uygula. E-posta ile commit alırken faydalıdır."
content_hash: 845d68c01f084e8625e342d2d4a6dde7319ab9d9
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
---
# git am

Yama dosyalarını uygula. E-posta ile commit alırken faydalıdır.
Ayrıca yama dosyalarının üretilmesine yarayan `git format-patch` sayfasına bakılması önerilir.
Daha fazla bilgi: <https://git-scm.com/docs/git-am>.

- Bir yama dosyasını uygula:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yama.patch</span>

- Yama dosyası uygulama işlemini durdur:

`git am --abort`

- Mümkün olacak kadar yama dosyasını uygula ve bu dosyaların uygulanamayan parçalarını bahsi geçen dosyaları reddetmek için kaydet:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/yama.patch</span>
