---
layout: page
title: linux/bluetoothd (한국어)
description: "블루투스 장치를 관리하는 데몬."
content_hash: 62f55b5833ef6fc2c0439d25a3e048770e5cd400
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bluetoothd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothd

블루투스 장치를 관리하는 데몬.
더 많은 정보: <https://manned.org/bluetoothd>.

- 데몬 시작:

`bluetoothd`

- 로그를 `stdout`으로 출력하며 데몬 시작:

`bluetoothd --nodetach`

- 특정 설정 파일을 사용하여 데몬 시작 (기본값은 `/etc/bluetooth/main.conf`):

`bluetoothd --configfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 자세한 출력을 `stderr`로 출력하며 데몬 시작:

`bluetoothd --debug`

- bluetoothd 또는 플러그인 소스의 특정 파일에서 오는 자세한 출력을 사용하여 데몬 시작:

`bluetoothd --debug=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1:경로/대상/파일2:...</span>
