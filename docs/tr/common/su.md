---
layout: page
title: common/su (Türkçe)
description: "Kabuk ortamında başka bir kullanıcıya geçiş yapın."
content_hash: 465c0f1a8eb456912f22c6862e51d093c6a874de
related_topics:
  - title: English version
    url: /en/common/su.html
    icon: bi bi-globe
---
# su

Kabuk ortamında başka bir kullanıcıya geçiş yapın.
Daha fazla bilgi için: <https://manned.org/su>.

- Süper kullanıcıya geçin (kök şifresi gerektirir):

`su`

- Belirli bir kullanıcıya geçin (kullanıcının şifresini gerektirir):

`su `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>

- Belirli bir kullanıcıya geçin ve tam oturum açma kabuğunu simüle edin:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>

- Başka bir kullanıcı olarak bir komut çalıştırın:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>`"`
