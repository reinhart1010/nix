---
layout: page
title: common/nginx (Türkçe)
description: "Nginx web sunucusu."
content_hash: 9c5c68cc9412b7b4c30f30af1170f34dbc14a1ac
related_topics:
  - title: Deutsch version
    url: /de/common/nginx.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nginx.html
    icon: bi bi-globe
---
# nginx

Nginx web sunucusu.
Daha fazla bilgi için: <https://nginx.org/en/>.

- Varsayılan konfigürasyon dosyasıyla sunucuyu başlat:

`nginx`

- Özel bir konfigürasyon dosyasıyla sunucuyu başlat:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigürasyon_dosyası</span>

- Konfigürasyon dosyasındaki her göreceli dosya yolu için bir ön ek ile sunucuyu başlat:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigürasyon_dosyası</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">göreceli/dosya/yolu/ön/eki</span>

- Çalışan sunucuyu etkilemeden konfigürasyon dosyasını test et:

`nginx -t`

- Aksamasız bir sinyal göndererek konfigürasyonu tekrar yükle:

`nginx -s reload`
