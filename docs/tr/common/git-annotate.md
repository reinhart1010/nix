---
layout: page
title: common/git-annotate (Türkçe)
description: "Her satırdaki dosyanın yanında en son commit değeri ve yazarını göster."
content_hash: ea02e50b0719546a5e22f9ed51bee398feb13da2
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-annotate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-annotate.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git annotate

Her satırdaki dosyanın yanında en son commit değeri ve yazarını göster.
Ayrıca `git annotate` yerine tercih edilen `git blame` sayfasına bakılması önerilir.
`git annotate`, git dışındaki sürüm kontrol sistemlerine aşina olanlar için sağlanmıştır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-annotate>.

- Bir dosyayı, her satırında son commit değeri ve yazarı bulunacak şekilde göster:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Bir dosyayı, her satırında son commit değeri ve yazarının [e]-postası bulunacak şekilde göster:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
