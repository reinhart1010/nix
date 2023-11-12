---
layout: page
title: linux/xfce4-screenshooter (Türkçe)
description: "XFCE4 ekran görüntüsü aracı."
content_hash: 1d160cbf8aa1c5947f715955820bb0f53e2dfec3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xfce4-screenshooter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xfce4-screenshooter

XFCE4 ekran görüntüsü aracı.
Daha fazla bilgi için: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- Ekran görüntüsü alma grafik arayüzünü başlat:

`xfce4-screenshooter`

- Tüm ekranın ekran görüntüsünü al ve nasıl devam edileceğini belirlemek adına grafik arayüzünü başlat:

`xfce4-screenshooter --fullscreen`

- Tüm ekranın ekran görüntüsünü al ve görüntüyü belirtilen dizine kaydet:

`xfce4-screenshooter --fullscreen --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>

- Ekran görüntüsünü çekmeden önce belli bir süre bekle:

`xfce4-screenshooter --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saniye_miktarı</span>

- Ekranın (fare ile seçilecek) belli bir bölümünün görüntüsünü al:

`xfce4-screenshooter --region`

- Üzerinde bulunulan pencerenin görüntüsünü al ve panoya kopyala:

`xfce4-screenshooter --window --clipboard`

- Üzerinde bulunulan pencerenin görüntüsünü qal ve seçilen bir program ile aç:

`xfce4-screenshooter --window --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gimp</span>
