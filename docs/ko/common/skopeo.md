---
layout: page
title: common/skopeo (한국어)
description: "컨테이너 이미지 관리 도구 모음."
content_hash: 01a94500fc863393ede90f5f9565e969fe5f3525
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/skopeo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/skopeo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># skopeo

컨테이너 이미지 관리 도구 모음.
원격 컨테이너 이미지를 관리하기 위한 다양한 유틸리티 명령을 제공합니다.
더 많은 정보: <https://github.com/containers/skopeo>.

- 레지스트리에서 원격 이미지 검사:

`skopeo inspect docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_호스트명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 원격 이미지의 사용 가능한 태그 목록:

`skopeo list-tags docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_호스트명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 레지스트리에서 이미지 다운로드:

`skopeo copy docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_호스트명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>` dir:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 한 레지스트리에서 다른 레지스트리로 이미지 복사:

`skopeo copy docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스_레지스트리</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>` docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_레지스트리</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 레지스트리에서 이미지 삭제:

`skopeo delete docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_호스트명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 레지스트리에 로그인:

`skopeo login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_호스트명</span>
