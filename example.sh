#!/bin/sh

read -r -d '' query <<EOF || true
(start_tag (attribute)) @tag-with-attr
(start_tag (attribute) (attribute)) @tag-with-2-attrs
EOF

#export TSQUERY_DEBUG=1
export XDG_DATA_HOME='./tests/xdg-data-home'
set -x
tsquery "$query" ./tests/test.html
tsquery -l html "$query" < ./tests/test.html
