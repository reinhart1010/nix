---
layout: page
title: common/aws-ses (한국어)
description: "AWS Simple Email Service용 CLI."
content_hash: 4ce3ab6013dfd4f59868fbca9624753a15b542f5
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-ses.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ses.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-ses.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws ses

AWS Simple Email Service용 CLI.
대규모 인바운드 및 아운바운드 클라우드 이메일 서비스.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- 새로운 수신 규칙 세트를 생성:

`aws ses create-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_모음_이름</span>` --generate-cli-skeleton`

- 활성 수신 규칙 세트 정보를 표시:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- 특정 수신 규칙 정보를 표시:

`aws ses describe-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_모음_이름</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_이름</span>` --generate-cli-skeleton`

- 모든 수신 규칙 세트를 나열:

`aws ses list-receipt-rule-sets --starting-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰_문자열</span>` --max-items `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정수</span>` --generate-cli-skeleton`

- 특정 수신 규칙 세트 삭제 (현재 활성화된 규칙 세트는 삭제할 수 없음):

`aws ses delete-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_정보_이름</span>` --generate-cli-skeleton`

- 특정 수신 규칙 삭제:

`aws ses delete-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_정보_이름</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_이름</span>` --generate-cli-skeleton`

- 이메일 전송:

`aws ses send-email --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">송신_주소</span>` --destination "ToAddresses=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>`" --message "Subject={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject_text</span>`,Charset=utf8},Body={Text={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">body_text</span>`,Charset=utf8},Html={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message_body_containing_html</span>`,Charset=utf8</span>`"`

- 특정 SES 하위 명령어에 대한 도움말 표시:

`aws ses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>` help`
