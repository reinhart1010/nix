---
layout: page
title: common/docker-compose (日本語)
description: "複数コンテナを持つDockerアプリケーションの実行と管理をします。"
content_hash: 651d6a5563d740bb024ebb0a111685c7f6a07b3b
last_modified_at: 2024-09-14
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
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker compose

複数コンテナを持つDockerアプリケーションの実行と管理をします。
詳しくはこちら: <https://docs.docker.com/reference/cli/docker/compose/>

- 実行中のコンテナ全てをリスト表示する:

`docker compose ps`

- カレントディレクトリにある `docker-compose.yml`ファイルを使用してバックグラウンドで全てのコンテナを作成・起動する:

`docker compose up --detach`

- 全てのコンテナを起動し、必要に応じて再ビルドする:

`docker compose up --build`

- 実行中の全てのコンテナを停止する:

`docker compose stop`

- 全てのコンテナ、ネットワーク、イメージ、ボリュームを停止して削除する:

`docker compose down --rmi all --volumes`

- 全てのコンテナのログをフォローする(表示し続ける):

`docker compose logs --follow`

- 特定コンテナのログをフォローする(表示し続ける):

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>
