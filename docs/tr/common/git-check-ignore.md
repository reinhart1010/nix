---
layout: page
title: common/git-check-ignore (Türkçe)
description: "Git yoksayma / dışlama (\".gitignore\") dosyalarını analiz et."
content_hash: e6b10b1ad3a05fd69bc18b231f36db61038749ea
last_modified_at: 2023-11-12
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

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>

- Her bir satıra tekabül edecek şekilde `stdin`'den yolisimleri kullan:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_sırası</span>

- İndeksi kontrol etme:

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>

- Her yol için eşleşen desene dair detayları dahil et:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>
