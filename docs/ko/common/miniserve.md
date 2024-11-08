---
layout: page
title: common/miniserve (한국어)
description: "간단한 HTTP 파일 서버."
content_hash: 9e80f20ce5572e0c83bafef2e91b06beef75bc81
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/miniserve.html
    icon: bi bi-globe
tldri18n_status: 2
---
# miniserve

간단한 HTTP 파일 서버.
더 많은 정보: <https://github.com/svenstaro/miniserve>.

- 디렉터리 서빙:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 단일 파일 서빙:

`miniserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- HTTP 기본 인증을 사용하여 디렉터리 서빙:

`miniserve --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
