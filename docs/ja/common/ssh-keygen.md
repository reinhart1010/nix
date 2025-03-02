---
layout: page
title: common/ssh-keygen (日本語)
description: "認証やパスワード不要のログインなどに使われるSSHキーを生成します。"
content_hash: a82d0651d4c5bd05fac23ab55c2f6521eddf5f42
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keygen.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keygen.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keygen.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-keygen

認証やパスワード不要のログインなどに使われるSSHキーを生成します。
もっと詳しく: <https://man.openbsd.org/ssh-keygen>。

- 対話的にキーを生成します:

`ssh-keygen`

- 32ラウンド回数の鍵導出関数でed25519鍵を生成し、特定のファイルに保存する:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ed25519</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- Eメールをコメントとして、RSA 4096ビット鍵を生成する:

`ssh-keygen -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -C "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment|email</span>`"`

- known_hostsファイルからホストの鍵を削除する (既知のホストが新しい鍵を持つ場合に便利):

`ssh-keygen -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>

- 鍵のフィンガープリントをMD5 Hexで取得する:

`ssh-keygen -l -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- 鍵のパスワードを変更する:

`ssh-keygen -p -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/filename</span>

- 鍵の形式を変更する (たとえば OPENSSH 形式から PEM 形式へ):

`ssh-keygen -p -N "" -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PEM</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/OpenSSH_private_key</span>

- 秘密鍵から公開鍵を取得する:

`ssh-keygen -y -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/OpenSSH_private_key</span>
