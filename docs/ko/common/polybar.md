---
layout: page
title: common/polybar (한국어)
description: "빠르고 사용하기 쉬운 상태 표시줄."
content_hash: 4b1f9584a21dc15d252bdbc7b365ec565f373bb8
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/polybar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/polybar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/polybar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># polybar

빠르고 사용하기 쉬운 상태 표시줄.
더 많은 정보: <https://github.com/polybar/polybar/wiki>.

- Polybar 시작 (구성 파일에 하나의 막대만 정의되어 있는 경우 막대 이름은 선택 사항):

`polybar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">막대_이름</span>

- 지정된 구성 파일로 Polybar 시작:

`polybar --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.ini</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">막대_이름</span>

- 구성 파일이 수정될 때 막대를 다시 로드하며 Polybar 시작:

`polybar --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">막대_이름</span>
