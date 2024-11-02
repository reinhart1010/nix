---
layout: page
title: common/zmv (한국어)
description: "지정된 확장 글로브 패턴과 일치하는 파일을 이동하거나 이름 변경."
content_hash: c8004982ad4161a837021c276489b98a0e881f22
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zmv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zmv

지정된 확장 글로브 패턴과 일치하는 파일을 이동하거나 이름 변경.
같이 보기: `zcp` 및 `zln`.
더 많은 정보: <https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- 정규 표현식과 유사한 패턴을 사용하여 파일 이동:

`zmv '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 이동 결과를 미리 보기(실제 변경 없음):

`zmv -n '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 각 변경 전에 확인을 요청하면서 파일을 대화식으로 이동:

`zmv -i '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 실행 중인 각 작업을 자세히 출력:

`zmv -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`
