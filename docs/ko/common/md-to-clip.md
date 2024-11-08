---
layout: page
title: common/md-to-clip (한국어)
description: "tldr 페이지를 커맨드라인 인터페이스 페이지로 변환."
content_hash: d98b1ecbc60ab385483af40a901c24cc98894938
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/md-to-clip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# md-to-clip

tldr 페이지를 커맨드라인 인터페이스 페이지로 변환.
같이 보기: `clip-view`.
더 많은 정보: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>.

- tldr 페이지 파일을 변환하고 같은 디렉토리에 저장:

`md-to-clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/페이지.md 경로/대상/페이지2.md ...</span>

- tldr 페이지 파일을 변환하고 특정 디렉토리에 저장:

`md-to-clip --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/페이지1.md 경로/대상/페이지2.md ...</span>

- tldr 페이지 파일을 변환하여 `stdout`에 출력:

`md-to-clip --no-file-save <(echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지-내용</span>`')`

- 특정 설정 파일에서 추가 플레이스홀더를 인식하여 tldr 페이지 파일 변환:

`md-to-clip --special-placeholder-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/페이지1.md 경로/대상/페이지2.md ...</span>

- 도움말 표시:

`md-to-clip --help`

- 버전 정보 표시:

`md-to-clip --version`
