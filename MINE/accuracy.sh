cat KGs/*results.json | jq '.[] | .accuracy' | sed -e 's/"//g' -e 's/%//' | grep -v null | awk '{ sum += $1; n++ } END { if (n > 0) print sum / n; }'
