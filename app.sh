while true
do
	curl -X POST -H "Content-Type: application/json" -d "{\"rate\": "$((60 + RANDOM % 120))"}"   "$1/raspberry/patient/$2"
	sleep 30
done
