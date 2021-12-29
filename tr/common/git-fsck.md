---
layout: page
title: common/git-fsck (Türkçe)
description: "Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula:"
content_hash: fcb34d980c27f8122cc36e30190d5a70699612d8
related_topics:
  - title: English version
    url: /en/common/git-fsck.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git fsck

Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula:
Düzenleme yapılması tavsiye edilmez. Geçersiz düğümleri çözmek için `git gc` komutu önerilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-fsck>.

- Mevcut depoyu kontrol et:

`git fsck`

- Bulunan tüm etiketleri sırala:

`git fsck --tags`

- Bulunan tüm kök düğümleri sırala:

`git fsck --root`
