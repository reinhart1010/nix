---
layout: page
title: common/git-credential (Türkçe)
description: "Kullanıcı kimlik bilgilerini kurtar ve sakla."
content_hash: c8222b828f10411bd6effa63cdb0379e89cb6600
related_topics:
  - title: English version
    url: /en/common/git-credential.html
    icon: bi bi-globe
---
# git credential

Kullanıcı kimlik bilgilerini kurtar ve sakla.
Daha fazla bilgi: <https://git-scm.com/docs/git-credential>.

- Kimlik bilgilerini, kullanıcı ismi ve parolayı konfigürasyon dosyası aracılığıyla kurtararak göster:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://örnek.com</span>`" | git credential fill`

- Kimlik bilgilerini sonra kullanma amacıyla saklamak için bütün yapılandırılmış kimlik yardımcılarına gönder:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://örnek.com</span>`" | git credential approve`

- Belirtilen kimlik bilgisini bütün yapılandırılmış kimlik yardımcılarından temizle:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://örnek.com</span>`" | git credential reject`
