---
layout: page
title: common/polybar-msg (한국어)
description: "`polybar`를 프로세스 간 메시징(IPC)을 사용하여 제어."
content_hash: d185a7368d1d007c588f743c6028da2c9555c530
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/polybar-msg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/polybar-msg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/polybar-msg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># polybar-msg

`polybar`를 프로세스 간 메시징(IPC)을 사용하여 제어.
참고: IPC는 기본적으로 비활성화되어 있으며, Polybar 설정에서 `enable-ipc = true`로 설정하여 활성화할 수 있습니다.
더 많은 정보: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

- 바 종료:

`polybar-msg cmd quit`

- 바를 제자리에서 재시작:

`polybar-msg cmd restart`

- 바 숨기기 (이미 바가 숨겨져 있으면 아무 작업도 하지 않음):

`polybar-msg cmd hide`

- 바 다시 표시 (바가 숨겨져 있지 않으면 아무 작업도 하지 않음):

`polybar-msg cmd show`

- 숨김/표시 전환:

`polybar-msg cmd toggle`

- 모듈 작업 실행 (데이터 문자열은 선택 사항):

`polybar-msg action "#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_문자열</span>`"`

- 특정 Polybar 인스턴스에만 메시지 전송 (기본적으로 모든 인스턴스):

`polybar-msg -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmd|action</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이로드</span>
