---
layout: page
title: common/s3cmd (한국어)
description: "S3 호환 객체 저장소에서 데이터를 업로드, 검색 및 관리하기 위한 커맨드라인 도구 및 클라이언트."
content_hash: fefac5aeb0f75dbd2c58a7edd27e9c8bda1b89f0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/s3cmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/s3cmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># s3cmd

S3 호환 객체 저장소에서 데이터를 업로드, 검색 및 관리하기 위한 커맨드라인 도구 및 클라이언트.
더 많은 정보: <https://s3tools.org/s3cmd>.

- 구성/재구성 도구 실행:

`s3cmd --configure`

- 버킷/폴더/객체 나열:

`s3cmd ls s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷|경로/대상/파일</span>

- 버킷/폴더 생성:

`s3cmd mb s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷</span>

- 버킷에서 특정 파일 다운로드:

`s3cmd get s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_파일</span>

- 버킷에 파일 업로드:

`s3cmd put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_파일</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 객체를 특정 버킷 위치로 이동:

`s3cmd mv s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_버킷</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_객체</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_버킷</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_객체</span>

- 특정 객체 삭제:

`s3cmd rm s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체</span>
