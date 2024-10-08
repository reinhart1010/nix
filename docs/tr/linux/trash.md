---
layout: page
title: linux/trash (Türkçe)
description: "Çöp / geri dönüşüm kutusunu yönetmek için bir komut satırı arayüzü."
content_hash: f6e2cf3c89c8112d5f452195ddf3695e132b0ae2
last_modified_at: 2024-09-12
related_topics:
  - title: English version
    url: /en/linux/trash.html
    icon: bi bi-globe
tldri18n_status: 2
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

`trash-empty 10`

- Çöpte 'foo' ismini taşıyan tüm dosyaları sil:

`trash-rm "foo"`

- Belirtilen konumdaki tüm dosyaları sil:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/detaylı/örnek/konum/dosya_veya_dizin</span>
