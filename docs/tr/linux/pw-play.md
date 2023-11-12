---
layout: page
title: linux/pw-play (Türkçe)
description: "pw-cat --playback komutu için kısayol aracı."
content_hash: 56deee24327467bd1b7b1c224c2a1d3409da4f9a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/pw-play.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-play

pw-cat --playback komutu için kısayol aracı.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir oynatma hedeflerini sırala:

`pw-play --list-targets`

- Varsayılan hedef üzerinden bir WAV sesi oynat:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- WAV sesini farklı bir ses yüksekliğinde oynat:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
