---
layout: page
title: common/kubectl (日本語)
description: "Kubernetes クラスタに対してコマンドを実行するためのコマンドラインインターフェイス。"
content_hash: b7a73db2e83bbc7f509a6a2dd59cfce1d98a6c2a
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/kubectl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kubectl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kubectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl

Kubernetes クラスタに対してコマンドを実行するためのコマンドラインインターフェイス。
`run` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
もっと詳しく: <https://kubernetes.io/docs/reference/kubectl/>。

- リソースに関する情報をより詳細に一覧表示する:

`kubectl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|service|deployment|ingress|...</span>` -o wide`

- 指定したポッドにラベル 'unhealthy' と値 'true' を付けて更新する:

`kubectl label pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ポッド名</span>` unhealthy=true`

- 異なるタイプのリソースを全て一覧表示する:

`kubectl get all`

- ノードまたはポッドのリソース (CPU/Memory/Storage) 使用量を表示する:

`kubectl top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod|node</span>

- マスターとクラスタサービスのアドレスを表示する:

`kubectl cluster-info`

- 特定のフィールドの説明を表示する:

`kubectl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pods.spec.containers</span>

- ポッドまたは指定したリソース内のコンテナのログを表示する:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ポッド名</span>

- 既存のポッドでコマンドを実行する:

`kubectl exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ポッド名</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls /</span>
