---
layout: page
title: osx/xattr (한국어)
description: "확장 파일 시스템 속성을 다루는 유틸리티."
content_hash: 015a2cd514dc9a5812a5c4f8418994f558e1b139
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/xattr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xattr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xattr

확장 파일 시스템 속성을 다루는 유틸리티.
더 많은 정보: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

- 주어진 파일의 key:value 확장 속성 나열:

`xattr -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 주어진 파일에 속성 작성:

`xattr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 주어진 파일에서 속성 삭제:

`xattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.quarantine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 주어진 파일에서 모든 확장 속성 삭제:

`xattr -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 주어진 폴더에서 속성을 재귀적으로 삭제:

`xattr -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더</span>
