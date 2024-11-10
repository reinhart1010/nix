---
layout: page
title: common/swc (한국어)
description: "Rust로 작성된 JavaScript 및 TypeScript 컴파일러."
content_hash: 3fbe8984318dbd022dedd31493cbce2d6185d098
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/swc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swc

Rust로 작성된 JavaScript 및 TypeScript 컴파일러.
더 많은 정보: <https://swc.rs>.

- 지정된 입력 파일을 변환하여 `stdout`에 출력:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 입력 파일이 변경될 때마다 변환:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --watch`

- 지정된 입력 파일을 변환하여 특정 파일에 출력:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 지정된 입력 디렉토리를 변환하여 특정 디렉토리에 출력:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>` --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>

- 특정 설정 파일을 사용하여 지정된 입력 디렉토리를 변환:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>` --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/.swcrc</span>

- glob 경로를 사용하여 지정된 디렉토리의 파일 무시:

`swc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/무시할_파일1 경로/대상/무시할_파일2 ...</span>
