---
layout: page
title: common/espeak (English)
description: "Uses text-to-speech to speak through the default sound device."
content_hash: e4db920425a54e425d01e327d874339d6a665668
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

`espeak -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Save output to a WAV audio file, rather than speaking it directly:

`espeak -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.wav</span>` "It's GNU plus Linux"`

- Use a different voice:

`espeak -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voice</span>
