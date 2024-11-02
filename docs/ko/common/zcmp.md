---
layout: page
title: common/zcmp (한국어)
description: "압축된 파일 비교."
content_hash: ce8b4af5a0f034410af05d9623581e89d74e3d9c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zcmp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zcmp

압축된 파일 비교.
더 많은 정보: <https://manned.org/zcmp>.

- `gzip`로 압축된 두 파일을 `cmp`로 비교:

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.gz</span>

- 파일을 해당 gzipped 버전과 비교 (이미 `.gz`가 존재한다고 가정):

`zcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
