---
layout: page
title: common/chromium (English)
description: "Open-source web browser principally developed and maintained by Google."
content_hash: d600985323b9a63c11efa2fe11cf66cecc0aabd7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chromium.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

Open-source web browser principally developed and maintained by Google.
More information: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open a specific URL or file:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|path/to/file.html</span>

- Open in incognito mode:

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in a new window:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open in application mode (without toolbars, URL bar, buttons, etc.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Use a proxy server:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Open with a custom profile directory:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Open without CORS validation (useful to test an API):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --disable-web-security`

- Open with a DevTools window for each tab opened:

`chromium --auto-open-devtools-for-tabs`
