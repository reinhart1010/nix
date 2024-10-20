---
layout: page
title: common/ftp (한국어)
description: "파일 전송 프로토콜을 통해 서버와 상호 작용하는 도구."
content_hash: 18e35bf4539dc16c6e673a09a2c797580f517c86
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ftp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ftp

파일 전송 프로토콜을 통해 서버와 상호 작용하는 도구.
더 많은 정보: <https://manned.org/ftp>.

- FTP 서버에 연결:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.example.com</span>

- IP 주소와 포트를 지정하여 FTP 서버에 연결:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 바이너리 전송 모드 (그래픽, 압축 파일 등)로 전환:

`binary`

- 모든 파일에 대해 확인 메시지를 표시하지 않고 여러 파일을 전송:

`prompt off`

- 여러 파일 다운로드 (glob 표현식):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- 여러 파일 업로드 (glob 표현식):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- 원격 서버에서 여러 파일 삭제:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- 원격 서버의 파일 이름 바꾸기:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_파일이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_파일이름</span>
