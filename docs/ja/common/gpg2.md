---
layout: page
title: common/gpg2 (日本語)
description: "GNU Privacy Guard 2。"
content_hash: c5d8400d1d394f883ac0ed75b9dd9e8d39959703
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/gpg2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gpg2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg2

GNU Privacy Guard 2。
GNU Privacy Guard 1 については `gpg` を参照してください。
もっと詳しく: <https://docs.releng.linuxfoundation.org/en/latest/gpg.html>。

- インポートされたキーを一覧表示する:

`gpg2 --list-keys`

- 指定したファイルを指定した受信者のために暗号化し、`.gpg`を付加した新しいファイルに出力を書き出す:

`gpg2 --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- 指定したファイルをパスフレーズのみで暗号化し、`.gpg`を付加した新しいファイルに出力を書き出す:

`gpg2 --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- 指定したファイルを復号し、結果を`stdout`に出力する:

`gpg2 --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt.gpg</span>

- 公開鍵をインポートする:

`gpg2 --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key.gpg</span>

- 指定したメールアドレスの公開鍵を`stdout`にエクスポートする:

`gpg2 --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- 指定したメールアドレスの秘密鍵を`stdout`にエクスポートする:

`gpg2 --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
