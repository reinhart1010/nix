---
layout: page
title: common/docker-cp (日本語)
description: "ホスト、コンテナのファイルシステム間でファイルやディレクトリをコピーします。"
content_hash: 320918f768ea9ca1d30568776772fe67515d90bd
last_modified_at: 2023-01-24
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker cp

ホスト、コンテナのファイルシステム間でファイルやディレクトリをコピーします。
詳しくはこちら: <https://docs.docker.com/engine/reference/commandline/cp>.

- ホストからコンテナへファイルやディレクトリをコピーする:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のファイルパスもしくはディレクトリパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>

- コンテナからホストへファイルやディレクトリをコピーする:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のファイルパスもしくはディレクトリパス</span>

- ホストからコンテナへシンボリックリンクに従ってファイルやディレクトリをコピーする。(シンボリックリンクされたファイルを直接コピーし、シンボリックリンクそのものはコピーしない):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト上のシンボリックリンクパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ名</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コンテナ内のファイルパスもしくはディレクトリパス</span>
