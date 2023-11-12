---
layout: page
title: common/cmp (한국어)
description: "두 개의 파일 비교."
content_hash: f7ed993c271f3e5b50c040a0abf2f158bcf87e30
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cmp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cmp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmp

두 개의 파일 비교.
더 많은 정보: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- 파일 간의 첫 번째 바이트 번호와 선 번호의 차이를 찾습니다:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 모든 바이트 수와 다른 바이트의 차이 찾기:

`cmp -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>
