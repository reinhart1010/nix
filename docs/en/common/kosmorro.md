---
layout: page
title: common/kosmorro (English)
description: "Compute the ephemerides and the events for a given date, at a given position on Earth."
content_hash: 070670c76d4bdd98e18746fb95a00edf0af406e3
related_topics:
  - title: français version
    url: /fr/common/kosmorro.html
    icon: bi bi-globe
---
# kosmorro

Compute the ephemerides and the events for a given date, at a given position on Earth.
More information: <http://kosmorro.space>.

- Get ephemerides for Paris, France:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>

- Get ephemerides for Paris, France, in the UTC+2 timezone:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --timezone=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Get ephemerides for Paris, France, on June 9th, 2020:

`kosmorro --latitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">48.7996</span>` --longitude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.3511</span>` --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-06-09</span>

- Generate a PDF (note: TeXLive must be installed):

`kosmorro --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
