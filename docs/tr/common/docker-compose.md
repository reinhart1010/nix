---
layout: page
title: common/docker-compose (Türkçe)
description: "Çoklu konteynerli Docker uygulamalarını çalıştırın ve yönetin."
content_hash: 40a5b0de217727c631cac10f5b94b472eb3f1689
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Çoklu konteynerli Docker uygulamalarını çalıştırın ve yönetin.
Daha fazla bilgi için: <https://docs.docker.com/compose/reference/>.

- Tüm konteynerleri listele:

`docker compose ps`

- Mevcut dizinde bir `docker-compose.yml` dosyası çalıştırarak arkaplandaki tüm konteynerleri çalıştırın ve başlatın:

`docker compose up --detach`

- Tüm konteynerleri çalıştırın ve gerekiyorsa yeniden oluşturun:

`docker compose up --build`

- Tüm konteynerleri alternatif bir beste dosyasıyla başlatın:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proje Adı</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yoldan/dosyaya</span>` up`

- Çalışan tüm konteynerleri durdurun:

`docker compose stop`

- Tüm konteynerleri, ağları, imgeleri ve alanları durdurun ve silin:

`docker compose down --rmi all --volumes`

- Tüm konteynerler için logları takip edin:

`docker compose logs --follow`

- Belirtilmiş bir konteyner için logları takip edin:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>
