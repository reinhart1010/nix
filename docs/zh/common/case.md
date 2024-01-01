---
layout: page
title: common/case (中文)
description: "case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构。"
content_hash: e9f431cec9c18b9a68283fc70a897eb43477b5c0
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/case.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/case.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/case.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/case.html
    icon: bi bi-globe
tldri18n_status: 2
---
# case

case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构。
更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- 通过字符串字面量判断执行分支：

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入参变量</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符字面量</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w 执行语句块</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l 执行语句块</span>`; ;; esac`

- 搭配通配符进行匹配，判断执行分支：

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入参变量</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[wW]|字符字面量</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w 执行语句块</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[lL]|字符串</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">执行语句块</span>`; ;; *) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "what?"</span>`; ;; esac`
