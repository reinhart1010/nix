---
layout: page
title: common/arthas-watch (English)
description: "Method invoke data observation."
content_hash: aaecdab1b37d52325ab5c45e1e3e3c83adbfd509
last_modified_at: 2025-03-02
related_topics:
  - title: 中文 version
    url: /zh/common/arthas-watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas-watch

Method invoke data observation.
See also: `arthas`, `arthas-trace`.
More information: <https://arthas.aliyun.com/en/doc/watch.html>.

- Observe the first parameter and return value of method, and expand the nested attributes of the object to 4 levels:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[0],returnObj }'</span>` -x 4`

- When the value of the first parameter of the method is 5, the second parameter and return value are output, and the object is expanded 4 layers:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[1],returnObj }'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'"5".equals(params[0])'</span>` -x 4`

- When the method returns or an exception occurs, observe the count property of the second parameter:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{ params[1].count }'</span>` -e -s`
