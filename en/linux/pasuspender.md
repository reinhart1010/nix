---
layout: page
title: linux/pasuspender (English)
description: "Temporarily suspends `pulseaudio` while another command is running to allow access to alsa."
content_hash: 90879d1f2dfbc6ab2a50f30767ca8fe9bb952878
---
# pasuspender

Temporarily suspends `pulseaudio` while another command is running to allow access to alsa.

- Suspend PulseAudio while running `jackd`:

`pasuspender -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jackd -d alsa --device hw:0</span>
