---
layout: page
title: linux/dockerd (العربية)
description: "هي عملية مستمرة تعمل في الخلفية تبدأها لتتحكم في حاويات الدوكر."
content_hash: c32469f9f49ac9be87d146b0d433fba607214bcb
related_topics:
  - title: English version
    url: /en/linux/dockerd.html
    icon: bi bi-globe
---
# dockerd

هي عملية مستمرة تعمل في الخلفية تبدأها لتتحكم في حاويات الدوكر.
لمزيد من التفاصيل: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- قم بتشغيل دوكر في الخلفية:

`dockerd`

- قم بتشغيل دوكر في الخلفية واجعله يستمع علي منفذ معين (يونكس وبروتوكول ضبط الإرسال):

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">السوكيت/إلي/المسار</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- قم بتشغيل دوكر في الخلفية برقم عملية معين:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ملف_رقم_العملية/إلي/المسار</span>

- قم بتشغيل دوكر في وضع التصحيح واكتشاف الأخطاء:

`dockerd --debug`

- قم بتشغيل دوكر وحدد له مستوي سجل معين:

`dockerd --log-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
