---
layout: page
title: common/git-send-email (Türkçe)
description: "Bir yama koleksiyonunu e-posta olarak gönder."
content_hash: be47e70a0816e666fa4a1005549e177c847cb261
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git send-email

Bir yama koleksiyonunu e-posta olarak gönder.
Yamalar dosya, dizin veya sürüm listesi olarak tanımlanabilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-send-email>.

- Mevcut dizindeki son commit'i gönder:

`git send-email -1`

- Belirtilen commit'i gönder:

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Mevcut dizindeki belirtilen sayı kadar (örneğin 10) commit'i gönder:

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Gönderilecek yama serisi için bir giriş e-posta mesajı gönder:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` --compose`

- Gönderilecek her bir yama için e-posta mesajını görüntüle ve düzenle:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` --annotate`
