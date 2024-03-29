---
layout: page
title: common/git-checkout-index (Türkçe)
description: "Dosyaları indeksten çalışma ağacına kopyala."
content_hash: 97f847008655e1a539595fa6b545b6c9e64366d5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout-index.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout-index

Dosyaları indeksten çalışma ağacına kopyala.
Daha fazla bilgi için: <https://git-scm.com/docs/git-checkout-index>.

- Son commit'den beri silinen dosyaları geri döndür:

`git checkout-index --all`

- Son commit'den beri silinen veya değiştirilen dosyaları geri döndür:

`git checkout-index --all --force`

- Son commit'den beri değiştirilen dosyaları geri döndür ancak silinenleri yoksay:

`git checkout-index --all --force --no-create`

- Tüm ağacın bir kopyasını belirtilen dizinde dışa aktar (sondaki eğik çizgi önemli):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dışa/aktarılacak/dizin/</span>
