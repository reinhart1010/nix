---
layout: page
title: common/mail (한국어)
description: "인수가 주어지지 않으면 사용자의 메일함을 조작하는 명령입니다."
content_hash: 0b02580ff32928a395c66b73637bb22ee2477378
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mail

인수가 주어지지 않으면 사용자의 메일함을 조작하는 명령입니다.
이메일을 보내려면 메시지 본문을 `stdin`에서 작성합니다.
더 많은 정보: <https://manned.org/mail>.

- 개인 메일을 확인하기 위한 대화형 프롬프트 열기:

`mail`

- 입력한 이메일 메시지를 선택적으로 참조(CC)와 함께 보내기. 아래 명령은 `<Enter>`를 누른 후 계속됩니다. 메시지 텍스트를 입력하세요(여러 줄 가능). 메시지 입력이 완료되면 `<Ctrl>-D`를 누르세요:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">받는이@example.com</span>` --cc="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조_이메일_주소</span>`"`

- 파일 내용을 포함하는 이메일 보내기:

`mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOSTNAME 파일명.txt</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">받는이@example.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명.txt</span>

- `tar.gz` 파일을 첨부 파일로 보내기:

`tar cvzf - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2</span>` | uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터.tar.gz</span>` | mail --subject="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">받는이@example.com</span>
