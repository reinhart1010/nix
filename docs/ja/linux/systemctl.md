---
layout: page
title: linux/systemctl (日本語)
description: "systemd システムとサービスマネージャーを制御します。"
content_hash: f942606d6d218c0415ab79a1c12dc0e73a13339f
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/linux/systemctl.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

systemd システムとサービスマネージャーを制御します。
もっと詳しく: <https://www.freedesktop.org/software/systemd/man/systemctl.html>。

- 実行中のサービスを全て表示する:

`systemctl status`

- 失敗状態のユニット一覧:

`systemctl --failed`

- サービスを Start/Stop/Restart/Reload/Show 状態にする:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユニット</span>

- 起動時に起動するユニットを Enable/Disable に設定する:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユニット</span>

- systemdを再読み込みし、新規または変更されたユニットをスキャンする:

`systemctl daemon-reload`

- ユニットが active/enabled/failed かをチェックする:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is-active|is-enabled|is-failed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユニット</span>

- 全ての service/socket/automount ユニットを running/failed 状態でフィルタリングして一覧表示する:

`systemctl list-units --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|socket|automount</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">failed|running</span>

- ユニットファイルの内容と絶対パスを表示する:

`systemctl cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユニット</span>
