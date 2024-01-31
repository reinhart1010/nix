---
layout: page
title: common/opusenc (English)
description: "Convert WAV or FLAC audio to Opus."
content_hash: 94a0b0ccc99ddfa5ee25bf113273fc3ecb520ffd
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/common/opusenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opusenc

Convert WAV or FLAC audio to Opus.
More information: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- Convert WAV to Opus using default options:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.opus</span>

- Convert stereo audio at the highest quality level:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.opus</span>

- Convert 5.1 surround sound audio at the highest quality level:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.opus</span>

- Convert speech audio at the lowest quality level:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` --downmix-mono --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out.opus</span>
