---
layout: page
title: common/xml (한국어)
description: "XMLStarlet 도구 모음: XML 문서를 쿼리, 편집, 검사, 변환 및 변형."
content_hash: 54c9a4597d4deefd147f339ca71dc6003d6a0e41
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xml.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml

XMLStarlet 도구 모음: XML 문서를 쿼리, 편집, 검사, 변환 및 변형.
`xml validate`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- 하위 명령 목록을 포함한 일반 도움말 표시:

`xml --help`

- 파일 또는 URI에서 입력을 받아 `stdout`에 출력하여 하위 명령 실행:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>

- `stdin`과 `stdout`을 사용하여 하위 명령 실행:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>

- 파일 또는 URI에서 입력을 받아 파일로 출력하여 하위 명령 실행:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 특정 하위 명령에 대한 도움말 표시:

`xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`

- 버전 표시:

`xml --version`
