#!/bin/sh

read -r -d '' query <<SCM || True
(start_tag (attribute)) @tag-with-attr
(start_tag (attribute) (attribute)) @tag-with-2-attrs
SCM

set -x
tsquery "$query" 'test/test.html'
tsquery -l html "$query" < 'test/test.html'
