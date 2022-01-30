---
layout: page
title: common/git-checkout-index (Türkçe)
description: "Dosyaları indeksten çalışma ağacına kopyala."
content_hash: 28ce186053cb5229a430beacb3508a0e53fd77b2
related_topics:
  - title: English version
    url: /en/common/git-checkout-index.html
    icon: bi bi-globe
---
# git checkout-index

Dosyaları indeksten çalışma ağacına kopyala.
Daha fazla bilgi: <https://git-scm.com/docs/git-checkout-index>.

- Son commit'den beri silinen dosyaları geri döndür:

`git checkout-index --all`

- Son commit'den beri silinen veya değiştirilen dosyaları geri döndür:

`git checkout-index --all --force`

- Son commit'den beri değiştirilen dosyaları geri döndür ancak silinenleri yoksay:

`git checkout-index --all --force --no-create`

- Tüm ağacın bir kopyasını belirtilen dizinde dışa aktar (sondaki eğik çizgi önemli):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dışa/aktarılacak/dizin/</span>
