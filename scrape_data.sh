#! /bin/bash

# Display help
usage() {
cat << EOF
USAGE:
   scrape_data [query]
OPTIONS:
    -l : limit
    -q : query
    -b : beginning date
EXAMPLE:
    bash scrape_data.sh -q=sports -l=10000 -b=2019-05-01
EOF
}

if [[ "$#" -eq 0 ]]; then
    usage; exit
fi

for i in "$@"
do

case $i in
    -l=*|--limit=*)
    LIMIT="${i#*=}"
    shift
    ;;
    -q=*|--query=*)
    QUERY="${i#*=}"
    shift
    ;;
    -b=*|--beg=*)
    BD="${i#*=}"
    shift
    ;;
    *)
    echo "invalid set of arguments"
esac
done

# echo "${QUERY}"
# echo "${LIMIT}"

twitterscraper $QUERY --limit $LIMIT --lang en --output ~/twitter_data/$(date +%d%B_%H%M).json -bd $BD -ed $(date +%Y-%m-%d)
