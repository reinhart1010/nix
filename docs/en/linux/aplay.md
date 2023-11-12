---
layout: page
title: linux/aplay (English)
description: "Command-line sound player for ALSA soundcard driver."
content_hash: 9d8b0dfd4ae5715c1d5faaaf575f54fd4535131a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/aplay.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aplay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aplay

Command-line sound player for ALSA soundcard driver.
More information: <https://manned.org/aplay>.

- Play a specific file (sampling rate, bit depth, etc. will be automatically determined for the file format):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play the first 10 seconds of a specific file at 2500 Hz:

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play the raw file as a 22050 Hz, mono, 8-bit, Mu-Law `.au` file:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
