---
layout: page
title: common/zdiff (한국어)
description: "`gzip` 아카이브에서 `diff` 호출."
content_hash: 817e333207e5309c7a9f04656a6bf2bd45cc384b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zdiff

`gzip` 아카이브에서 `diff` 호출.
더 많은 정보: <https://manned.org/zdiff>.

- 필요 시 압축을 해제하여 두 파일 비교:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.gz</span>

- 동일한 이름의 `gzip` 아카이브와 파일 비교:

`zdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
