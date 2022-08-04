---
layout: page
title: common/git-annotate (Türkçe)
description: "Her satırdaki dosyanın yanında en son commit değeri ve yazarını göster."
content_hash: 50e718ef34cbc255f0b2624423cd8a8d175a5a51
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
---
# git annotate

Her satırdaki dosyanın yanında en son commit değeri ve yazarını göster.
Ayrıca `git annotate` yerine tercih edilen `git blame` sayfasına bakılması önerilir.
`git annotate`, git dışındaki sürüm kontrol sistemlerine aşina olanlar için sağlanmıştır.
Daha fazla bilgi: <https://git-scm.com/docs/git-annotate>.

- Bir dosyayı, her satırında son commit değeri ve yazarı bulunacak şekilde göster:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Bir dosyayı, her satırında son commit değeri ve yazarının e-postası bulunacak şekilde göster:

`git annotate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
