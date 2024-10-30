---
layout: page
title: common/gyb (한국어)
description: "HTTPS를 통해 Gmail API를 사용하여 Gmail 메시지를 로컬로 백업."
content_hash: af3b953cd192ecd02a4bf41a5a2a36a959b8878b
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gyb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gyb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gyb

HTTPS를 통해 Gmail API를 사용하여 Gmail 메시지를 로컬로 백업.
더 많은 정보: <https://github.com/GAM-team/got-your-back>.

- Gmail 계정에 있는 모든 이메일의 수와 크기를 추정:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action estimate`

- Gmail 계정을 특정 디렉토리에 백업:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action backup --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- Gmail 계정에서 중요하거나 별표 표시된 이메일만 기본 로컬 폴더에 백업:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is:important OR is:starred</span>`"`

- 로컬 폴더에서 Gmail 계정에서 복원:

`gyb --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@gmail.com</span>` --action restore --local-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>
