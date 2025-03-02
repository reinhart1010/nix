---
layout: page
title: common/podman (日本語)
description: "ポッド、コンテナ、イメージのシンプルな管理ツールです。"
content_hash: 6e7fe441a5875c7a8937685a938a8b6668fbd4eb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/podman.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/podman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/podman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman

ポッド、コンテナ、イメージのシンプルな管理ツールです。
PodmanはDocker-CLIと互換性のあるコマンドラインを提供します。簡潔に言うと: `alias docker=podman`。
もっと詳しく: <https://github.com/containers/podman/blob/main/commands-demo.md>。

- 全てのコンテナ(実行中と停止中の両方)を一覧表示する:

`podman ps --all`

- イメージから任意の名前でコンテナを作成する:

`podman run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>

- 既存のコンテナを起動または停止する:

`podman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>

- レジストリからイメージをプルする (デフォルトは Docker Hub):

`podman pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">イメージ</span>

- 既にダウンロードされているイメージのリストを表示する:

`podman images`

- 既に起動しているコンテナ内でシェルを開く:

`podman exec --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- 停止しているコンテナを削除する:

`podman rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>

- 1つまたは複数のコンテナのログを表示し、ログ出力を追跡する:

`podman logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナid</span>
