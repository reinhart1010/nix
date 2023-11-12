---
layout: page
title: common/babel (한국어)
description: "코드를 JavaScript ES6/ES7 문법에서 ES5 문법으로 변환하는 변환기입니다."
content_hash: 29dfaad87a81b5ffd268d4e98f6a49617ef36597
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babel

코드를 JavaScript ES6/ES7 문법에서 ES5 문법으로 변환하는 변환기입니다.
더 많은 정보: <https://babeljs.io/>.

- 지정된 입력 파일을 변환하고 stdout`'으로 출력:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 지정된 입력 파일을 변환하고 특정 파일로 출력:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- 입력 파일이 변경될 때마다 변환:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --watch`

- 파일의 전체 디렉토리를 변환:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>

- 디렉토리에서 지정된 쉼표로 구분된 파일 무시:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignored_files</span>

- 축소된 JavaScript로 변환 및 출력:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --minified`

- 출력 형식에 대한 사전 설정 세트를 선택:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">presets</span>

- 사용 가능한 모든 옵션 출력:

`babel --help`
