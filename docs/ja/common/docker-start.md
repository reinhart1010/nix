---
layout: page
title: common/docker-start (日本語)
description: "1つまたは複数の停止中コンテナを起動します。"
content_hash: 1642a28c5f753b4f7410ffeb3a762f66a34db3fa
last_modified_at: 2023-11-04
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-start.html
    icon: bi bi-globe
---
# docker start

1つまたは複数の停止中コンテナを起動します。
詳しくはこちら: <https://docs.docker.com/engine/reference/commandline/start/>.

- ヘルプを表示する:

`docker start`

- Dockerコンテナを起動する:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ</span>

- コンテナを起動し、`stdout`(標準出力) と `stderr`(標準エラー出力) をアタッチし、シグナルを転送する:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ</span>

- スペースで区切られた1つまたは複数の停止中コンテナを起動する:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ1 コンテナ2 ...</span>
