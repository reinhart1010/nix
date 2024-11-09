---
layout: page
title: common/steam (한국어)
description: "Valve의 비디오 게임 플랫폼."
content_hash: ad1156acf01446268a31eec677c8c0337ed0550d
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/steam.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/steam.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/steam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/steam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># steam

Valve의 비디오 게임 플랫폼.
더 많은 정보: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- 디버그 메시지를 `stdout`에 출력하며 Steam 실행:

`steam`

- Steam을 실행하고 앱 내 디버그 콘솔 탭 활성화:

`steam -console`

- 실행 중인 Steam 인스턴스에서 Steam 콘솔 탭 활성화 및 열기:

`steam steam://open/console`

- 지정된 자격 증명으로 Steam 로그인:

`steam -login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- Big Picture 모드로 Steam 실행:

`steam -tenfoot`

- Steam 종료:

`steam -shutdown`
