---
layout: page
title: common/xxh (한국어)
description: "SSH 세션을 통해 모든 사용자 정의 설정과 함께 셸을 사용하세요."
content_hash: 3eaf1c1615d38b0d60d61274319e81bb2c327859
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xxh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xxh

SSH 세션을 통해 모든 사용자 정의 설정과 함께 셸을 사용하세요.
참고: xxh는 대상 머신의 시스템 디렉토리에 아무것도 설치하지 않습니다; `~/.xxh`를 제거하면 대상 머신에서 xxh의 모든 흔적이 제거됩니다.
더 많은 정보: <https://github.com/xxh/xxh>.

- 호스트에 연결하고 현재 셸 실행:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`"`

- 대화 상자 없이 현재 셸을 대상 머신에 설치:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++install`

- 대상 머신에서 지정된 셸 실행:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xonsh|zsh|fish|bash|osquery</span>

- 대상 머신에서 특정 xxh 구성 디렉토리 사용:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++host-xxh-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.xxh</span>

- 호스트 머신에서 지정된 구성 파일 사용:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++xxh-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.config/xxh/config.xxhc</span>

- SSH 연결에 사용할 비밀번호 지정:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`"`

- 대상 머신에 xxh 패키지 설치:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++install-xxh-packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 대상 머신의 셸 프로세스에 대한 환경 변수 설정:

`xxh "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`" ++env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
