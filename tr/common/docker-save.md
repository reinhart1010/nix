---
layout: page
title: common/docker-save (Türkçe)
description: "Bir veya daha fazla docker imgesini arşivlemek için dışa aktar."
content_hash: 980bd6d700181e6416d5cca026f03c5a39eb40dc
related_topics:
  - title: Deutsch version
    url: /de/common/docker-save.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-save.html
    icon: bi bi-globe
---
# docker save

Bir veya daha fazla docker imgesini arşivlemek için dışa aktar.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/save/>.

- Bir imgeyi, stdout'u tar arşivine yönlendirerek kaydet:

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket</span>` > {örnek/dosya.tar</span>

- Bir imgeyi, bir tar arşivine kaydet:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket</span>

- Bir imgenin tüm etiketlerini kaydet:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge_ismi</span>

- Bir imgenin belirli etiketlerini kaydetmek için elle seç:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge_ismi:etiket1 imge_ismi:etiket2 ...</span>
