---
layout: page
title: common/git-bugreport (Türkçe)
description: "Sşstem ve kullanıcıdan hata ayıklama bilgisi çeker ve olası bir Git hatasının rapor edilmesi için bu bilgiyi oluşturduğu bir metin dosyasına kaydeder."
content_hash: 1e25ed1bfc0c13394111a8f1fbfb4824105365d8
related_topics:
  - title: English version
    url: /en/common/git-bugreport.html
    icon: bi bi-globe
---
# git bugreport

Sşstem ve kullanıcıdan hata ayıklama bilgisi çeker ve olası bir Git hatasının rapor edilmesi için bu bilgiyi oluşturduğu bir metin dosyasına kaydeder.
Daha fazla bilgi için: <https://git-scm.com/docs/git-bugreport>.

- Mevcut dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport`

- Belirtilen dizinde yeni bir hata rapor dosyası oluştur:

`git bugreport --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>

- `strftime` formatında belirtilmiş bir dosya adı ekiyle yeni bir rapor dosyası oluştur:

`git bugreport --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
