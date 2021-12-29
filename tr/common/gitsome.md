---
layout: page
title: common/gitsome (Türkçe)
description: "GitHub için gh komutuyla erişilebilen terminal tabanlı arayüz."
content_hash: 8c4015fbea4c046957be6f8d5c6a473fcd1eed64
related_topics:
  - title: English version
    url: /en/common/gitsome.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gitsome

GitHub için gh komutuyla erişilebilen terminal tabanlı arayüz.
Ayrıca `git` komutları için menu tarzı otomatik tamamlanmış öneriler sunar.
Daha fazla bilgi için: <https://github.com/donnemartin/gitsome>.

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
