---
layout: page
title: common/pampop9 (한국어)
description: "Pop9과 같은 다중 렌즈 카메라를 시뮬레이션."
content_hash: d43525ceedabc8fb2b2945f861f19363cb2a5196
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pampop9.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pampop9.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pampop9

Pop9과 같은 다중 렌즈 카메라를 시뮬레이션.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pampop9.html>.

- 입력 이미지를 x타일 x y타일로 타일링하고, 각 번마다 x델타와 y델타에 따라 오프셋을 증가:

`pampop9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x타일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y타일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x델타</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y델타</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
