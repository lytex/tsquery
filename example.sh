#!/bin/sh

export XDG_DATA_HOME='./tests/xdg-data-home'
#export TSQUERY_DEBUG=1


# HTML

read -r -d '' html_query <<'EOF' || true
(element (element (text))) @elem-with-text
(start_tag (attribute (quoted_attribute_value))) @tag-with-quoted-attr
(start_tag (attribute) (attribute)) @tag-with-2-attrs
EOF

tsquery "$html_query" ./tests/test.html
tsquery -l html "$html_query" < ./tests/test.html


# Python

read -r -d '' python_query <<'EOF' || true
(function_definition
  name: (identifier) @func.name)
EOF

tsquery -l python "$python_query" <<'EOF'
def baz():
    return 1

def foo(bar):
    if bar:
        baz()
EOF
