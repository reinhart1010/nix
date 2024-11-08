---
layout: page
title: common/protoc (한국어)
description: "Google Protobuf `.proto` 파일을 파싱하고 지정된 언어로 출력을 생성."
content_hash: 13b199727223ec17c5cdb628470119377e91a3bb
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/protoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/protoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protoc

Google Protobuf `.proto` 파일을 파싱하고 지정된 언어로 출력을 생성.
더 많은 정보: <https://developers.google.com/protocol-buffers>.

- `.proto` 파일에서 Python 코드를 생성:

`protoc --python_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.proto</span>

- 다른 `.proto` 파일을 가져오는 `.proto` 파일에서 Java 코드를 생성:

`protoc --java_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` --proto_path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/가져오기_탐색_경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.proto</span>

- 여러 언어에 대한 코드 생성:

`protoc --csharp_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c#_출력_폴더</span>` --js_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/js_출력_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일.proto</span>
