---
layout: page
title: common/serve (한국어)
description: "정적 파일 제공 및 디렉토리 목록화 도구."
content_hash: 02f7d29e3edd7c579b54a76efa5bbce48a22e51b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/serve.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/serve.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># serve

정적 파일 제공 및 디렉토리 목록화 도구.
더 많은 정보: <https://github.com/vercel/serve>.

- 기본 포트에서 현재 디렉토리를 제공하는 HTTP 서버 시작:

`serve`

- 특정 [p]포트에서 특정 디렉토리를 제공하는 HTTP 서버 시작:

`serve -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 응답에 `Access-Control-Allow-Origin: *` 헤더를 포함하여 CORS가 활성화된 HTTP 서버 시작:

`serve --cors`

- 모든 찾을 수 없는 요청을 `index.html` 파일로 리다이렉트하는 기본 포트의 HTTP 서버 시작:

`serve --single`

- 지정된 인증서를 사용하여 기본 포트에서 HTTPS 서버 시작:

`serve --ssl-cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.pem</span>` --ssl-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.pem</span>

- 특정 구성 파일을 사용하여 기본 포트에서 HTTP 서버 시작:

`serve --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서버.json</span>

- 도움말 표시:

`serve --help`
