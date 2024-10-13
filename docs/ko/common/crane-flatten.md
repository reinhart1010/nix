---
layout: page
title: common/crane-flatten (한국어)
description: "이미지의 레이어를 단일 레이어로 병합."
content_hash: 4bfface055a19162ac92309019956ffec61cd827
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-flatten.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane flatten

이미지의 레이어를 단일 레이어로 병합.
태그가 지정되지 않은 경우, 다이제스트를 원본 이미지 저장소에 푸시.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- 이미지 병합:

`crane flatten`

- 병합된 이미지에 새로운 태그 적용:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 도움말 표시:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
