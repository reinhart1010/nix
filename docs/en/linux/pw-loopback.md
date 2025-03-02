---
layout: page
title: linux/pw-loopback (English)
description: "Create loopback devices in PipeWire."
content_hash: 8253d74b27c8c170c66410e5a5fe637bd2066a43
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/pw-loopback.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-loopback.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

Create loopback devices in PipeWire.
More information: <https://docs.pipewire.org/page_man_pw-loopback_1.html>.

- Create a loopback device with the default loopback behavior:

`pw-loopback`

- Create a loopback device that automatically connects to the speakers:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`'`

- Create a loopback device that automatically connects to the microphone:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Create a dummy loopback device that doesn't automatically connect to anything:

`pw-loopback -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[FL FR]</span>`' --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source</span>`'`

- Create a loopback device that automatically connects to the speakers and swaps the left and right channels between the sink and source:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Sink audio.position=[FL FR]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`'`

- Create a loopback device that automatically connects to the microphone and swaps the left and right channels between the sink and source:

`pw-loopback --capture-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">audio.position=[FR FL]</span>`' --playback-props='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">media.class=Audio/Source audio.position=[FL FR]</span>`'`
