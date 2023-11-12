---
layout: page
title: linux/pasuspender (English)
description: "Temporarily suspends `pulseaudio` while another command is running to allow access to alsa."
content_hash: 73565294fc44fb69f208a635b29b93f34df9884f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pasuspender

Temporarily suspends `pulseaudio` while another command is running to allow access to alsa.
More information: <https://manned.org/pasuspender>.

- Suspend PulseAudio while running `jackd`:

`pasuspender -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jackd -d alsa --device hw:0</span>
