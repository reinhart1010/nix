---
layout: page
title: linux/pw-cat (English)
description: "Play and record audio files through PipeWire."
content_hash: 47ba4bc27a61085e1e6d1c692687a739f6e22a21
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/pw-cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-cat

Play and record audio files through PipeWire.
More information: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Play a WAV file over the default target:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Play a WAV file with a specified resampler quality (4 by default):

`pw-cat --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..15</span>` --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording at a volume level of 125%:

`pw-cat --record --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording using a different sample rate:

`pw-cat --record --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
