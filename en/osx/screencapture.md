---
layout: page
title: osx/screencapture (English)
description: "Utility to take screenshots and screen recordings."
content_hash: f0d6f699c697381c5f577e451c31493481d860e1
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/osx/screencapture.html
    icon: bi bi-globe
---
# screencapture

Utility to take screenshots and screen recordings.
More information: <https://ss64.com/osx/screencapture.html>.

- Take a screenshot and save it to a file:

`screencapture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Take a screenshot including the mouse cursor:

`screencapture -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Take a screenshot and open it in Preview, instead of saving:

`screencapture -P`

- Take a screenshot of a selected rectangular area:

`screencapture -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Take a screenshot after a delay:

`screencapture -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.png</span>

- Make a screen recording and save it to a file:

`screencapture -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp4</span>
