---
layout: page
title: common/fastd (한국어)
description: "VPN 데몬."
content_hash: 1c2ba66d2f8167535de4c6f290a276521869239a
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/common/fastd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fastd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/fastd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastd

VPN 데몬.
레이어 2 또는 레이어 3에서 작동하며, Freifunk에서 사용하는 다양한 암호화 방법을 지원.
참고: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`.
더 많은 정보: <https://fastd.readthedocs.io/en/stable/>.

- 특정 구성 파일로 `fastd`를 시작:

`fastd --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fastd.conf</span>

- MTU 1400으로 레이어 3 VPN을 시작하고 파일에서 나머지 구성 매개변수를 로드:

`fastd --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tap</span>` --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1400</span>` --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fastd.conf</span>

- 구성 파일의 유효성을 검증:

`fastd --verify-config --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fastd.conf</span>

- 새로운 키의 쌍을 생성:

`fastd --generate-key`

- 구성 파일의 개인 키에 공개 키를 표시:

`fastd --show-key --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fastd.conf</span>

- 현재 버전 보여주기:

`fastd -v`
