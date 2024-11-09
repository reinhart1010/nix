---
layout: page
title: common/sftp (한국어)
description: "안전한 파일 전송 프로그램."
content_hash: d966254c3c6cb0e7bd07dedcc260db3f2ab290dd
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sftp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sftp

안전한 파일 전송 프로그램.
SSH를 통해 호스트 간 파일을 복사하는 대화형 프로그램.
비대화형 파일 전송은 `scp` 또는 `rsync`를 참조하세요.
더 많은 정보: <https://manned.org/sftp>.

- 원격 서버에 연결하고 대화형 명령 모드로 진입:

`sftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 다른 포트를 사용하여 연결:

`sftp -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 사전 정의된 호스트를 사용하여 연결 (`~/.ssh/config`에 설정된 경우):

`sftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 원격 파일을 로컬 시스템으로 전송:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/원격_파일</span>

- 로컬 파일을 원격 시스템으로 전송:

`put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/로컬_파일</span>

- 원격 디렉토리를 로컬 시스템으로 재귀적으로 전송 (`put`에도 적용 가능):

`get -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/원격_디렉토리</span>

- 로컬 컴퓨터의 파일 목록 보기:

`lls`

- 원격 컴퓨터의 파일 목록 보기:

`ls`
