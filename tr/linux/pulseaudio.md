---
layout: page
title: linux/pulseaudio (Türkçe)
description: "Ses sistem arkaplan uygulaması ve yöneticisi."
content_hash: 9e0eda462dbf1fc26741961260289ff1bc74a656
related_topics:
  - title: English version
    url: /en/linux/pulseaudio.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pulseaudio.html
    icon: bi bi-globe
---
# pulseaudio

Ses sistem arkaplan uygulaması ve yöneticisi.
Daha fazla bilgi: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Pulseaudio'nun çalışıp çalışmadığını kontrol et (sıfır olmayan çıktı, çalışmadığı anlamına gelir):

`pulseaudio --check`

- Pulseaudio'yu arkaplanda çalıştır:

`pulseaudio --start`

- Arkaplanda çalışan tüm pulseaudio uygulamalarını öldür:

`pulseaudio --kill`

- Müsait modülleri sırala:

`pulseaudio --dump-modules`

- Belirtilen argümanlarla bir modülü mevcut çalışan arkaplan uygulamasına yükle:

`pulseaudio --load="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modül_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argümanlar</span>`"`
