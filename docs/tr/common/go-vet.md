---
layout: page
title: common/go-vet (Türkçe)
description: "Go kaynak kodunu kontrol et ve şüpheli yapıları bildir (örneğin Go kaynak dosyalarını tiftik et)."
content_hash: 86665ec427d653bc983f4041fad1e12f921229f6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-vet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go vet

Go kaynak kodunu kontrol et ve şüpheli yapıları bildir (örneğin Go kaynak dosyalarını tiftik et).
Go vet komutu eğer sorun bulunduysa sıfır olmayan bir çıkış kodu yazdırır. Eğer herhangi bir sorun bulunmadıysa sıfır çıkış kodu yazdırılır.
Daha fazla bilgi için: <https://pkg.go.dev/cmd/vet>.

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
