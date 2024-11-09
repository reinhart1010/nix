---
layout: page
title: common/tt (한국어)
description: "터미널 기반 타자 테스트."
content_hash: 28ee0b3c34955f72e484899a444fdc01f484841d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tt

터미널 기반 타자 테스트.
더 많은 정보: <https://github.com/lemnos/tt>.

- 내장된 영어 인용문 목록으로 인용문 모드 시작:

`tt -quotes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en</span>

- 10개의 단어로 이루어진 5개의 그룹에서 무작위로 선택된 50개의 단어로 구성된 테스트 생성:

`tt -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 10초 동안 지속되는 타이머 테스트 시작:

`tt -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 테마 없이 타이핑하면서 WPM(분당 타자 속도)을 표시하며 `tt` 시작:

`tt -showwpm -notheme`
