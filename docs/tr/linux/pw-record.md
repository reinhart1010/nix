---
layout: page
title: linux/pw-record (Türkçe)
description: "Pipewire aracılığıyla ses dosyalarını kaydedin."
content_hash: 7328a7708fc332a881b1ac7e0c188a7716c2141a
last_modified_at: 2023-10-24
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
---
# pw-record

Pipewire aracılığıyla ses dosyalarını kaydedin.
pw-cat --record için kısaltma.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Varsayılan hedefi kullanarak örnek bir ses kaydı al:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir ses seviyesinde örnek ses kaydı al:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir kayıt oranı kullanarak örnek ses kaydı al:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
