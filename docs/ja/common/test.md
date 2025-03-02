---
layout: page
title: common/test (日本語)
description: "条件を評価します。"
content_hash: d0259d4ef47c096ba48cb2e5582a936a3dc88ea7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/test.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/test.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/test.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# test

条件を評価します。
条件が真と評価された場合は 0 を、偽と評価された場合は 1 を返します。
もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>。

- 与えられた変数が与えられた文字列と等しいかどうかをテスト:

`test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$変数名</span>`" = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>`"`

- 与えられた変数が空であるかどうかをテスト:

`test -z "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$変数名</span>`"`

- ファイルが存在するかどうかをテスト:

`test -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルへのパス</span>`"`

- ディレクトリが存在しないかどうかをテスト:

`test ! -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリへのパス</span>`"`

- if-else 文:

`test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">条件</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "真"</span>` || `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "偽"</span>
