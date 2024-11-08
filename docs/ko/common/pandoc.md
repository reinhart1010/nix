---
layout: page
title: common/pandoc (한국어)
description: "다양한 형식 간에 문서를 변환합니다."
content_hash: ff6a9439963fd6f18ef137cda76cdcd3a1742907
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pandoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pandoc

다양한 형식 간에 문서를 변환합니다.
더 많은 정보: <https://pandoc.org/MANUAL.html>.

- 파일을 PDF로 변환 (출력 형식은 파일 확장자로 결정됨):

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.md</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 적절한 헤더/푸터가 있는 독립 실행형 파일로 변환 (LaTeX, HTML 등):

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.md</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--standalone</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.html</span>

- 형식 감지 및 변환을 수동으로 지정 (파일 이름 확장자를 사용한 자동 형식 감지를 무시하거나 파일 이름 확장자가 전혀 없는 경우):

`pandoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|-r|--from|--read</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docx|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-w|--to|--write</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 지원되는 모든 입력 형식 나열:

`pandoc --list-input-formats`

- 지원되는 모든 출력 형식 나열:

`pandoc --list-output-formats`
