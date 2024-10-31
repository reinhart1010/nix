---
layout: page
title: common/gum (한국어)
description: "매력적인 쉘 스크립트 만들기."
content_hash: 71e5477fec3978f83b6a21c184b4b259b760335b
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gum

매력적인 쉘 스크립트 만들기.
더 많은 정보: <https://github.com/charmbracelet/gum>.

- `stdout`으로 출력할 특정 옵션을 대화형으로 선택:

`gum choose "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_3</span>`"`

- 사용자가 특정 자리 표시자와 함께 문자열을 입력할 수 있는 대화형 프롬프트를 열기:

`gum input --placeholder "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 대화형 확인 프롬프트를 열고 `0` 또는 `1`로 종료:

`gum confirm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Continue?</span>`" --default=false --affirmative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Yes</span>`" --negative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">No</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&& echo "Yes selected" || echo "No selected"</span>

- 명령이 실행되는 동안 텍스트와 함께 스피너를 표시:

`gum spin --spinner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loading...</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 이모티콘을 포함하도록 텍스트 형식을 지정:

`gum format -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emoji</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:smile: :heart: hello</span>`"`

- 여러 줄의 텍스트를 대화식으로 프롬프트하고 (저장하려면 CTRL + D) `data.txt`에 작성:

`gum write > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.txt</span>
