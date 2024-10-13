---
layout: page
title: common/crane-pull (한국어)
description: "참조를 통해 원격 이미지를 가져오고 해당 콘텐츠를 로컬에 저장."
content_hash: 36fe777c66a1f4de2c82164c4b9a904839a24576
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane pull

참조를 통해 원격 이미지를 가져오고 해당 콘텐츠를 로컬에 저장.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- 원격 이미지 가져오기:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>

- --format=oci와 함께 사용할 때 주석으로 가져오는 데 사용되는 이미지 참조를 유지:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` --annotate-ref`

- 캐시 이미지 레이어 경로:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cache_path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/캐시</span>

- 이미지를 저장할 형식 지정 (기본값 'tarball'):

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포맷_이름</span>

- 도움말 표시:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
