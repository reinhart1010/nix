---
layout: page
title: windows/choice (English)
description: "Prompts the user to select one item from a list of single-character choices in a batch program, and then returns the index of the selected choice."
content_hash: 2729d9891dde1991bf85487c18ccf8fd257456e7
---
# choice

Prompts the user to select one item from a list of single-character choices in a batch program, and then returns the index of the selected choice.
If used without parameters, choice displays the default choices Y and N.
More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/choice>.

- A,B and C as list of choices to be used:

`choice /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ABC</span>

- Use the default [Y,N] list of choices:

`choice`

- Specify that the choices are case-sensitive:

`choice /CS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AaBb</span>

- Specify the number of seconds to pause before using the default choice specified by `/d`:

`choice /C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AaBb</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b</span>

- Specify a message to display before the list of choices. If `/m` is not specified, only the choice prompt is displayed:

`choice /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>` /C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ABC</span>

- Display help message:

`choice /?`
