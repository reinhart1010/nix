---
layout: page
title: osx/plutil (한국어)
description: "속성 목록(\"plist\") 파일을 보기, 변환, 검증 또는 편집."
content_hash: 48a844a190ee49fd5621b871c68de18f2ca25604
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/plutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/plutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# plutil

속성 목록("plist") 파일을 보기, 변환, 검증 또는 편집.
더 많은 정보: <https://keith.github.io/xcode-man-pages/plutil.1.html>.

- 하나 이상의 plist 파일 내용을 사람이 읽을 수 있는 형식으로 표시:

`plutil -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.plist 파일2.plist ...</span>

- 하나 이상의 plist 파일을 XML 형식으로 변환하여 원본 파일을 덮어쓰기:

`plutil -convert xml1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.plist 파일2.plist ...</span>

- 하나 이상의 plist 파일을 바이너리 형식으로 변환하여 원본 파일을 덮어쓰기:

`plutil -convert binary1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.plist 파일2.plist ...</span>

- plist 파일을 다른 형식으로 변환하여 새 파일에 쓰기:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.plist</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일.plist</span>

- plist 파일을 다른 형식으로 변환하여 `stdout`에 쓰기:

`plutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml1|binary1|json|swift|objc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.plist</span>` -o -`
