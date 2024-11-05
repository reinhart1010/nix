---
layout: page
title: common/pamstack (한국어)
description: "여러 PAM 이미지의 평면을 하나의 PAM 이미지로 스택."
content_hash: 305ec70e0fff480081edf16f9f52b94089898b66
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamstack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamstack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamstack

여러 PAM 이미지의 평면을 하나의 PAM 이미지로 스택.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamstack.html>.

- 지정된 PAM 이미지의 평면을 특정 순서로 스택:

`pamstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.pam 경로/대상/이미지2.pam ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 출력 PAM 파일의 튜플 타입 이름 지정 (최대 255자):

`pamstack -tupletype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">튜플_타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.pam 경로/대상/이미지2.pam ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
