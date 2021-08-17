Custom project
==============

At first I thought I don't have the patience to call a bunch of draw
commands and save the `id` for later deletion, so I looked for easier
wrapped libraries like `PySimpleGUI`.

Then it turned out I can't even make it through the documentation without
screaming about bad formatting.

And that's on top of me having a "nice" Python 3 installation without Tk
and the system's builtin "not nice" one having Tk.

I am sorry.  I am too spolied by React.


Original text
-------------

I don't want to write much this time, so I decide to fall back on the
"hello world" of JavaScript frameworks -- TodoMVC for inspiration. This,
if it runs at all, is a TODO manager with a search functionality.

I try to be fashionable to split the code into the MVC pattern, so that
the UI (View), in theory, does not directly modify the data (Model), but
does so via the Controller.


