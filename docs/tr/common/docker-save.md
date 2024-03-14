---
layout: page
title: common/docker-save (Türkçe)
description: "Bir veya daha fazla Docker imgesini arşivlemek için dışa aktar."
content_hash: c98b03bb709982faea726239a60592232f843f1e
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-save.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-save.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-save.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker save

Bir veya daha fazla Docker imgesini arşivlemek için dışa aktar.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/save/>.

- Bir imgeyi, `stdout`'u tar arşivine yönlendirerek kaydet:

`docker save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>

- Bir imgeyi, bir tar arşivine kaydet:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket</span>

- Bir imgenin tüm etiketlerini kaydet:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge_ismi</span>

- Bir imgenin belirli etiketlerini kaydetmek için elle seç:

`docker save --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge_ismi:etiket1 imge_ismi:etiket2 ...</span>
