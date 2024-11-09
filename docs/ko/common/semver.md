---
layout: page
title: common/semver (한국어)
description: "의미적 버전 문자열 파서."
content_hash: 6624522bc75bb134335bd832a63387e1d8f3bcc1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/semver.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/semver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># semver

의미적 버전 문자열 파서.
더 많은 정보: <https://github.com/npm/node-semver>.

- 버전 문자열이 의미적 버전 규칙을 따르는지 확인 (일치하지 않으면 빈 문자열 출력):

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>

- 버전 문자열을 의미적 버전 형식으로 변환:

`semver --coerce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>

- `1.2.3`이 `^1.0` 범위와 일치하는지 테스트 (일치하지 않으면 빈 문자열 출력):

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` --range "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^1.0</span>`"`

- 여러 범위로 테스트:

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">">=1.0"</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"<2.0"</span>

- 여러 버전 문자열을 테스트하고 일치하는 것만 반환:

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0.0</span>` --range "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^1.0</span>`"`
