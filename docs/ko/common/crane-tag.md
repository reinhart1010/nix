---
layout: page
title: common/crane-tag (한국어)
description: "`copy` 명령과 달리 다운로드지 않고 원격 이미지에 효율적으로 태그를 지정."
content_hash: 491e3330527f00885c2845c719b1db4dedaffaa3
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/crane-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane tag

`copy` 명령과 달리 다운로드지 않고 원격 이미지에 효율적으로 태그를 지정.
매니페스트가 이미 존재한다는 것을 알고 있어, 레이어 존재 확인을 건너뛰므로 속도가 약간 빨라짐.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- 원격 이미지 태깅:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 도움말 표시:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
