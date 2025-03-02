---
layout: page
title: common/arthas-watch (中文)
description: "函数执行数据观测。"
content_hash: 4cbac1ea524267815733b459ea747ee84ce6ef67
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/arthas-watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas-watch

函数执行数据观测。
另见 `arthas`, `arthas-trace`.
更多信息：<https://arthas.aliyun.com/en/doc/watch.html>.

- 在方法调用后观察，显示第一个参数和返回值，展开嵌套对象的 4 层：

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[0],returnObj }'</span>` -x 4`

- 在方法调用后观测，当第一个参数的值是 5 时，显示第二个参数和返回值，展开嵌套对象的 4 层：

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[1],returnObj }'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'"5".equals(params[0])'</span>` -x 4`

- 在方法返回和异常后观测，显示第二个参数的 count 属性：

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[1].count }'</span>` -e -s`
