---
layout: page
title: windows/chromium (English)
description: "Open-source web browser principally developed and maintained by Google."
content_hash: b4f7bd07fa7d34b25ea53cf0451dbca8a3cfce62
last_modified_at: 2024-10-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/chromium.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chromium

Open-source web browser principally developed and maintained by Google.
Note: You may need to replace the `chromium` command with your desired web browser, such as `brave`, `google-chrome`, `microsoft-edge`/`msedge`, `opera`, or `vivaldi`.
More information: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Open a specific URL or file:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com|path/to/file.html</span>

- Open in incognito mode (use `--inprivate` for Microsoft Edge):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chromium --incognito|msedge --inprivate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

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
