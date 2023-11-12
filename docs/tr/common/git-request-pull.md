---
layout: page
title: common/git-request-pull (Türkçe)
description: "Ana projeye yerelde yapılan değişiklikleri kendi ağacına çekmesini sormak için izin hazırla."
content_hash: b976266063713d6a3a445bceed1b8148e20f540b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-request-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-request-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git request-pull

Ana projeye yerelde yapılan değişiklikleri kendi ağacına çekmesini sormak için izin hazırla.
Daha fazla bilgi için: <https://git-scm.com/docs/git-request-pull>.

- v1.1 sürümü ve belirtilen dal arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/proje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- `foo` dalındaki v0.1 sürümü ile yereldeki `bar` dalları arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/proje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo:bar</span>
