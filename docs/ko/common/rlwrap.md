---
layout: page
title: common/rlwrap (한국어)
description: "REPL 명령에 라인 편집, 지속적인 히스토리 및 프롬프트 완성을 추가."
content_hash: b235cec163c5d87b42a5f9281851398b4d78cb19
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rlwrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rlwrap

REPL 명령에 라인 편집, 지속적인 히스토리 및 프롬프트 완성을 추가.
더 많은 정보: <https://github.com/hanslub42/rlwrap>.

- 라인 편집, 지속적인 히스토리 및 프롬프트 완성을 사용하여 REPL 명령 실행:

`rlwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 입력 및 출력에서 본 모든 단어를 프롬프트 완성에 사용:

`rlwrap --remember `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 프롬프트에 ANSI 색상 코드가 포함된 경우 더 나은 프롬프트 완성:

`rlwrap --ansi-colour-aware `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 파일 이름 완성 활성화 (대소문자 구분):

`rlwrap --complete-filenames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 색상이 있는 프롬프트 추가, 색상 이름 또는 ASCI 색상 사양 사용. 대문자 색상 이름은 굵게 스타일링:

`rlwrap --prompt-colour=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|red|green|yellow|blue|cyan|purple|white|colour_spec</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
