---
layout: page
title: common/case (中文)
description: "case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构。"
content_hash: 2a1b90e8b3475538e89669b0ef4fb11dac5ca266
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/case.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/case.html
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

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$计数规则</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字数</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>` ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">行数</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>` ;; esac`

- 使用 | 组合匹配模式，使用 * 作为默认匹配：

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$计数规则</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[wW]|字数</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>` ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[lL]|行数</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>` ;; *) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "无效输入"</span>` ;; esac`

- 允许匹配多个模式：

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$动物</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">猫</span>`) echo "这是一只猫" ;;& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">猫|狗</span>`) echo "这是一只猫或狗" ;;& *) echo "其他动物" ;; esac`

- 继续执行下一个模式的命令而不检查模式：

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$动物</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">猫</span>`) echo "这是一只猫" ;& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">狗</span>`) echo "这是一只狗或猫的匹配结果" ;& *) echo "其他动物" ;; esac`
