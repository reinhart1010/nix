---
layout: page
title: common/aws-configure (日本語)
description: "AWS CLI の設定を管理します。"
content_hash: e470fec5ed33f5f88e64d4a0bb2d163f1df68a2b
related_topics:
  - title: English version
    url: /en/common/aws-configure.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-configure.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws configure

AWS CLI の設定を管理します。
詳しくはこちら: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- 対話形式で AWS CLI を設定する（新しい設定の作成、または既定の更新）:

`aws configure`

- 対話形式で AWS CLI の名前付きプロファイルを設定する（新規プロファイルの作成、または既存プロファイルの更新）:

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">プロファイル名</span>

- 特定の設定変数の値を表示する:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名前</span>

- 特定プロファイルの設定変数の値を表示する:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名前</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">プロファイル名</span>

- 特定の設定変数の値をセットする:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名前</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">値</span>

- 特定プロファイルの設定変数の値をセットする:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名前</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">値</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">プロファイル名</span>

- 設定エントリを一覧表示する:

`aws configure list`

- 特定プロファイル内の設定エントリを一覧表示する:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">プロファイル名</span>
