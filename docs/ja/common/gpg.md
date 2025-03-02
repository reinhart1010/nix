---
layout: page
title: common/gpg (日本語)
description: "GNU Privacy Guard。"
content_hash: d4fa864cbb5584d56b9ac0ecaaa19ba14f001ddb
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/gpg.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg

GNU Privacy Guard。
GNU Privacy Guard 2 については `gpg2` を参照してください。殆どのオペレーティングシステムは `gpg` を `gpg2` にシンボリックリンクしています。
もっと詳しく: <https://gnupg.org>。

- GPGの公開鍵と秘密鍵を対話的に作成する:

`gpg --full-generate-key`

- 暗号化せずに `doc.txt` に署名する (出力を `doc.txt.asc` に書き出す):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- alice@example.com と bob@example.com の `doc.txt` を暗号化して署名する (`doc.txt.gpg` に出力):

`gpg --encrypt --sign --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bob@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- パスフレーズのみで `doc.txt` を暗号化する (`doc.txt.gpg` に出力):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- `doc.txt.gpg` を復号化する (`stdout` に出力):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- 公開鍵をインポートする:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- alice@example.com 用に公開鍵をエクスポートする (`stdout` に出力):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- alice@example.com の秘密鍵をエクスポートする (`stdout` に出力):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
