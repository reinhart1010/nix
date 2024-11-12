---
layout: page
title: linux/setcap (한국어)
description: "지정된 파일의 권한 설정."
content_hash: e3371e44b71eb849db6d31478a6cc44f49303588
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setcap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setcap

지정된 파일의 권한 설정.
같이 보기: `getcap`.
더 많은 정보: <https://manned.org/setcap>.

- 주어진 파일에 `cap_net_raw` 권한 설정 (RAW 및 PACKET 소켓 사용을 위해):

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에 여러 권한 설정 (`ep`는 "효과적 허가"를 의미):

`setcap '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_dac_read_search,cap_sys_tty_config+ep</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 모든 권한 제거:

`setcap -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 파일에 현재 지정된 권한이 연관되어 있는지 확인:

`setcap -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_raw</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 선택적 `-n root_uid` 인수는 이 루트 사용자 ID 소유자와 함께 사용자 네임스페이스에서만 파일 권한을 설정하는 데 사용될 수 있음:

`setcap -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_uid</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cap_net_admin</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
