---
layout: page
title: common/crane-append (한국어)
description: "(선택 사항) 기본 이미지를 기반으로 이미지를 푸시."
content_hash: fd59339fc34c9bfd1e511e4382af193265753a8f
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/crane-append.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-append.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane append

(선택 사항) 기본 이미지를 기반으로 이미지를 푸시.
제공된 tarball의 내용이 포함된 레이어를 추가.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- 기본 이미지를 기반으로 하는 이미지 푸시:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>

- tarball에서 추가된 레이어가 있는 이미지 푸시:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--new_layer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이어_이름1 레이어_이름2 ...</span>

- 새로운 태그가 포함된 레이어가 추가된 이미지 푸시:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--new_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 결과 이미지를 새 tarball로 푸시:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>

- Docker 대신 OCI 미디어 유형의 비어있는 기본 이미지를 사용:

`crane append --oci-empty-base`

- 기본 이미지를 기반으로 결과 이미지에 주석을 달기:

`crane append --set-base-image-annotations`

- 도움말 표시:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
