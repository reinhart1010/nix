---
layout: page
title: common/gh-pr (한국어)
description: "GitHub 풀 리퀘스트를 관리."
content_hash: ab4420e7dd26be9eee704dd72ef25971fcf70ecf
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-pr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-pr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh pr

GitHub 풀 리퀘스트를 관리.
`create`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://cli.github.com/manual/gh_pr>.

- 풀 리퀘스트 생성:

`gh pr create`

- 특정 풀 리퀘스트를 로컬에서 체크아웃:

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- 현재 브랜치의 풀 리퀘스트에서 변경 사항 보기:

`gh pr diff`

- 현재 브랜치의 풀 리퀘스트 승인:

`gh pr review --approve`

- 현재 브랜치와 연관된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge`

- 풀 리퀘스트를 대화식으로 수정:

`gh pr edit`

- 풀 리퀘스트의 기준 브랜치 수정:

`gh pr edit --base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- 현재 저장소의 풀 리퀘스트 상태 확인:

`gh pr status`
