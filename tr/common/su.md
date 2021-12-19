---
layout: page
title: common/su (Türkçe)
description: "Kabuk ortamında başka bir kullanıcıya geçiş yapın."
content_hash: 200471a9992bbbb7994ba4b3e31f67c41b556203
related_topics:
  - title: English version
    url: /en/common/su.html
    icon: bi bi-globe
---
# su

Kabuk ortamında başka bir kullanıcıya geçiş yapın.

- Süper kullanıcıya geçin (kök şifresi gerektirir):

`su`

- Belirli bir kullanıcıya geçin (kullanıcının şifresini gerektirir):

`su `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>

- Belirli bir kullanıcıya geçin ve tam oturum açma kabuğunu simüle edin:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>

- Başka bir kullanıcı olarak bir komut çalıştırın:

`su - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kullanıcıadı</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>`"`
