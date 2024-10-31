---
layout: page
title: common/doppler-projects (한국어)
description: "Doppler 프로젝트 관리."
content_hash: a8e1a4d1291c74a3c8c722ccee28b0838a1621d3
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/doppler-projects.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doppler-projects.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doppler projects

Doppler 프로젝트 관리.
더 많은 정보: <https://docs.doppler.com/docs/cli>.

- 모든 프로젝트 가져오기:

`doppler projects`

- 프로젝트에 대한 정보 얻기:

`doppler projects get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|프로젝트_아이디</span>

- 프로젝트 생성:

`doppler projects create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 프로젝트 이름과 설명 업데이트:

`doppler projects update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|프로젝트_아이디</span>` --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_이름</span>`" --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_설명</span>`"`

- 프로젝트 삭제:

`doppler projects delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|프로젝트_아이디</span>
