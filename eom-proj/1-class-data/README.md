# Course webform

This directory holds task1 of the project.

## The structure

There is no heavy use of any algorithm in this project. The layout is, in fact,
basically identical to the sample project, with the fields simply changed.
In this case I decide to use the `Flask-Bootstrap4` package just to be lazy.

I originally thought about collecting multiple courses at once, but doing so
sounds more complicated and will make the data output less flexible.

As with the sample, the project only has one entry point in the form of the `/`
handler. In case of a `GET`, the template is rendered without anything provided,
while in the POST case validation and file writing is done.

A CSV format is used for easier machine manipulation such as in Microsoft Excel.
Note that the Unix dialect of the CSV file format is used due to my familiarity
with it, so I guess it's more of "for easier manipulation by R and whatever
statitians use these days" rather than in Excel.

## Testing

Testing is manually done with the idea of maximizing coverage -- in the code I have
written. In other words, the following cases are tested:

- Plain GET.
- POST with invalid data.
- POST with valid data.

In each case, the "smoke test" is first conducted by inspecting the browser output.
If they look fine, I move on to checking the CSV.

## Further work

It would be really nice to add an `Idempotency-Key`, so that refreshes do not
result in a resubmit. The package [`flask-idempotent`](https://pypi.org/project/Flask-Idempotent/)
provides an almost ideal solution, as it does not require an additional HTTP header.
However, its dependency on Redis means I cannot really trust the testing environment
to do the job. Cooking up an OrderedDict-based datastore and capping it onto the main
function as a "caching" decorator is interesting but possibly a bad idea given the deadline.

## References

1. *Flask-Bootstrap4 Documentation* (c. 2018) <https://flask-bootstrap4.readthedocs.io/en/latest/>)
2. Portions of the Flask-Boostrap4 source code, for figuring out what the
   template thing is all about.

\newpage
