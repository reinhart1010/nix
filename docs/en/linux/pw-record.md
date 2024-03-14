---
layout: page
title: linux/pw-record (English)
description: "Record audio files through PipeWire."
content_hash: 763843c1532f8fc0e25eeb475ebb75b8e6aab743
last_modified_at: 2024-03-14
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-record.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-record

Record audio files through PipeWire.
Shorthand for pw-cat --record.
More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Record a sample recording using the default target:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording at a different volume level:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Record a sample recording using a different sample rate:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
