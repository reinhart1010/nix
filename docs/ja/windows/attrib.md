---
layout: page
title: windows/attrib (日本語)
description: "ファイルまたはディレクトリの属性を表示または変更します。"
content_hash: 16831f332111f27e1a8b93e23cf45bea9e2593c6
related_topics:
  - title: English version
    url: /en/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
---
# attrib

ファイルまたはディレクトリの属性を表示または変更します。
詳しくはこちら: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>

- 現在のディレクトリ内のファイルの属性を表示します:

`attrib`

- 現在のディレクトリとサブディレクトリにあるファイルの属性を表示します:

`attrib /S`

- 現在のディレクトリとサブディレクトリ内のファイルとディレクトリの属性を表示します:

`attrib /S /D`

- ファイルに読み取り専用属性を追加します:

`attrib +R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名.txt</span>

- システムとファイルの非表示属性を削除します:

`attrib -S -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名.txt</span>

- 非表示の属性をディレクトリに追加します:

`attrib +H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>
