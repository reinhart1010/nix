---
layout: page
title: linux/pulseaudio (Türkçe)
description: "Ses sistem arkaplan uygulaması ve yöneticisi."
content_hash: c83d62483feebcd6f0a38869d5ec0ae770f0cf93
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/linux/pulseaudio.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pulseaudio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulseaudio

Ses sistem arkaplan uygulaması ve yöneticisi.
Daha fazla bilgi için: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Pulseaudio'nun çalışıp çalışmadığını kontrol et (sıfır olmayan çıktı, çalışmadığı anlamına gelir):

`pulseaudio --check`

- Pulseaudio'yu arkaplanda çalıştır:

`pulseaudio --start`

- Arkaplanda çalışan tüm PulseAudio uygulamalarını öldür:

`pulseaudio --kill`

- Müsait modülleri sırala:

`pulseaudio --dump-modules`

- Belirtilen argümanlarla bir modülü mevcut çalışan arkaplan uygulamasına yükle:

`pulseaudio --load="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modül_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argümanlar</span>`"`
