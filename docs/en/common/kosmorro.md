---
layout: page
title: common/kosmorro (English)
description: "Compute the ephemerides and the events for a date at a position on Earth."
content_hash: f095c7ed09940788ce5849ed3ec6a96414916431
last_modified_at: 2024-10-12
related_topics:
  - title: français version
    url: /fr/common/kosmorro.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kosmorro

Compute the ephemerides and the events for a date at a position on Earth.
More information: <https://kosmorro.space>.

- Get ephemerides for Paris, France:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>

- Get ephemerides for Paris, France, in the UTC+2 timezone:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --timezone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Get ephemerides for Paris, France, on June 9th, 2020:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-06-09</span>

- Generate a PDF (Note: TeXLive must be installed):

`kosmorro --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
