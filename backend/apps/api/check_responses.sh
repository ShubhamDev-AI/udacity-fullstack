
printf '\n'
printf '\n'

curl -X GET http://localhost:5000/readHello

printf '\n'

curl -X POST http://localhost:5000/createHello

printf '\n'

curl -X PUT http://localhost:5000/updateHello

printf '\n'

curl -X DELETE http://localhost:5000/deleteHello

printf '\n'