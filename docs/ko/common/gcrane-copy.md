---
layout: page
title: common/gcrane-copy (한국어)
description: "다이제스트 값을 유지하며 소스에서 대상으로 원격 이미지를 효율적으로 복사."
content_hash: c69273402eab41ca8bf07d62082e811d2b84bf7d
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gcrane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane copy

다이제스트 값을 유지하며 소스에서 대상으로 원격 이미지를 효율적으로 복사.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 소스에서 대상으로 이미지 복사:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cp|copy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 최대 동시 복사본 수를 설정, 기본값은 20:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nr_of_copies</span>

- 레포지토리를 통해 반복할지 여부 문의:

`grance copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- 도움말 표시:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
