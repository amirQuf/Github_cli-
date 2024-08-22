username=$1

echo "$username"

url='https://api.github.com/users/'$1'/events'

echo "$url"


response=curl $url

echo "Output:"
