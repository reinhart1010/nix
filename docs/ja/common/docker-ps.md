---
layout: page
title: common/docker-ps (日本語)
description: "Dockerコンテナ一覧を表示します。"
content_hash: 515f4577c390889f7d3b4e3fe69d65dbbfeab4b1
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-ps.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

Dockerコンテナ一覧を表示します。
もっと詳しく: <https://docs.docker.com/reference/cli/docker/container/ls/>。

- 現在実行中のdockerコンテナ一覧を表示する:

`docker ps`

- 全てのdockerコンテナを表示する(実行中・停止中、両方のコンテナ):

`docker ps --all`

- 最後に作成したコンテナを表示する(全ての状態を含む):

`docker ps --latest`

- コンテナ名に指定の部分文字列を含むコンテナのみになるようにフィルタリングする:

`docker ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`"`

- 指定したイメージを原型(ancestor)として共有するコンテナのみになるようにフィルタリングする:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">タグ</span>`"`

- 終了コードでコンテナをフィルタリングする:

`docker ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コード</span>`"`

- 以下のいずれかのステータスでフィルタリングする(created, running, removing, paused, exited, dead):

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ステータス</span>`"`

- 特定のボリュームをマウントしている、または特定のパスにボリュームがマウントされているコンテナをフィルタリングする:

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
