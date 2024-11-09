---
layout: page
title: common/tea (한국어)
description: "Gitea 서버와 상호 작용."
content_hash: 551e19fbf15e8b466786e92082d3f9b301dc0490
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tea.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tea.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tea

Gitea 서버와 상호 작용.
더 많은 정보: <https://gitea.com/gitea/tea>.

- Gitea 서버에 로그인:

`tea login add --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --url "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>`" --token "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>`"`

- 모든 저장소 표시:

`tea repos ls`

- 이슈 목록 표시:

`tea issues ls`

- 특정 저장소의 이슈 목록 표시:

`tea issues ls --repo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>`"`

- 새 이슈 생성:

`tea issues create --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">본문</span>`"`

- 열려 있는 풀 리퀘스트 목록 표시:

`tea pulls ls`

- 현재 저장소를 브라우저에서 열기:

`tea open`
