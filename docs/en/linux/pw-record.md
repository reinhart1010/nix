---
layout: page
title: linux/pw-record (English)
description: "Record audio files through pipewire."
content_hash: 88ea4b9454c46fc0299eb4567d903c25e6d2c454
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-record

Record audio files through pipewire.
Shorthand for pw-cat --record.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Record a sample recording using the default target:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording at a different volume level:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording using a different sample rate:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
