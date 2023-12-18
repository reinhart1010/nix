---
layout: page
title: linux/pw-cat (Türkçe)
description: "Pipewire üzerinden ses dosyalarını çalın ve kaydedin."
content_hash: fc7355a7279d3d2018a0e6795fc9af4fcc7f91c8
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/linux/pw-cat.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-cat

Pipewire üzerinden ses dosyalarını çalın ve kaydedin.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Varsayılan hedef üzerinden bir WAV dosyası oynat:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Örnek bir kaydı farklı bir ses seviyesinde kayda al:

`pw-cat --record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Örnek bir kaydı farklı bir örnek oran kullanarak kayda al:

`pw-cat --record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
