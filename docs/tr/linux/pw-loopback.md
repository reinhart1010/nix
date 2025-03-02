---
layout: page
title: linux/pw-loopback (Türkçe)
description: "PipeWire'da geri döngü cihazları yaratma aracı."
content_hash: d1974649d56e522a9b00412af5efdd2dc71ba765
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-loopback.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pw-loopback.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

PipeWire'da geri döngü cihazları yaratma aracı.
Daha fazla bilgi için: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Varsayılan geri döngü davranışına sahip bir geri döngü cihazı yarat:

`pw-loopback`

- Hoparlörlere otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`'`

- Mikrofona otomatik olarak bağlanan bir geri döngü cihazı yarat:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Hiçbir şeye otomatik olarak bağlanmayan salak bir geri döngü cihazı yarat:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Hoparlörlere otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink audio.position=[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`'`

- Mikrofona otomatik olarak bağlanan ve taban-kaynak arasında sağ-sol kanalların yerini değiştiren bir geri döngü cihazı yarat:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source audio.position=[FL FR]</span>`'`
