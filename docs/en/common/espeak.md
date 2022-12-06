---
layout: page
title: common/espeak (English)
description: "Uses text-to-speech to speak through the default sound device."
content_hash: e0f63a73c7e27413b87843c21d20ad358c200764
last_modified_at: 2022-12-06
related_topics:
  - title: italiano version
    url: /it/common/espeak.html
    icon: bi bi-globe
---
# espeak

Uses text-to-speech to speak through the default sound device.
More information: <http://espeak.sourceforge.net>.

- Speak a phrase aloud:

`espeak "I like to ride my bike."`

- Speak a file aloud:

`espeak -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Save output to a WAV audio file, rather than speaking it directly:

`espeak -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.wav</span>` "It's GNU plus Linux"`

- Use a different voice:

`espeak -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voice</span>
