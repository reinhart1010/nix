---
layout: page
title: common/xmlstarlet (한국어)
description: "명령줄 XML/XSLT 도구 모음."
content_hash: afe7095597476be92f59e3e6ef625ed36e3e4d76
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/xmlstarlet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xmlstarlet

명령줄 XML/XSLT 도구 모음.
참고: XPath를 알아야 할 수도 있습니다: <https://developer.mozilla.org/en-US/docs/Web/XPath>.
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- XML 문서를 포맷하여 `stdout`에 출력:

`xmlstarlet format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>

- XML 문서를 `stdin`에서 파이프로 입력할 수도 있음:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일.xml</span>` | xmlstarlet format`

- 주어진 XPath와 일치하는 모든 노드 출력:

`xmlstarlet select --template --copy-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>

- 일치하는 모든 노드에 속성을 삽입하고 `stdout`에 출력 (원본 파일은 변경되지 않음):

`xmlstarlet edit --insert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` --type attr --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>

- 일치하는 모든 노드의 값을 직접 업데이트 (원본 파일이 변경됨):

`xmlstarlet edit --inplace --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.xml</span>

- 일치하는 모든 노드 삭제 (원본 파일이 변경됨):

`xmlstarlet edit --inplace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.xml</span>

- 주어진 문자열의 특수 XML 문자를 이스케이프 또는 언이스케이프:

`xmlstarlet [un]escape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 주어진 디렉토리를 XML로 나열 (인수를 생략하면 현재 디렉토리를 나열):

`xmlstarlet ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
