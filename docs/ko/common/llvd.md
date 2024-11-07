---
layout: page
title: common/llvd (한국어)
description: "Linkedin Learning 비디오 다운로드 도구."
content_hash: d85a7167db54070a71cf5151907c99a4ded7dca8
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/llvd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llvd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llvd

Linkedin Learning 비디오 다운로드 도구.
더 많은 정보: <https://github.com/knowbee/llvd>.

- 쿠키 기반 인증을 사용하여 [c]ourse 다운로드:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코스-슬러그</span>` --cookies`

- 특정 [r]esolution으로 코스 다운로드:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코스-슬러그</span>` -r 720`

- [ca]ptions(자막)과 함께 코스 다운로드:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코스-슬러그</span>` --caption`

- [p]ath를 다운로드하고 10초에서 30초 사이 [t]hrottling 적용:

`llvd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로-슬러그</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10,30</span>` --cookies`
