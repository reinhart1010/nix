---
layout: page
title: common/git-describe (Türkçe)
description: "Bir nesneye varolan referans üzerinden insanlar tarafından okunabilecek biçimde olan bir isim ver."
content_hash: bd45def8e0911561e2edc8b154b89659707ba593
related_topics:
  - title: English version
    url: /en/common/git-describe.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-describe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-describe.html
    icon: bi bi-globe
---
# git describe

Bir nesneye varolan referans üzerinden insanlar tarafından okunabilecek biçimde olan bir isim ver.
Daha fazla bilgi: <https://git-scm.com/docs/git-describe>.

- Mevcut commit için (en son eklenmiş etiket, ilave commit'lerin sayısı ve kısaltılmış commit değerini içeren) özel bir isim oluştur:

`git describe`

- Kısaltılmış commit değeri için 4 haneli bir isim oluştur:

`git describe --abbrev=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Etiket referans yolu ile bir isim oluştur:

`git describe --all`

- Bir Git etiketini açıkla:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.0.0</span>

- Belirtilen daldaki son commit için bir isim oluştur:

`git describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>
