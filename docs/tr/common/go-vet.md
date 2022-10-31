---
layout: page
title: common/go-vet (Türkçe)
description: "Go kaynak kodunu kontrol et ve şüpheli yapıları bildir (örneğin Go kaynak dosyalarını tiftik et)."
content_hash: dd71050104d0af5eb6324ae6a1db1d9d112615b7
related_topics:
  - title: English version
    url: /en/common/go-vet.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go vet

Go kaynak kodunu kontrol et ve şüpheli yapıları bildir (örneğin Go kaynak dosyalarını tiftik et).
Go vet komutu eğer sorun bulunduysa sıfır olmayan bir çıkış kodu yazdırır. Eğer herhangi bir sorun bulunmadıysa sıfır çıkış kodu yazdırılır.
More information: <https://pkg.go.dev/cmd/vet>.

- Mevcut dizindeki Go paketini kontrol et:

`go vet`

- Belirtilen yoldaki Go paketini kontrol et:

`go vet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>

- Go vet ile çalıştırılabilecek erişilebilir kontrolleri sırala:

`go tool vet help`

- Belirtilen bir kontrol için detayları ve bayrakları göster:

`go tool vet help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kontrol_ismi</span>

- Kontrolün sorun bulmasına sebep olan satırları artı N sayıda ek içeriği görüntüle:

`go vet -c=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Analiz ve hataları JSON formatında çıkart:

`go vet -json`
