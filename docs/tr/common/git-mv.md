---
layout: page
title: common/git-mv (Türkçe)
description: "Dosyaları taşı veya yeniden adlandır ve Git indeksini güncelle."
content_hash: d607c22562d3b76f44843a13efdde6a22b3a1e8c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-mv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git mv

Dosyaları taşı veya yeniden adlandır ve Git indeksini güncelle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-mv>.

- Depo içindeki dosyayı taşı ve bu hareketi sonraki commit'e ekle:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni/dosya/konumu</span>

- Dosyayı yeniden adlandır ve yeniden adlandırma hareketini sonraki commit'e ekle:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_dosya_ismi</span>

- Eğer varsa belirtilen hedefteki dosyanın üstüne yaz:

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef</span>
