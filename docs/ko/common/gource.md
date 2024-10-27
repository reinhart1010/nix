---
layout: page
title: common/gource (한국어)
description: "Git, SVN, Mercurial 및 Bazaar 저장소의 애니메이션 트리 다이러그램을 렌더링."
content_hash: 581e2b4e9ecc6f539b71cf64a62881b5d062d6f9
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/gource.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gource.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gource

Git, SVN, Mercurial 및 Bazaar 저장소의 애니메이션 트리 다이러그램을 렌더링.
시간이 지남에 따라 생성, 수정 또는 제거되는 파일 및 디렉터리르 보여줌.
더 많은 정보: <https://gource.io>.

- 디렉토리에서 gource를 실행 (저장소의 루트 디렉토리가 아닌 경우, 그곳에서 루트를 찾음):

`gource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레포지토리</span>

- 사용자 정의 출력 해상도를 사용해, 현재 디렉터리에서 gource를 실행:

`gource -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>

- 애니메이션의 기간을 지정:

`gource -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_척도_승수</span>

- 매일 애니메이션에 표시되는 시간을 지정 (제공된 경우, -c와 결합):

`gource -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- 전체 화면 모드 및 사용자 정의 배경색 사용:

`gource -f -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_색상_코드</span>

- 애니메이션 제목을 지정:

`gource --title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>
