---
layout: page
title: common/git-request-pull (Türkçe)
description: "Ana projeye yerelde yapılan değişiklikleri kendi ağacına çekmesini sormak için izin hazırla."
content_hash: 0bfcd598a4526eec26a2f09f516851643987a1d8
related_topics:
  - title: English version
    url: /en/common/git-request-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-request-pull.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git request-pull

Ana projeye yerelde yapılan değişiklikleri kendi ağacına çekmesini sormak için izin hazırla.
Daha fazla bilgi için: <https://git-scm.com/docs/git-request-pull>

- v1.1 sürümü ve belirtilen dal arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/proje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- `foo` dalındaki v0.1 sürümü ile yereldeki `bar` dalları arasındaki değişiklikleri özetleyen bir izin üret:

`git request-pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/proje</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo:bar</span>
