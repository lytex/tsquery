# TSQuery

Run [Tree Sitter](https://tree-sitter.github.io) queries from the command line.

Forked from [https://git.sr.ht/~wintershadows/tsquery] to write only the text from the code that matches the query

To write only the code add a `--only-code` argument


# Installation

```shell
pip install tsquery
```

For a general-purpose installation, [Pipx](https://pipxproject.github.io/pipx/installation/) is highly recommended:

```shell
pipx install tsquery
```

# Usage

Parsers (`.so` files) should be installed somewhere in `$XDG_DATA_HOME/tree-sitter/parsers`
or `$XDG_DATA_DIRS/tree-sitter/parsers`.
Use the [official Tree Sitter CLI tool](https://tree-sitter.github.io/tree-sitter/creating-parsers#tool-overview)
to compile a grammar to parser source.

For example, this command prints the names of functions defined in a toy Python
program:

```shell
# Write a toy Python program
cat > example.py <<EOF
def baz():
    return 1

def foo(bar):
    if bar:
        baz()
EOF

# Run a query against it
tsquery '(function_definition name: (identifier) @func.name)' example.py
```

See also `example.sh` in this repository.
