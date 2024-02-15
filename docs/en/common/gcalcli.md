---
layout: page
title: common/gcalcli (English)
description: "Interact with Google Calendar."
content_hash: 3ae1c45f2484db84999824bddacc17de1f5a9470
last_modified_at: 2024-02-15
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gcalcli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcalcli

Interact with Google Calendar.
Requests Google API authorization upon first launch.
More information: <https://github.com/insanum/gcalcli>.

- List your events for all your calendars over the next 7 days:

`gcalcli agenda`

- Show events starting from or between specific dates (also takes relative dates e.g. "tomorrow"):

`gcalcli agenda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>`]`

- List events from a specific calendar:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">calendar_name</span>` agenda`

- Display an ASCII calendar of events by week:

`gcalcli calw`

- Display an ASCII calendar of events for a month:

`gcalcli calm`

- Quick-add an event to your calendar:

`gcalcli --calendar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">calendar_name</span>` quick "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mm/dd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HH:MM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_name</span>`"`

- Add an event to calendar. Triggers interactive prompt:

`gcalcli --calendar "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">calendar_name</span>`" add`
