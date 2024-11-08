---
layout: page
title: common/mailx (한국어)
description: "메일을 보내고 받습니다."
content_hash: d5aa6661adb6aafe5401577e85bc6aee98c9e57e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mailx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mailx

메일을 보내고 받습니다.
더 많은 정보: <https://manned.org/mailx>.

- 메일 보내기 (명령어 입력 후 내용을 작성하고 `Ctrl+D`로 종료):

`mailx -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>

- 다른 명령의 출력을 메일 내용으로 보내기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내용</span>`" | mailx -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>

- 파일에서 읽은 내용을 메일로 보내기:

`mailx -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내용.txt</span>

- 메일을 보내고 다른 주소로 CC하기:

`mailx -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>

- 발신자 주소를 지정하여 메일 보내기:

`mailx -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">발신자_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>

- 첨부 파일과 함께 메일 보내기:

`mailx -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수신자_주소</span>
