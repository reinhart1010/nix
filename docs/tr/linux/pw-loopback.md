---
layout: page
title: linux/pw-loopback (Türkçe)
description: "PipeWire'da geri döngü cihazları yaratma aracı."
content_hash: e8fd03e0e3956bf1e174951d8e956da7ac1915af
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

PipeWire'da geri döngü cihazları yaratma aracı.
Daha fazla bilgi için: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

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
