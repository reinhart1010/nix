---
layout: page
title: common/glab (한국어)
description: "GitLab으로 원활하게 작업."
content_hash: b4c9b93f86a53070fa61f2a78a1d396b94b0f1d7
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/glab.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/glab.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># glab

GitLab으로 원활하게 작업.
`config`와 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
더 많은 정보: <https://github.com/profclems/glab>.

- 로컬에서 GitLab 저장소를 복제:

`glab repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>

- 새로운 이슈 생성:

`glab issue create`

- 현재 저장소의 공개 이슈를 보고 필터링:

`glab issue list`

- 기본 브라우저에서 이슈 보기:

`glab issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 병합 요청을 생성:

`glab mr create`

- 기본 웹 브라우저에서 풀 요청 보기:

`glab mr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호</span>

- 특정 풀 요청을 로컬에서 확인:

`glab mr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호</span>
