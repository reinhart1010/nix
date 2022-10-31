---
layout: page
title: common/git-notes (Türkçe)
description: "Nesne notları ekle veya incele."
content_hash: 848ab4bb1b4adfa62e0ec8927d82d597eea5b032
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
Daha fazla bilgi için: <https://git-scm.com/docs/git-notes>.

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
