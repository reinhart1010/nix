---
layout: page
title: common/gocryptfs (한국어)
description: "Go로 작성된 암호화된 오버레이 파일 시스템."
content_hash: eb9f5575bdeeb81b3f0b840790bc1d045dd82ec7
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gocryptfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/gocryptfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gocryptfs

Go로 작성된 암호화된 오버레이 파일 시스템.
더 많은 정보: <https://github.com/rfjakob/gocryptfs>.

- 암호화된 파일 시스템 초기화:

`gocryptfs -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_디렉터리</span>

- 암호화된 파일 시스템 마운트:

`gocryptfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 비밀번호 대신 명시적인 마스터 키를 사용하여 마운트:

`gocryptfs --masterkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 비밀번호 변경:

`gocryptfs --passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_디렉터리</span>

- 일반 디렉터리의 암호화된 스냅샷 생성:

`gocryptfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/일반_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_디렉터리</span>
