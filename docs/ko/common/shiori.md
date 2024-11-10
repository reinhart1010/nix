---
layout: page
title: common/shiori (한국어)
description: "Go로 제작된 간단한 북마크 관리자."
content_hash: 36c3f93945997a0cffbd930029b4d23dc93f9cd8
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/shiori.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shiori

Go로 제작된 간단한 북마크 관리자.
더 많은 정보: <https://github.com/go-shiori/shiori>.

- HTML 넷스케이프 북마크 형식 파일에서 북마크 가져오기:

`shiori import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/북마크들.html</span>

- 지정된 URL을 북마크로 저장:

`shiori add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 저장된 북마크 나열:

`shiori print`

- 저장된 북마크를 브라우저에서 열기:

`shiori open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_id</span>

- 포트 8181에서 북마크 관리를 위한 웹 인터페이스 시작:

`shiori serve --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8181</span>
