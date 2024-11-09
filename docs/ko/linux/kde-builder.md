---
layout: page
title: linux/kde-builder (한국어)
description: "소스 저장소에서 KDE 구성 요소를 쉽게 빌드."
content_hash: 5e817895416656ff06777e61f18b928877ca92eb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kde-builder.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/kde-builder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kde-builder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kde-builder

소스 저장소에서 KDE 구성 요소를 쉽게 빌드.
`kdesrc-build`의 대체 도구.
더 많은 정보: <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>.

- `kde-builder` 초기 설정:

`kde-builder --initial-setup`

- KDE 구성 요소 및 의존성을 소스에서 컴파일:

`kde-builder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 로컬 코드를 업데이트하지 않고 의존성을 컴파일하지 않으며 구성 요소 컴파일:

`kde-builder --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 컴파일 전 빌드 디렉토리 [r]efresh:

`kde-builder --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 특정 의존성부터 컴파일 재개:

`kde-builder --resume-from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성_구성_요소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>

- 지정된 실행 파일 이름으로 구성 요소 실행:

`kde-builder --run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일_이름</span>

- 모든 구성된 구성 요소 빌드:

`kde-builder`

- 빌드 실패 시 구성 요소 대신 시스템 라이브러리 사용:

`kde-builder --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소_이름</span>
