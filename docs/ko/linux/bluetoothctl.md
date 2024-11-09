---
layout: page
title: linux/bluetoothctl (한국어)
description: "블루투스 장치를 관리합니다."
content_hash: 369fd33c208f090089c75813b0d4a4cb74fb0a84
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothctl

블루투스 장치를 관리합니다.
더 많은 정보: <https://bitbucket.org/serkanp/bluetoothctl>.

- `bluetoothctl` 셸에 진입:

`bluetoothctl`

- 모든 알려진 장치 나열:

`bluetoothctl devices`

- 블루투스 컨트롤러를 켜거나 끔:

`bluetoothctl power `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- 장치와 페어링:

`bluetoothctl pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥_주소</span>

- 장치 제거:

`bluetoothctl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥_주소</span>

- 페어링된 장치에 연결:

`bluetoothctl connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥_주소</span>

- 페어링된 장치와 연결 해제:

`bluetoothctl disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">맥_주소</span>

- 도움말 표시:

`bluetoothctl help`
