---
layout: page
title: common/gitwatch (한국어)
description: "파일 또는 디렉터리 변경 사항을 Git 리포지토리에 자동으로 커밋."
content_hash: 4f107efb5e5fb298cdc6253843932047d8d09b95
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitwatch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitwatch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitwatch

파일 또는 디렉터리 변경 사항을 Git 리포지토리에 자동으로 커밋.
더 많은 정보: <https://github.com/gitwatch/gitwatch>.

- 파일이나 디렉터리에 대한 모든 변경 사항을 자동으로 커밋:

`gitwatch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 변경 사항을 자동으로 커밋하고 원격 저장소에 푸시:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 변경 사항을 자동으로 커밋하고 원격 저장소의 특정 브랜치로 푸시:

`gitwatch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>
