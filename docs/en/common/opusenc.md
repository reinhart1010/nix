---
layout: page
title: common/opusenc (English)
description: "Convert WAV or FLAC audio to Opus."
content_hash: 8a158b065fef791c52f2ef1ec2bf10fb34524c1d
related_topics:
  - title: italiano version
    url: /it/common/opusenc.html
    icon: bi bi-globe
---
# opusenc

Convert WAV or FLAC audio to Opus.
More information: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- Convert WAV to Opus using default options:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.opus`

- Convert stereo audio at the highest quality level:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.opus`

- Convert 5.1 surround sound audio at the highest quality level:

`opusenc --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1536</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.opus`

- Convert speech audio at the lowest quality level:

`opusenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.wav</span>` --downmix-mono --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out</span>`.opus`
