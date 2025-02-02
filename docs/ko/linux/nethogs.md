---
layout: page
title: linux/nethogs (한국어)
description: "프로세스별 대역폭 사용량 모니터링."
content_hash: f2de194f958411c5f03bb4ed3d6dc80f1cb16490
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/nethogs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nethogs

프로세스별 대역폭 사용량 모니터링.
더 많은 정보: <https://github.com/raboof/nethogs>.

- 루트 권한으로 NetHogs 시작 (기본 장치는 `eth0`):

`sudo nethogs`

- 특정 장치의 대역폭 모니터링:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>

- 여러 장치의 대역폭 모니터링:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치2</span>

- 새로 고침 주기 지정:

`sudo nethogs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>
