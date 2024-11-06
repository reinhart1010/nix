---
layout: page
title: common/dvc-add (한국어)
description: "변경된 파일을 색인에 추가."
content_hash: d06637028f10aa66e27d4f0a9e76b97b987902d4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/dvc-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dvc-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dvc-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dvc add

변경된 파일을 색인에 추가.
더 많은 정보: <https://dvc.org/doc/command-reference/add>.

- 단일 대상 파일을 색인에 추가:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 대상 디렉토리를 색인에 추가:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 주어진 대상 디렉토리의 모든 파일을 재귀적으로 추가:

`dvc add --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사용자 정의 `.dvc` 파일 이름으로 대상 파일 추가:

`dvc add --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_name.dvc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
