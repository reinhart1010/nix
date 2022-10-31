---
layout: page
title: linux/pw-record (Türkçe)
description: "pw-cat --playback komutu için kısayol aracı."
content_hash: 4b57f6d732939b1af2f778f5049f60dd5e96ff8e
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-record

pw-cat --playback komutu için kısayol aracı.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir kayıt hedeflerini sırala:

`pw-record --list-targets`

- Varsayılan hedefi kullanarak örnek bir ses kaydı al:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir ses seviyesinde örnek ses kaydı al:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir kayıt oranı kullanarak örnek ses kaydı al:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
