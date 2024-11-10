---
layout: page
title: common/soupault (한국어)
description: "HTML 요소 트리 재작성에 기반한 정적 웹사이트 생성기."
content_hash: b0ac7b7788cf5a076685684c5cbd8a5c8459de37
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/soupault.html
    icon: bi bi-globe
tldri18n_status: 2
---
# soupault

HTML 요소 트리 재작성에 기반한 정적 웹사이트 생성기.
HTML 후처리기나 메타데이터 추출기로도 사용될 수 있습니다.
더 많은 정보: <https://soupault.app>.

- 현재 작업 디렉토리에 최소 웹사이트 프로젝트 초기화:

`soupault --init`

- 웹사이트 빌드:

`soupault`

- 기본 설정 파일 및 디렉토리 위치 재정의:

`soupault --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일_경로</span>` --site-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_디렉토리</span>` --build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_디렉토리</span>

- 페이지를 생성하지 않고 메타데이터를 JSON 파일로 추출:

`soupault --index-only --dump-index-json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- 효과적인 설정 표시 (`soupault.toml`의 값과 기본값 포함):

`soupault --show-effective-config`
