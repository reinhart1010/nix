---
layout: page
title: common/docker-rmi (Türkçe)
description: "Bir veya daha fazla Docker imgesini sil."
content_hash: 77a295ef74b64e0b9e8e356dd6b2614c63f70ba9
last_modified_at: 2024-09-15
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Bir veya daha fazla Docker imgesini sil.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Yardım göster:

`docker rmi`

- Bir veya daha fazla imgeyi isimlerini belirterek sil:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge1 imge2 ...</span>

- Bir imgeyi zorla sil:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>

- Bir imgeyi etiketlenmemiş ana yollarını silmeden sil:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>
