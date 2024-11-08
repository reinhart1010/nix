---
layout: page
title: common/r2e (한국어)
description: "RSS 피드를 이메일 주소로 전달."
content_hash: 52e9bb219b8d3b5ae65c29529249852b062c7b4b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/r2e.html
    icon: bi bi-globe
tldri18n_status: 2
---
# r2e

RSS 피드를 이메일 주소로 전달.
설정된 `sendmail` 또는 SMTP 설정이 필요합니다.
더 많은 정보: <https://github.com/rss2email/rss2email>.

- 이메일 주소로 이메일을 보내는 새로운 피드 데이터베이스 생성:

`r2e new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_주소</span>

- 피드 구독:

`r2e add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">피드_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">피드_URI</span>

- 새로운 이야기를 이메일 주소로 전송:

`r2e run`

- 모든 피드 나열:

`r2e list`

- 지정된 색인의 피드 삭제:

`r2e delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색인</span>
