---
layout: page
title: common/git-bugreport (Türkçe)
description: "Sşstem ve kullanıcıdan hata ayıklama bilgisi çeker ve olası bir Git hatasının rapor edilmesi için bu bilgiyi oluşturduğu bir metin dosyasına kaydeder."
content_hash: 970b0aa156fa2e617f80b052a7babe9353cd67e5
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bugreport.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bugreport.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bugreport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bugreport

Sşstem ve kullanıcıdan hata ayıklama bilgisi çeker ve olası bir Git hatasının rapor edilmesi için bu bilgiyi oluşturduğu bir metin dosyasına kaydeder.
Daha fazla bilgi için: <https://git-scm.com/docs/git-bugreport>.

- Mevcut dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport`

- Belirtilen dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output-directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>

- `strftime` formatında belirtilmiş bir dosya adı ekiyle yeni bir rapor dosyası oluştur:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--suffix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
