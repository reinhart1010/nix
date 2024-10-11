---
layout: page
title: common/gh (한국어)
description: "GitHub와 원활하게 작업."
content_hash: 6a863f64bde7e1ab12f956033934b892330f11b3
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/gh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh

GitHub와 원활하게 작업.
`config`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://cli.github.com/>.

- GitHub 리포지토리를 로컬에 복제:

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리포지토리</span>

- 새 이슈 생성:

`gh issue create`

- 현재 리포지토리의 열린 이슈를 보고 필터링:

`gh issue list`

- 기본 웹 브라우저에서 이슈 보기:

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 풀 리퀘스트 생성:

`gh pr create`

- 기본 웹 브라우저에서 풀 리퀘스트 보기:

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호</span>

- 특정 풀 리퀘스트를 로컬에 체크아웃:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_번호</span>

- 리포지토리의 풀 리퀘스트 상태 확인:

`gh pr status`
