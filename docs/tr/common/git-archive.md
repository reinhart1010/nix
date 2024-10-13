---
layout: page
title: common/git-archive (Türkçe)
description: "İsimlendirilmiş bir ağaçtan dosyaların arşivini oluştur."
content_hash: f0726398427d3899cfe75e8b6a77f9a610c8acb7
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-archive.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-archive.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git archive

İsimlendirilmiş bir ağaçtan dosyaların arşivini oluştur.
Daha fazla bilgi için: <https://git-scm.com/docs/git-archive>.

- Mevcut HEAD'deki içerik ile bir tar arşivi oluştur ve içeriği standart çıktı biçiminde göster:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` HEAD`

- Mevcut HEAD'deki içerik ile bir zip arşivi oluştur ve içeriği standart çıktı biçiminde göster:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` --format zip HEAD`

- Yukarıda yazan madde ile aynı şeyi yap, ama zip arşivini belirtilen dosya olarak yaz:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/arşiv/dosyası.zip</span>` HEAD`

- Belirtilmiş bir daldaki son commitlerin içeriğinden bir tar arşivi oluştur:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/arşiv/dosyası.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilmiş bir dizindeki içeriklerden tar arşivi oluştur:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/arşiv/dosyası.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>

- Bir takım dosyayı belirtilmiş bir dizinin içinde arşivlemek için başlarına yol ekle:

`git archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/arşiv/dosyası.tar</span>` --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">başlarına/yol/eklenecek/dosyalar</span>`/ HEAD`
