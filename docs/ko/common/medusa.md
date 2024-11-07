---
layout: page
title: common/medusa (한국어)
description: "다양한 프로토콜에 대한 모듈식 병렬 로그인 브루트포싱 도구."
content_hash: 14d0d04681ebcbb675441fdfdfb37920d3fb4aac
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/medusa.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/medusa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/medusa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># medusa

다양한 프로토콜에 대한 모듈식 병렬 로그인 브루트포싱 도구.
더 많은 정보: <https://jmk-foofus.github.io/medusa/medusa.html>.

- 설치된 모든 모듈 나열:

`medusa -d`

- 특정 모듈의 사용 예시 보기 (`medusa -d`로 모든 설치된 모듈 나열 가능):

`medusa -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh|http|web-form|postgres|ftp|mysql|...</span>` -q`

- 사용자 이름 파일과 비밀번호 파일을 사용하여 FTP 서버에 대해 브루트포싱 실행:

`medusa -M ftp -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자_이름_파일</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>

- 지정된 사용자 이름, 비밀번호, 사용자 에이전트를 사용하여 HTTP 서버에 로그인 시도:

`medusa -M HTTP -h host -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -m USER-AGENT:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트</span>`"`

- 사용자 이름 파일과 해시를 사용하여 MySQL 서버에 대해 브루트포싱 실행:

`medusa -M mysql -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/사용자_이름_파일</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시</span>` -m PASS:HASH`

- 사용자 이름과 pwdump 파일을 사용하여 SMB 서버 목록에 대해 브루트포싱 실행:

`medusa -M smbnt -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/호스트_파일</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pwdump_파일</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -m PASS:HASH`
