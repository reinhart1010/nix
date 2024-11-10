---
layout: page
title: linux/rename (한국어)
description: "여러 파일의 이름을 변경합니다."
content_hash: 117c589be07113e8697fb39ad80bc2fa1d01cb32
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rename.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rename.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rename.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rename

여러 파일의 이름을 변경합니다.
참고: 이 페이지는 `util-linux` 패키지의 명령어를 다룹니다.
Perl 버전에 대해서는 `file-rename` 또는 `perl-rename`을 참조하세요.
경고: 이 명령어는 안전장치가 없으며, 파일을 덮어쓰기 전에 확인하지 않습니다.
더 많은 정보: <https://manned.org/rename>.

- 간단한 치환을 사용하여 파일 이름 변경 ('foo'를 'bar'로 변경):

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 실행하지 않고 변경 내용을 표시하는 드라이런:

`rename -vn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 기존 파일을 덮어쓰지 않음:

`rename -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 파일 확장자 변경:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.bak</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- 현재 디렉토리의 모든 파일 이름 앞에 "foo" 추가:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">''</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'foo'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- 숫자가 점차 증가하는 파일 그룹의 이름을 3자리로 0을 채워 변경:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo?</span>` && rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo??</span>
