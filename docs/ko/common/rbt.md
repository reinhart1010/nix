---
layout: page
title: common/rbt (한국어)
description: "RBTools는 Review Board 및 RBCommons와 함께 작업하기 위한 명령줄 도구 세트입니다."
content_hash: 53b70bb9c32db5b66413a977339a9098572ba495
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rbt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rbt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rbt

RBTools는 Review Board 및 RBCommons와 함께 작업하기 위한 명령줄 도구 세트입니다.
더 많은 정보: <https://www.reviewboard.org/docs/rbtools/dev/>.

- Review Board에 변경 사항 게시:

`rbt post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변경_번호</span>

- Review Board에 전송될 차이점 표시:

`rbt diff`

- 로컬 브랜치 또는 검토 요청에 변경사항 적용:

`rbt land `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 검토 요청에 대한 변경사항으로 트리 패치:

`rbt patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검토_요청_ID</span>

- RBTool을 설정하여 저장소와 통신하도록 설정:

`rbt setup-repo`
