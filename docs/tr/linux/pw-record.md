---
layout: page
title: linux/pw-record (Türkçe)
description: "Pipewire aracılığıyla ses dosyalarını kaydedin."
content_hash: 7328a7708fc332a881b1ac7e0c188a7716c2141a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pw-record.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pw-record.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-record

Pipewire aracılığıyla ses dosyalarını kaydedin.
pw-cat --record için kısaltma.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Varsayılan hedefi kullanarak örnek bir ses kaydı al:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir ses seviyesinde örnek ses kaydı al:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Farklı bir kayıt oranı kullanarak örnek ses kaydı al:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
