---
layout: page
title: common/hugo (한국어)
description: "템플릿 기반 정적 사이트 생성기. 모듈, 구성 요소 및 테마를 사용"
content_hash: 9f41c5e90a6f600787eed863e14f30d8bd476c8f
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/hugo.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/hugo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hugo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hugo

템플릿 기반 정적 사이트 생성기. 모듈, 구성 요소 및 테마를 사용
`server`와 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
더 많은 정보: <https://gohugo.io>.

- 새로운 Hugo 사이트 생성:

`hugo new site `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사이트</span>

- 새로운 Hugo 테마를 생성 (테마는 <https://themes.gohugo.io/>에서도 다운로드 할 수 있음):

`hugo new theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테마_이름</span>

- 새로운 페이지 생성:

`hugo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">섹션_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_이름</span>

- `./public/` 디렉토리에 사이트를 구축:

`hugo`

- "초안"으로 표시된 페이지를 포함하는 사이트 구축:

`hugo --buildDrafts`

- 로컬 IP에 사이트 구축:

`hugo server --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬-ip</span>` --baseURL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://로컬-ip</span>

- 주어진 디렉토리에 사이트를 구축:

`hugo --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 사이트를 구축하고, 웹 서버를 시작하여 서비스를 제공하여, 페이지가 편집되면 자동으로 다시 로드됨:

`hugo server`
