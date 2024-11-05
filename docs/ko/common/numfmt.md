---
layout: page
title: common/numfmt (한국어)
description: "숫자를 사람이 읽기 쉬운 문자열로 변환하거나 그 반대로 변환."
content_hash: 55f9dac1cd3322f7ede0f5b305674a7d053fbe6a
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/numfmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/numfmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/numfmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># numfmt

숫자를 사람이 읽기 쉬운 문자열로 변환하거나 그 반대로 변환.
더 많은 정보: <https://www.gnu.org/software/coreutils/numfmt>.

- 1.5K(SI 단위)를 1500으로 변환:

`numfmt --from=si 1.5K`

- 5번째 필드(1부터 시작)를 IEC 단위로 변환하되 헤더는 변환하지 않음:

`ls -l | numfmt --header=1 --field=5 --to=iec`

- IEC 단위로 변환하고, 5자리를 채워 왼쪽 정렬:

`du -s * | numfmt --to=iec --format="%-5f"`
