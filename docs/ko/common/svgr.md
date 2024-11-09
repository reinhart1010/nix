---
layout: page
title: common/svgr (한국어)
description: "SVG를 React 컴포넌트로 변환."
content_hash: f347542215c2c4396a1533b8110c9590020266c2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/svgr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/svgr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svgr

SVG를 React 컴포넌트로 변환.
더 많은 정보: <https://react-svgr.com>.

- SVG 파일을 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.svg</span>

- SVG 파일을 TypeScript를 사용하여 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr --typescript -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.svg</span>

- SVG 파일을 JSX 변환을 사용하여 React 컴포넌트로 변환하여 `stdout`으로 출력:

`svgr --jsx-runtime automatic -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.svg</span>

- 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>

- 이미 변환된 파일을 건너뛰고 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` --ignore-existing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>

- 파일 이름에 특정 케이스를 사용하여 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` --filename-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">camel|kebab|pascal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>

- 색인 파일을 생성하지 않고 디렉터리의 모든 SVG 파일을 특정 디렉터리의 React 컴포넌트로 변환:

`svgr --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_폴더</span>
