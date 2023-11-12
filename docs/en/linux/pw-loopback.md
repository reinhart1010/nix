---
layout: page
title: linux/pw-loopback (English)
description: "Tool for creating loopback devices in pipewire."
content_hash: 42caeb878d139bd6e36c86ba1c91acbb020fd2ea
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/pw-loopback.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-loopback

Tool for creating loopback devices in pipewire.
More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

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
