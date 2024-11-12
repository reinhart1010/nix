---
layout: page
title: osx/qlmanage (한국어)
description: "QuickLook 서버 도구."
content_hash: 0f871bfaadbf5a58d5a7505878e581a37a117fd3
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/qlmanage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/qlmanage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qlmanage

QuickLook 서버 도구.
더 많은 정보: <https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

- 하나 또는 여러 [f]파일에 대해 QuickLook 표시:

`qlmanage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 현재 폴더의 모든 JPEG 파일에 대해 300px 너비의 PNG 썸네일 생성 후, 지정된 폴더에 저장:

`qlmanage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- QuickLook 재설정:

`qlmanage -r`
