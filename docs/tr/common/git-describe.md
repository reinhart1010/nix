---
layout: page
title: common/git-describe (Türkçe)
description: "Bir nesneye varolan referans üzerinden insanlar tarafından okunabilecek biçimde olan bir isim ver."
content_hash: 4827f378d7b8c21046311dbed6ab6ee289631ae5
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# git describe

Bir nesneye varolan referans üzerinden insanlar tarafından okunabilecek biçimde olan bir isim ver.
Daha fazla bilgi için: <https://git-scm.com/docs/git-describe>.

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
