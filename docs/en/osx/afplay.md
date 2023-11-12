---
layout: page
title: osx/afplay (English)
description: "Command-line audio player."
content_hash: eea63e12f22a6b47f1f8bd920b3c11b2772143e6
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/afplay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afplay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afplay

Command-line audio player.
More information: <https://ss64.com/osx/afplay.html>.

- Play a sound file (waits until playback ends):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a sound file at 2x speed (playback rate):

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play a sound file at half speed:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Play the first N seconds of a sound file:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
