---
layout: page
title: common/git-imerge (Türkçe)
description: "İki git dalı arasında aşamalı olarak birleştirme veya taban değiştirme işlemlerini uygula."
content_hash: bfb75b292a52892adf02c283b76acda2b522db23
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-imerge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-imerge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-imerge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-imerge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-imerge

İki git dalı arasında aşamalı olarak birleştirme veya taban değiştirme işlemlerini uygula.
Dallar arasındaki uyuşmazlıklar özel commitler ile bölüşülerek uyuşmazlıkları çözmek kolaylaştırılır.
Daha fazla bilgi için: <https://github.com/mhagger/git-imerge>.

- imerge bazlı taban değiştirme işlemini başlat (işlemden önce tabanı değiştirilmek istenen dalı kontrol et):

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yerine_geçilecek_dal</span>

- imerge bazlı birleştirme işlemini başlat (işlemden önce birleştirilmek istenen dalı kontrol et):

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">birleştirilecek_dal</span>

- Devam eden birleştirme ve taban değiştirme işlemlerinin ASCII diagramını göster:

`git imerge diagram`

- Uyuşmazlıkları çözdükten sonra imerge işlemine devam et (önce `git add` komutu ile uyuşmayan dosyaları ekle):

`git imerge continue --no-edit`

- Tüm uyuşmazlıklar çözüldükten sonra imerge işlemini sonlandır:

`git imerge finish`

- imerge işlemini sonlandır ve belirtilen eski bir dala geri dön:

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_dal</span>
