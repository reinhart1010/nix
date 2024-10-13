---
layout: page
title: common/crane-registry (한국어)
description: "이 명령은 자동으로 선택된 포트(:0), $PORT 또는 --address에서 레지스트리 구현을 제공."
content_hash: 37121812c3c110865308c9fcd0894e4ed27407fc
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-registry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane registry

이 명령은 자동으로 선택된 포트(:0), $PORT 또는 --address에서 레지스트리 구현을 제공.
서버가 push 및 pull을 수락하는 동안 명령 블록과 내용을 메모리 및 디스크에 저장할 . 수 있음.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- 레지스트리 구현 제공:

`crane registry serve`

- 서버 준비 상태의 주소:

`crane registry serve --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_이름</span>

- blob이 저장될 디렉터리의 경로:

`crane registry serve --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/store_dir</span>

- 도움말 표시:

`crane registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>

- 도움말 표시:

`crane registry serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
