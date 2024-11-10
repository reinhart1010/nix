---
layout: page
title: common/sendmail (한국어)
description: "이메일 보내기."
content_hash: d3ed71acbe6c9add56a0105888732c18ec6c5f94
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sendmail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sendmail

이메일 보내기.
더 많은 정보: <https://manned.org/sendmail>.

- `message.txt`의 내용을 로컬 사용자 `username`의 메일 디렉토리로 전송:

`sendmail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.txt</span>

- 메일 서버가 설정되어 있다고 가정하고, you@yourdomain.com에서 test@gmail.com으로 `message.txt`의 내용을 포함한 이메일 보내기:

`sendmail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">you@yourdomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test@gmail.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.txt</span>

- 메일 서버가 설정되어 있다고 가정하고, you@yourdomain.com에서 test@gmail.com으로 `file.zip` 파일을 포함한 이메일 보내기:

`sendmail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">you@yourdomain.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test@gmail.com</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.zip</span>
