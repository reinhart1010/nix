---
layout: page
title: common/combine (한국어)
description: "두 파일의 줄에서 설정 작업 수행."
content_hash: fd715071b73ec25d8e5f8b50b382fbb4e939dfd5
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/combine.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/combine.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># combine

두 파일의 줄에서 설정 작업 수행.
출력되는 줄의 순서는 첫 번째 파일의 줄 순서에 따라 결정됨.
참고: `diff`.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 지정된 두 파일 모두에 있는 라인을 출력:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 첫 번째 파일에는 있지만, 두 번째 파일에는 없는 줄을 출력:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 지정된 파일 중 하나에 있는 줄을 출력:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 지정된 파일 중 정확히 하나에만 있는 줄을 출력:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` xor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
