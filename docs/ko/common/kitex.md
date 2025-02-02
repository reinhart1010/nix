---
layout: page
title: common/kitex (한국어)
description: "Go RPC 프레임워크 Kitex에서 제공하는 코드 생성 도구."
content_hash: 215eb8dfeef3028041e0e8b2329feb0fa74568f4
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kitex.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/kitex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kitex

Go RPC 프레임워크 Kitex에서 제공하는 코드 생성 도구.
Kitex는 thrift와 protobuf IDL을 모두 수용하며, 서버 측 프로젝트의 스켈레톤을 생성하는 것을 지원합니다.
더 많은 정보: <https://www.cloudwego.io>.

- 프로젝트가 `$GOPATH`에 있을 때 클라이언트 코드 생성:

`kitex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/IDL_파일.thrift</span>

- 프로젝트가 `$GOPATH`에 없을 때 클라이언트 코드 생성:

`kitex -module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/xx-org/xx-name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/IDL_파일.thrift</span>

- protobuf IDL로 클라이언트 코드 생성:

`kitex -type protobuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/IDL_파일.proto</span>

- 서버 코드 생성:

`kitex -service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/IDL_파일.thrift</span>
