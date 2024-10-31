---
layout: page
title: common/glib-compile-resources (한국어)
description: "리소스 파일 (예: 이미지)을 바이너리 리소스 번들로 컴파일."
content_hash: b96faa6bffb6f23bdefd21175446c67ee6a5575d
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glib-compile-resources.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glib-compile-resources

리소스 파일 (예: 이미지)을 바이너리 리소스 번들로 컴파일.
GResource API를 사용해 GTK 애플리케이션에 연결될 수 있음.
더 많은 정보: <https://manned.org/glib-compile-resources>.

- `file.gresource.xml`에서 참조된 리소스를 .gresource 바이너리로 컴파일:

`glib-compile-resources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.gresource.xml</span>

- `file.gresource.xml`에서 참조된 리소스를 C 소스 파일로 컴파일:

`glib-compile-resources --generate-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.gresource.xml</span>

- `file.gresource.xml`의 리소스를 `.c`, `.h` 또는 `.gresource` 확장자를 사용하여 선택한 대상 파일로 컴파일:

`glib-compile-resources --generate --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.gresource.xml</span>

- `file.gresource.xml`에서 참조되는 리소스 파일 목록을 출력:

`glib-compile-resources --generate-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.gresource.xml</span>
