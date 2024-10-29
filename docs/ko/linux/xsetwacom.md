---
layout: page
title: linux/xsetwacom (한국어)
description: "커맨드 라인 도구로, Wacom 펜 태블릿의 설정을 실행 중에 변경합니다."
content_hash: 2b11021983cf471e180acdc33c217d43cd557f6f
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xsetwacom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xsetwacom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xsetwacom

커맨드 라인 도구로, Wacom 펜 태블릿의 설정을 실행 중에 변경합니다.
더 많은 정보: <https://manned.org/xsetwacom>.

- 사용 가능한 모든 Wacom 장치를 나열. 장치 이름은 첫 번째 열에 표시됩니다:

`xsetwacom list`

- Wacom 영역을 특정 화면에 설정. 화면 이름은 `xrandr`로 확인:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" MapToOutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">화면</span>

- 모드를 상대적(마우스처럼) 또는 절대적(펜처럼) 모드로 설정:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" Mode "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Relative|Absolute</span>`"`

- 입력을 회전(화면을 회전할 때 유용) "자연" 회전에서 0|90|180|270 도로 설정:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" Rotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|half|cw|ccw</span>

- 펜촉이 태블릿에 닿을 때만 버튼이 작동하도록 설정:

`xsetwacom set "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치_이름</span>`" TabletPCButton "on"`
