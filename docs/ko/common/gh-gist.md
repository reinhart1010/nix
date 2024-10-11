---
layout: page
title: common/gh-gist (한국어)
description: "GitHub Gist 작업."
content_hash: 735613854c37d2beb9ae6161c532363b3267e073
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-gist.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gh-gist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-gist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh gist

GitHub Gist 작업.
더 많은 정보: <https://cli.github.com/manual/gh_gist>.

- 하나 이상의 파일에서 새 Gist 생성:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 설명으로 새 Gist 생성:

`gh gist create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` --desc "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`"`

- Gist 수정:

`gh gist edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>

- 현재 로그인된 사용자가 소유한 최대 42개의 Gist 나열:

`gh gist list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- 기본 브라우저에서 마크다운 렌더링 없이 Gist 보기:

`gh gist view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id|url</span>` --web --raw`
