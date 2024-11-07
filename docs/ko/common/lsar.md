---
layout: page
title: common/lsar (한국어)
description: "아카이브 파일의 내용을 나열합니다."
content_hash: 494ade0c155693e5cf62fe7c4bcd51a36e50d235
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lsar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lsar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lsar

아카이브 파일의 내용을 나열합니다.
같이 보기: `unar`, `ar`.
더 많은 정보: <https://manned.org/lsar>.

- 아카이브 파일의 내용 나열:

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 암호로 보호된 아카이브 파일의 내용 나열:

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 아카이브 내 각 파일에 대한 모든 사용 가능한 정보 출력 (매우 길게 출력됨):

`lsar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-L|--verylong</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 아카이브 파일의 무결성 테스트 (가능한 경우):

`lsar --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 아카이브 파일의 내용을 JSON 형식으로 나열:

`lsar --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 도움말 표시:

`lsar --help`
