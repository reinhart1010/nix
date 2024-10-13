---
layout: page
title: common/crane-copy (한국어)
description: "다이제스트 값을 유지하면서 소스에서 대상으로 원격 이미지를 효율적으로 복사."
content_hash: 0d85e6f47aa3aa187364ac97f7ca535c1140108b
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane copy

다이제스트 값을 유지하면서 소스에서 대상으로 원격 이미지를 효율적으로 복사.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- 소스에서 대상으로 이미지를 복사:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 모든 태그 복사:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--all-tags</span>

- 최대 동시 복사본 수를 설정, 기본값은 GOMAXPROCS:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">int</span>

- 대상의 기존 태그를 덮어쓰지 않음:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--no-clobber</span>

- 도움말 표시:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
