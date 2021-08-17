TODO, not MVC, not even GUI
===========================

Mingye "Too tired to Microsoft Word" Wang, 2021.

Doing GUI is too much of a drain on my sanity.

I don't see much point in doing MVC on CLI, since users are not going to
want to have an automatic "repaint" anyways. Drawing with TUI might be less
sanity-consuming than a Tkinter GUI, but then I'd have to ship `ncurses`.

Wasn't `ed(1)` the "standard editor"?  Yeah, let's do that.


The core
--------

This project centers around the TODO list as defined in the model.
We first define the `Item` as having four component: the UUID, the title, the body,
and a boolean flag for whether it is checked.

The `TODOList` is then defined as containing a dict of `Items` mapping from the UUID
(as an optimization assuming a fully-featured GUI), a list of action "hooks" again
serving the now-abandoned MVC structure, and finally a string `key` specifying what
file to load or save from.

As with project #1, the standard RFC CSV format (`dialect='unix'`) is used for saving.


Interaction
-----------

The CLI is a loop using `input` to read commands. For basic quoting ability, such
as for writing titles with spaces (`add "Reheat pizza at 3pm"`), the builtin `shlex`
library is used to parse the input into a list.

The design of the CLI is nowhere near good. Things that heavily impact usability include:

* Lack of tab completion. I know it's somewhere in the builtin `readline` module.
* Awful help messages. Can be better written.
* No multi-named commands (e.g. abbreviating `help` as `?`) due to the way `help` is
  implemented.  Can be solved by using a separate `ALIASES` dictionary.
* `search` result are not highlighting matches.

Most commands are wrappers around what's available in the `TODOList` object. The exceptions
are:

* `search`, which performs a linear search;
* `edit`, which dumps an entry to a text file, calls the system's text editor,
  and then reads back when done.  Probably the only thing I am proud of here.

References
----------

1. *TodoMVC*, <https://todomvc.com/>. The original intention was to mimic it in
   Python, but I ended up only roughly taking the Model design.
2. *Python 3.9.6 documentation*, specifically the `itertools` module for the `nth`
   function, the `re` module for usage, and the `tempfile` module for a replacement
   of `mktemp`.
