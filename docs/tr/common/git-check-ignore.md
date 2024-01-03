---
layout: page
title: common/git-check-ignore (Türkçe)
description: "Git yoksayma / dışlama (\".gitignore\") dosyalarını analiz et."
content_hash: 4bf6bc55f2a6e313abee0349d8526c8a61640a6e
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Git yoksayma / dışlama (".gitignore") dosyalarını analiz et.
Daha fazla bilgi için: <https://git-scm.com/docs/git-check-ignore>.

- Bir dosya veya dizinin yoksayıldığı veya sayılmadığını kontrol et:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>

- Birden fazla dosya veya dizinin yoksayıldığı veya sayılmadığını kontrol et:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...</span>

- Her bir satıra tekabül edecek şekilde `stdin`'den yolisimleri kullan:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_sırası</span>

- İndeksi kontrol etme:

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...</span>

- Her yol için eşleşen desene dair detayları dahil et:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin1 örnek/dosya_veya_dizin2 ...</span>
