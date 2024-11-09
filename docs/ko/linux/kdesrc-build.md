---
layout: page
title: linux/kdesrc-build (한국어)
description: "KDE 구성 요소를 소스 저장소에서 손쉽게 빌드."
content_hash: 46f1c418f65f021d18ac8216e456cf60a56b1256
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kdesrc-build.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kdesrc-build.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdesrc-build

KDE 구성 요소를 소스 저장소에서 손쉽게 빌드.
더 많은 정보: <https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/index.html>.

- `kdesrc-build` 초기화:

`kdesrc-build --initial-setup`

- KDE 구성 요소와 그 의존성을 소스에서 컴파일:

`kdesrc-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 로컬 코드 업데이트 없이, 의존성 컴파일 없이 구성 요소 컴파일:

`kdesrc-build --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 컴파일 전에 빌드 디렉토리 새로고침:

`kdesrc-build --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 특정 의존성에서 컴파일 재개:

`kdesrc-build --resume-from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성_구성_요소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 지정된 실행 파일 이름으로 구성 요소 실행:

`kdesrc-build --run --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 모든 구성된 구성 요소 빌드:

`kdesrc-build`

- 빌드 실패 시 구성 요소 대신 시스템 라이브러리 사용:

`kdesrc-build --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>
