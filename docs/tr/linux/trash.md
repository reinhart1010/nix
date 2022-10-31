---
layout: page
title: linux/trash (Türkçe)
description: "Çöp / geri dönüşüm kutusunu yönetmek için bir komut satırı arayüzü."
content_hash: cfa930a1fd4292a86f61737f5a655efc7569e3d2
related_topics:
  - title: English version
    url: /en/linux/trash.html
    icon: bi bi-globe
---
# trash

Çöp / geri dönüşüm kutusunu yönetmek için bir komut satırı arayüzü.
Daha fazla bilgi için: <https://github.com/andreafrancia/trash-cli>.

- Bir dosyayı sil (çöpe gönder):

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Çöpteki dosyaları göster:

`trash-list`

- Çöpteki dosyaları geri getir:

`trash-restore`

- Çöpü boşalt:

`trash-empty`

- Çöpü 10 gün öncesinden daha yeni atılan dosyalar hariç boşalt:

`trash-empty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Çöptw 'foo' ismini taşıyan tüm dosyaları sil:

`trash-rm foo`

- Belirtilen konumdaki tüm dosyaları sil:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/detaylı/örnek/konum/dosya_veya_dizin</span>
