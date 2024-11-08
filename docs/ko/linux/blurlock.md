---
layout: page
title: linux/blurlock (한국어)
description: "화면 잠금 도구 `i3lock`의 단순 래퍼로, 화면을 흐리게 처리합니다."
content_hash: 0e5131f44d3a2ef10c088e2df5eb802bd49c6aa4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/blurlock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/blurlock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># blurlock

화면 잠금 도구 `i3lock`의 단순 래퍼로, 화면을 흐리게 처리합니다.
같이 보기: `i3lock`.
더 많은 정보: <https://gitlab.manjaro.org/packages/community/i3/i3exit/-/blob/master/blurlock>.

- 현재 화면의 흐려진 스크린샷으로 화면 잠금:

`blurlock`

- 화면 잠금 시 잠금 해제 표시기 비활성화 (키 입력 시 피드백 제거):

`blurlock --no-unlock-indicator`

- 화면 잠금 시 마우스 포인터 숨김 해제:

`blurlock --pointer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- 화면 잠금 시 로그인 실패 횟수 표시:

`blurlock --show-failed-attempts`
