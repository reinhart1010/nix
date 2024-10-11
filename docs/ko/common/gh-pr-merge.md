---
layout: page
title: common/gh-pr-merge (한국어)
description: "GitHub 풀 리퀘스트 병합."
content_hash: 27380e9623913c85cd359898017c505092d64f93
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-pr-merge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-pr-merge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh pr merge

GitHub 풀 리퀘스트 병합.
더 많은 정보: <https://cli.github.com/manual/gh_pr_merge>.

- 현재 브랜치와 연관된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge`

- 지정된 풀 리퀘스트를 대화식으로 병합:

`gh pr merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- 로컬과 원격 모두에서 브랜치를 삭제하며 풀 리퀘스트 병합:

`gh pr merge --delete-branch`

- 지정된 병합 전략으로 현재 풀 리퀘스트 병합:

`gh pr merge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">merge|squash|rebase</span>

- 지정된 병합 전략과 커밋 메시지로 현재 풀 리퀘스트 병합:

`gh pr merge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">merge|squash|rebase</span>` --subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>

- 메시지 본문과 함께 현재 풀 리퀘스트를 하나의 커밋으로 압축하여 병합:

`gh pr merge --squash --body="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message_body</span>`"`

- 도움말 표시:

`gh pr merge --help`
