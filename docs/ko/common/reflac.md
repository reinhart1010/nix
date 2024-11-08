---
layout: page
title: common/reflac (한국어)
description: "FLAC 파일을 메타데이터를 유지하며 제자리에서 재압축."
content_hash: 1772a24ab8e9e9863fcce2e1724d0e734c01dfac
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/reflac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reflac

FLAC 파일을 메타데이터를 유지하며 제자리에서 재압축.
더 많은 정보: <https://github.com/chungy/reflac>.

- FLAC 파일이 있는 디렉토리 재압축:

`reflac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 최대 압축 사용 (매우 느림):

`reflac --best `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 처리 중인 파일 이름 표시:

`reflac --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 하위 디렉토리까지 재귀적으로 처리:

`reflac --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 파일 수정 시간 보존:

`reflac --preserve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
