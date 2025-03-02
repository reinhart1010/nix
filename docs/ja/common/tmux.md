---
layout: page
title: common/tmux (日本語)
description: "端末のマルチプレクサ。"
content_hash: e54cebf9f01e4f13ae528d6b11d07795258431c6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tmux.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tmux.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tmux.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmux

端末のマルチプレクサ。
ウィンドウやペインなどによる複数セッションを可能にします。
も参照してください: `zellij`, `screen` 。
もっと詳しく: <https://github.com/tmux/tmux>。

- 新規セッションの開始:

`tmux`

- 新しい名前付きセッションを開始する:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">セッション名</span>

- 既存のセッションを一覧表示:

`tmux ls`

- 直近に使用したセッションにアタッチ:

`tmux attach`

- 現在のセッションからの切り離し（tmuxセッション内）:

`<Ctrl>-B d`

- 新しいウィンドウを作成する（tmuxセッション内）:

`<Ctrl>-B c`

- セッションとウィンドウの切り替え（tmuxセッション内）:

`<Ctrl>-B w`

- 名前を指定してセッションを終了させる:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">セッション名</span>
