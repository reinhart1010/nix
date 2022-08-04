---
layout: page
title: common/docker-rmi (Türkçe)
description: "Bir veya daha fazla Docker imgesini sil."
content_hash: 16777d95feb50287d01c5782dfaff6f1fd18cdaf
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
---
# docker rmi

Bir veya daha fazla Docker imgesini sil.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Yardım göster:

`docker rmi`

- Bir veya daha fazla imgeyi isimlerini belirterek sil:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge1 imge2 ...</span>

- Bir imgeyi zorla sil:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>

- Bir imgeyi etiketlenmemiş ana yollarını silmeden sil:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>
