---
layout: page
title: common/git-log (Türkçe)
description: "Commit geçmişini göster."
content_hash: 8de4b95f752a52e9cf1e3c5aefe389f9c7c0a15c
related_topics:
  - title: Deutsch version
    url: /de/common/git-log.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-log.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-log.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-log.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-log.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-log.html
    icon: bi bi-globe
---
# git log

Commit geçmişini göster.
Daha fazla bilgi: <https://git-scm.com/docs/git-log>.

- Mevcut olandan başlayarak mevcut çalışma ortamındaki git deposunun commit silsilesini ters kronolojik düzende göster:

`git log`

- Belirtilen dosya veya dizinin tarihini farklılıklarla beraber göster:

`git log -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/veya/dizin/konumu</span>

- Her bir commit'de hangi dosya(lar)ın değiştiğinin önizlemesini göster:

`git log --stat`

- Mevcut daldaki commit'lerin mesajlarının ilk satırını içeren bir çizelge göster:

`git log --oneline --graph`

- Bir depodaki commit, etiket ve dalların tamamını içeren bir çizelge göster:

`git log --oneline --decorate --all --graph`

- Mesajları yalnızca belirtilen ifadeleri içeren commit'leri göster (büyük-küçük harfe duyarsız):

`git log -i --grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aranan_ifade</span>

- Belirtilmiş yazardan gelen, belirtilen sayıda commit göster:

`git log -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sayı</span>` --author=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yazar</span>

- İki tarih arasında yapılmış commit'leri göster:

`git log --before=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tarih</span>` --after=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tarih</span>
