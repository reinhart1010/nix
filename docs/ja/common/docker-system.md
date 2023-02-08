---
layout: page
title: common/docker-system (日本語)
description: "Dockerのデータ管理とシステム全体に関わる情報の表示をします。"
content_hash: 21786bf7ca9057d382489f2825794b9389001941
last_modified_at: 2023-02-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker system

Dockerのデータ管理とシステム全体に関わる情報の表示をします。
詳しくはこちら: <https://docs.docker.com/engine/reference/commandline/system/>.

- ヘルプの表示をする:

`docker system`

- Dockerディスクの使用量を表示する:

`docker system df`

- ディスクの使用量に関して詳細な情報を表示する:

`docker system df --verbose`

- 不使用データを削除する:

`docker system prune`

- 不使用データのうち指定時間より前に作成されたものを削除する:

`docker system prune --filter="until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">時</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分</span>`m"`

- Dockerデーモンからのリアルタイムイベントを表示する:

`docker system events`

- コンテナからのリアルタイムイベントを適正なJSON行としてストリーム表示する:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- システム全体に関わる情報の表示をする:

`docker system info`
