---
layout: page
title: common/git-notes (Türkçe)
description: "Nesne notları ekle veya incele."
content_hash: 9346bfff3bb684417a8ba5826e28f2e8a0cc85ad
related_topics:
  - title: English version
    url: /en/common/git-notes.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-notes.html
    icon: bi bi-globe
---
# git notes

Nesne notları ekle veya incele.
Daha fazla bilgi: <https://git-scm.com/docs/git-notes>.

- Tüm notları ve bağlı oldukları nesneleri sırala:

`git notes list`

- Belirtilen nesneye bağlanan tüm notları sırala (varsayılan HEAD'dedir):

`git notes list [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>`]`

- Belirtilen nesneye bağlanan tüm notları göster (varsayılan HEAD'dedir):

`git notes show [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>`]`

- Belirtilen nesneye bir not ekle (varsayılan metin editörü açılır):

`git notes append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>

- Mesajı belirterek belirtilen nesneye bir not ekle:

`git notes append --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaj_yazısı</span>`"`

- Varolan bir notu düzenle (varsayılan HEAD'dedir):

`git notes edit [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>`]`

- Bir notu bir nesneden öbürüne kopyala:

`git notes copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kaynak_nesne</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_nesne</span>

- Belirtilen nesneye eklenen tüm notları sil:

`git notes remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>
