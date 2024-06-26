---
layout: page
title: linux/dockerd (العربية)
description: "هي عملية مستمرة تعمل في الخلفية تبدأها لتتحكم في حاويات الدوكر."
content_hash: 681929975d94b1eb6a4ead5118a62a4141196081
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/linux/dockerd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dockerd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dockerd

هي عملية مستمرة تعمل في الخلفية تبدأها لتتحكم في حاويات الدوكر.
لمزيد من التفاصيل: <https://docs.docker.com/reference/cli/dockerd/>.

- قم بتشغيل دوكر في الخلفية:

`dockerd`

- قم بتشغيل دوكر في الخلفية واجعله يستمع علي منفذ معين (يونكس وبروتوكول ضبط الإرسال):

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/tmp.sock</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- قم بتشغيل دوكر في الخلفية برقم عملية معين:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pid_file</span>

- قم بتشغيل دوكر في وضع التصحيح واكتشاف الأخطاء:

`dockerd --debug`

- قم بتشغيل دوكر وحدد له مستوي سجل معين:

`dockerd --log-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
