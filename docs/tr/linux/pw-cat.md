---
layout: page
title: linux/pw-cat (Türkçe)
description: "Ses dosyalarını çalıştırmak ve kayıt etmek için pipewire aracı."
content_hash: aa128f59f762d8604f155d08004087bbffb04848
related_topics:
  - title: English version
    url: /en/linux/pw-cat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-cat

Ses dosyalarını çalıştırmak ve kayıt etmek için pipewire aracı.
Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir oynatma hedeflerini sırala:

`pw-cat --playback --list-targets`

- Varsayılan hedef üzerinden bir WAV dosyası oynat:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Tüm erişilebilir kayıt hedeflerini sırala:

`pw-cat --record --list-targets`

- Örnek bir kaydı farklı bir ses seviyesinde kayda al:

`pw-cat --record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>

- Örnek bir kaydı farklı bir örnek oran kullanarak kayda al:

`pw-cat --record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dosya.wav</span>
