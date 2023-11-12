---
layout: page
title: linux/pulseaudio (English)
description: "The PulseAudio sound system daemon and manager."
content_hash: 817265ecf8d7804706a862244f31f3f46ace3df9
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/pulseaudio.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pulseaudio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pulseaudio

The PulseAudio sound system daemon and manager.
More information: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Check if PulseAudio is running (a non-zero exit code means it is not running):

`pulseaudio --check`

- Start the PulseAudio daemon in the background:

`pulseaudio --start`

- Kill the running PulseAudio daemon:

`pulseaudio --kill`

- List available modules:

`pulseaudio --dump-modules`

- Load a module into the currently running daemon with the specified arguments:

`pulseaudio --load="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>`"`
