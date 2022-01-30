---
layout: page
title: common/gitsome (Türkçe)
description: "GitHub için gh komutuyla erişilebilen terminal tabanlı arayüz."
content_hash: 8ade75c6402cfb9bdd4d1f81b100f759457db29c
related_topics:
  - title: English version
    url: /en/common/gitsome.html
    icon: bi bi-globe
---
# gitsome

GitHub için gh komutuyla erişilebilen terminal tabanlı arayüz.
Ayrıca `git` komutları için menu tarzı otomatik tamamlanmış öneriler sunar.
Daha fazla bilgi: <https://github.com/donnemartin/gitsome>.

- Otomatik tamamlamayı ve Git ile gh komutları için etkileşimli yardımı etkinleştirmek için gitsome kabuğuna gir:

`gitsome`

- Mevcut hesap ile GitHub entegrasyonunu ayarla:

`gh configure`

- Mevcut hesap için bildirimleri (https://github.com/notifications adresinde görülebildiği gibi) sırala:

`gh notifications`

- Mevcut hesabın yıldızlanan depolarını belirtilen filtre ile sırala:

`gh starred "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python 3</span>`"`

- Belirtilen GitHub deposunun güncel etkileşimini görüntüle:

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-pages/tldr</span>

- Belirtilen GitHub kullanıcısının güncel etkileşimini varsayılan sayfacı ile (örneğin `less`) göster:

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torvalds</span>` -p`
