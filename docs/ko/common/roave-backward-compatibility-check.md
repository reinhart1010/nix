---
layout: page
title: common/roave-backward-compatibility-check (한국어)
description: "PHP 라이브러리의 두 버전 간 호환성 파손 여부를 확인."
content_hash: 1e0dc86b0dffd0b26f6f50b0d6487d77d50e88d5
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/roave-backward-compatibility-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/roave-backward-compatibility-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># roave-backward-compatibility-check

PHP 라이브러리의 두 버전 간 호환성 파손 여부를 확인.
더 많은 정보: <https://github.com/Roave/BackwardCompatibilityCheck>.

- 마지막 태그 이후의 호환성 파손 점검:

`roave-backward-compatibility-check`

- 특정 태그 이후의 호환성 파손 점검:

`roave-backward-compatibility-check --from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_레퍼런스</span>

- 마지막 태그와 특정 참조 간의 호환성 파손 점검:

`roave-backward-compatibility-check --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_레퍼런스</span>

- 호환성 파손 점검 결과를 Markdown으로 출력:

`roave-backward-compatibility-check --format=markdown > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">결과.md</span>
