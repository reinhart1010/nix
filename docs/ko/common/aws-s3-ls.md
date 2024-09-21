---
layout: page
title: common/aws-s3-ls (한국어)
description: "AWS S3 버킷, 폴더 (접두사) 및 파일 (객체) 나열."
content_hash: c9bb73fe1a9486b7941ba5e4f67fde80a03e8727
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-s3-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-s3-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws s3 ls

AWS S3 버킷, 폴더 (접두사) 및 파일 (객체) 나열.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- 모든 버킷 나열:

`aws s3 ls`

- 버킷 루트 파일 및 폴더 나열 (`s3://`는 선택 사항):

`aws s3 ls s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 디렉터리 내부에 있는 파일과 폴더를 직접 나열:

`aws s3 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리/</span>`/`

- 버킷의 모든 파일 나열:

`aws s3 ls --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>

- 주어진 접두사가 있는 경로의 모든 파일 나열:

`aws s3 ls --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리/</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>

- 도움말 표시:

`aws s3 ls help`
