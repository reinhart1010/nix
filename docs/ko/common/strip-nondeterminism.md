---
layout: page
title: common/strip-nondeterminism (한국어)
description: "파일에서 비결정적인 정보(예: 타임스탬프)를 제거."
content_hash: e81fe859cb0396a421d5779494c5ede14461144c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/strip-nondeterminism.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/strip-nondeterminism.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># strip-nondeterminism

파일에서 비결정적인 정보(예: 타임스탬프)를 제거.
더 많은 정보: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>.

- 파일에서 비결정적인 정보 제거:

`strip-nondeterminism `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 유형을 수동으로 지정하여 파일에서 비결정적인 정보 제거:

`strip-nondeterminism --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 비결정적인 정보를 제거하되, 타임스탬프를 제거하는 대신 지정한 UNIX 타임스탬프로 설정:

`strip-nondeterminism --timestamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유닉스_타임스탬프</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
