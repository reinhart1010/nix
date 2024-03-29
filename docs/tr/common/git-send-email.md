---
layout: page
title: common/git-send-email (Türkçe)
description: "Bir yama koleksiyonunu e-posta olarak gönder."
content_hash: 8b6502cad2b4c84c7e402acfb5bba579a7c6cf71
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# git send-email

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

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commits_sayı</span>` --compose`

- Gönderilecek her bir yama için e-posta mesajını görüntüle ve düzenle:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commits_sayı</span>` --annotate`
