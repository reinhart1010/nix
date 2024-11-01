---
layout: page
title: common/updog (한국어)
description: "Python의 SimpleHTTPServer를 대체하는 도구."
content_hash: 74ba3353dc823818bc51a8d7a247df57be3855c8
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/updog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/updog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># updog

Python의 SimpleHTTPServer를 대체하는 도구.
HTTP/S를 통해 업로드와 다운로드를 지원하며, 임시 SSL 인증서를 설정하고 HTTP 기본 인증을 사용할 수 있습니다.
더 많은 정보: <https://github.com/sc0tfree/updog>.

- 현재 디렉토리에 대한 HTTP 서버 시작:

`updog`

- 지정된 디렉토리에 대한 HTTP 서버 시작:

`updog --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/폴더</span>

- 지정된 포트에서 HTTP 서버 시작:

`updog --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 비밀번호를 사용하여 HTTP 서버 시작 (로그인 시 사용자 이름을 비워두고 비밀번호 필드에 비밀번호 입력):

`updog --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- SSL을 통한 전송 암호화 활성화:

`updog --ssl`
