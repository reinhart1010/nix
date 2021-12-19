---
layout: page
title: common/gh-screensaver (English)
description: "Extension for GitHub CLI that runs animated terminal screensavers."
content_hash: 9ccddf0bffeb4fde6c1b5a0cb4a497acc764b674
---
# gh screensaver

Extension for GitHub CLI that runs animated terminal screensavers.
See also: `gh extension`.
More information: <https://github.com/vilmibm/gh-screensaver>.

- Run a random screensaver:

`gh screensaver`

- Run a specific screensaver:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fireworks|marquee|pipes|pollock|starfield</span>

- Run the "marquee" screensaver with a specific text and font:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">marquee</span>` -- --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" --font=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">font_name</span>

- Run the "starfield" screensaver with a specific density and speed:

`gh screensaver --saver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">starfield</span>` -- --density `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- List available screensavers:

`gh screensaver --list`
