---
layout: page
title: common/docker (русский)
description: "Управление контейнерами и образами Docker."
content_hash: 54abaefb564cc29ec8a52b4bd525ed6715beda81
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker

Управление контейнерами и образами Docker.
Некоторые подкоманды, такие как `run`, имеют собственную документацию по использованию.
Больше информации: <https://docs.docker.com/reference/cli/docker/>.

- Список всех контейнеров Docker (запущенных и остановленных):

`docker ps --all`

- Запустить контейнера из образа с заданным именем:

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_контейнера</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_образа</span>

- Запустить или остановить существующий контейнер:

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_контейнера</span>

- Загрузить образ из репозитория Docker:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_образа</span>

- Показать список уже загруженных образов:

`docker images`

- Запустить интерактивный ([i]) телетайп ([t]) с командной оболочкой Bourne shell (sh) внутри запущенного контейнера:

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_контейнера</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Удалить остановленный контейнер:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_контейнера</span>

- Получить и следить за логами контейнера:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_контейнера</span>
