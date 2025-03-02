---
layout: page
title: common/docker-cp (日本語)
description: "ホスト、コンテナのファイルシステム間でファイルやディレクトリをコピーします。"
content_hash: cf63672ead06dea5877a01caf8aa25050ac00c08
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker-cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker cp

ホスト、コンテナのファイルシステム間でファイルやディレクトリをコピーします。
もっと詳しく: <https://docs.docker.com/reference/cli/docker/container/cp/>。

- ホストからコンテナへファイルやディレクトリをコピーする:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のファイルパスもしくはディレクトリパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>

- コンテナからホストへファイルやディレクトリをコピーする:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のファイルパスもしくはディレクトリパス</span>

- ホストからコンテナへシンボリックリンクに従ってファイルやディレクトリをコピーする。(シンボリックリンクされたファイルを直接コピーし、シンボリックリンクそのものはコピーしない):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のシンボリックリンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>
