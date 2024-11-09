---
layout: page
title: linux/dm-tool (한국어)
description: "디스플레이 관리자와 통신하는 도구."
content_hash: acff0ee34ce2269869182304cdb73ea3e0c8b745
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dm-tool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dm-tool

디스플레이 관리자와 통신하는 도구.
더 많은 정보: <https://manned.org/dm-tool>.

- 현재 데스크톱 세션을 열어두고 로그인한 사용자가 인증하면 복원되도록 하면서 그리터 표시:

`dm-tool switch-to-greeter`

- 현재 세션 잠금:

`dm-tool lock`

- 특정 사용자로 전환하며 필요 시 인증 프롬프트 표시:

`dm-tool switch-to-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션</span>

- 실행 중인 LightDM 세션 내에서 동적 시트 추가:

`dm-tool add-seat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xlocal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
