---
layout: page
title: common/espeak (English)
description: "Uses text-to-speech to speak through the default sound device."
content_hash: 622858ea6ded44389f25fd383e3a8192a01d6a61
last_modified_at: 2024-10-12
related_topics:
  - title: italiano version
    url: /it/common/espeak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# espeak

Uses text-to-speech to speak through the default sound device.
More information: <https://espeak.sourceforge.net>.

- Speak a phrase aloud:

`espeak "I like to ride my bike."`

- Speak a file aloud:

`espeak -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Save output to a WAV audio file, rather than speaking it directly:

`espeak -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.wav</span>` "It's GNU plus Linux"`

- Use a different voice:

`espeak -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voice</span>
