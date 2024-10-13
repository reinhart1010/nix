---
layout: page
title: common/crane-index-filter (한국어)
description: "플랫폼 기반 필터링을 통해 원격 인덱스를 수정."
content_hash: b1cff67220d208c61f9fdad449730bf34430f9e4
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-index-filter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane index filter

플랫폼 기반 필터링을 통해 원격 인덱스를 수정.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- 원격 인덱스 수정:

`crane index filter`

- os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,<platform></span>` 형식으로 기본에서 유지할 플랫폼을 지정:

`crane index filter --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼1 플랫폼2 ...</span>

- 결과 이미지에 적용할 태그 지정:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tags</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 도움말 표시:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
