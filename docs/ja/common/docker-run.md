---
layout: page
title: common/docker-run (日本語)
description: "新しいDockerコンテナでコマンドを実行します。"
content_hash: b169fa52b9a629349aa683c87e0bc17b154e0940
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-run.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-run.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-run.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker run

新しいDockerコンテナでコマンドを実行します。
詳しくはこちら: <https://docs.docker.com/reference/cli/docker/container/run/>

- タグ付けイメージから作成した新しいコンテナでコマンドを実行する:

`docker run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ:タグ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- 新しいコンテナでコマンドをバックグランド実行し、そのIDを表示する:

`docker run --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- インタラクティブモードと疑似端末の割り当てを行って、使い捨てコンテナでコマンドを実行する:

`docker run --rm --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- 渡された環境変数を使って新しいコンテナでコマンドを実行する:

`docker run --env '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">環境変数名</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">値</span>`' --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">環境変数名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- バインドマウントを持つ新しいコンテナでコマンドを実行する:

`docker run --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホストへのパス</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- 公開ポートを持った新しいコンテナでコマンドを実行する:

`docker run --publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト側のポート</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ側のポート</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- イメージのエントリーポイントを上書きして新しいコンテナでコマンドを実行する:

`docker run --entrypoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>

- 新しいコンテナをネットワークに繋ぎ、そのコンテナでコマンドを実行する:

`docker run --network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ネットワーク</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>
