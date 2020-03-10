Microsoft Windows [Version 10.0.18363.476]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\ADAM-PC>cd C:\Program Files\MongoDB\Server\4.2\bin

C:\Program Files\MongoDB\Server\4.2\bin>mongod --dbpath C:\data\db





Microsoft Windows [Version 10.0.18363.476]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\ADAM-PC>

C:\Program Files\MongoDB\Server\4.2\bin>mongo
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("1c6a1908-c8bf-49c6-8393-4dc7b4eca545") }
MongoDB server version: 4.2.1
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
Server has startup warnings:
2019-11-25T09:49:13.003+0700 I  CONTROL  [initandlisten]
2019-11-25T09:49:13.003+0700 I  CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-11-25T09:49:13.003+0700 I  CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-11-25T09:49:13.004+0700 I  CONTROL  [initandlisten]
2019-11-25T09:49:13.005+0700 I  CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2019-11-25T09:49:13.005+0700 I  CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2019-11-25T09:49:13.006+0700 I  CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2019-11-25T09:49:13.006+0700 I  CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2019-11-25T09:49:13.007+0700 I  CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2019-11-25T09:49:13.008+0700 I  CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2019-11-25T09:49:13.008+0700 I  CONTROL  [initandlisten]
---
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
---

> mongo dbs
2019-11-25T09:57:54.273+0700 E  QUERY    [js] uncaught exception: SyntaxError: unexpected token: identifier :
@(shell):1:6
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> show databases
admin   0.000GB
config  0.000GB
local   0.000GB
> db
test
> use tokoonline
switched to db tokoonline
> db.createCollection('pelapak');
{ "ok" : 1 }
> show dbs
admin       0.000GB
config      0.000GB
local       0.000GB
tokoonline  0.000GB
> show collections
pelapak
> db.pelapak.drop()
true
> db
tokoonline
> show collections;
> db
tokoonline
> use tokoonline
switched to db tokoonline
> db.dropDatabase()
{ "dropped" : "tokoonline", "ok" : 1 }
> show db
2019-11-25T10:36:21.684+0700 E  QUERY    [js] uncaught exception: Error: don't know how to show [db] :
shellHelper.show@src/mongo/shell/utils.js:1139:11
shellHelper@src/mongo/shell/utils.js:790:15
@(shellhelp2):1:1
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> db.crateUser({
... user:"root",
... pwd:'363636'
... roles:['dbAdmin','readWrite']
... }]
2019-11-25T10:38:48.446+0700 E  QUERY    [js] uncaught exception: SyntaxError: missing } after property list :
@(shell):4:0
> db.createuser({
... user:"root",
... pwd:'363636',
... roles:['dbAdmin','readWrite']
... })
2019-11-25T10:40:05.272+0700 E  QUERY    [js] uncaught exception: TypeError: db.createuser is not a function :
@(shell):1:1
> show user;
2019-11-25T10:41:00.102+0700 E  QUERY    [js] uncaught exception: Error: don't know how to show [user] :
shellHelper.show@src/mongo/shell/utils.js:1139:11
shellHelper@src/mongo/shell/utils.js:790:15
@(shellhelp2):1:1
> db.createuser({
... user:"adam",
... pwd:'12345'
... roles:['dbAdmin','readWrite']
... }]
2019-11-25T10:43:41.000+0700 E  QUERY    [js] uncaught exception: SyntaxError: missing } after property list :
@(shell):4:0
> db.createuser({
... user:'adam',
... pwd:'123456',
... roles:['dbAdmin','readWrite']
... }]
2019-11-25T10:45:37.322+0700 E  QUERY    [js] uncaught exception: SyntaxError: missing ) after argument list :
@(shell):5:1
> db.createuser({
... user:'adam',
... pwd:'123456',
... roles:['dbAdmin','readWrite']
... })
2019-11-25T10:46:58.964+0700 E  QUERY    [js] uncaught exception: TypeError: db.createuser is not a function :
@(shell):1:1
> db.createUser({
... user:'adam',
... pwd:'123456',
... roles:['dbAdmin','readWrite']
... })
Successfully added user: { "user" : "adam", "roles" : [ "dbAdmin", "readWrite" ] }
> db.createCollection('seller')
{ "ok" : 1 }
> show collections
seller
> db.seller.insert({nama:'Andi',usia:22})
WriteResult({ "nInserted" : 1 })
> db.seller.insert([
... {nama:'Budi',usia:23},
... {nama:'Caca',usia:24},
... ])
BulkWriteResult({
        "writeErrors" : [ ],
        "writeConcernErrors" : [ ],
        "nInserted" : 2,
        "nUpserted" : 0,
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
})
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "usia" : 22
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24
}
> db.seller.insert(
... {nama:'Deni',kota:'Jakarta',job:'PNS'}
... )
WriteResult({ "nInserted" : 1 })
> show Collection
2019-11-25T10:54:06.023+0700 E  QUERY    [js] uncaught exception: Error: don't know how to show [Collection] :
shellHelper.show@src/mongo/shell/utils.js:1139:11
shellHelper@src/mongo/shell/utils.js:790:15
@(shellhelp2):1:1
> show collections
seller
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "usia" : 22
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24
}
{
        "_id" : ObjectId("5ddb5048590a39ae0553d002"),
        "nama" : "Deni",
        "kota" : "Jakarta",
        "job" : "PNS"
}
> db.seller.remove({job:'PNS'});
WriteResult({ "nRemoved" : 1 })
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "usia" : 22
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24
}
> db.seller.update(
... {nama:'Andi'},
... {nama:'Andi', kota:'jakarta'})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "kota" : "jakarta"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24
}
> db.seller.update(
... {nama:'Andi'},
... {$set:{kota:'cimahi'}});
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "kota" : "cimahi"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24
}
> db.seller.updateMany({},{$set: {nationality:'Indonesia}});
2019-11-25T11:11:25.759+0700 E  QUERY    [js] uncaught exception: SyntaxError: '' literal not terminated before end of script :
@(shell):1:58
> db.seller.updateMany({},{$set: {nationality:'Indonesia}}),
2019-11-25T11:11:33.847+0700 E  QUERY    [js] uncaught exception: SyntaxError: '' literal not terminated before end of script :
@(shell):1:58
> db.seller.updateMany({},{$set: {nationality:'Indonesia}})
2019-11-25T11:11:49.130+0700 E  QUERY    [js] uncaught exception: SyntaxError: '' literal not terminated before end of script :
@(shell):1:57
> db.seller.updateMany({},{$set: {nationality:'Indonesia}})
2019-11-25T11:13:32.487+0700 E  QUERY    [js] uncaught exception: SyntaxError: '' literal not terminated before end of script :
@(shell):1:57
> db.seller.updateMany({},{$set: {nationality:'Indonesia'}})
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "nama" : "Andi",
        "kota" : "cimahi",
        "nationality" : "Indonesia"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "nama" : "Budi",
        "usia" : 23,
        "nationality" : "Indonesia"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "nama" : "Caca",
        "usia" : 24,
        "nationality" : "Indonesia"
}
> db.seller.updateMany(
... {},
... {$rename:{'nama':'name'}}
... )
{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }
> db.seller.find().pretty()
{
        "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"),
        "kota" : "cimahi",
        "nationality" : "Indonesia",
        "name" : "Andi"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d000"),
        "usia" : 23,
        "nationality" : "Indonesia",
        "name" : "Budi"
}
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "usia" : 24,
        "nationality" : "Indonesia",
        "name" : "Caca"
}
> db.seller.find({name:'Andi'})
{ "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"), "kota" : "cimahi", "nationality" : "Indonesia", "name" : "Andi" }
> nationality : indonesia and usi >= 25
2019-11-25T11:40:51.081+0700 E  QUERY    [js] uncaught exception: SyntaxError: unexpected token: identifier :
@(shell):1:24
> nationality : indonesia and usi >= 23
2019-11-25T11:41:04.636+0700 E  QUERY    [js] uncaught exception: SyntaxError: unexpected token: identifier :
@(shell):1:24
> nationality : Indonesia and usi >= 23
2019-11-25T11:41:19.171+0700 E  QUERY    [js] uncaught exception: SyntaxError: unexpected token: identifier :
@(shell):1:24
> nationality : Indonesia and usia >= 23
2019-11-25T11:41:23.669+0700 E  QUERY    [js] uncaught exception: SyntaxError: unexpected token: identifier :
@(shell):1:24
> db.seller.find(
... {$and: [{nationality:'indonesia'}, {usia:{$gte:25}}]}
... ).pretty()
> db.seller.find( {$and: [{nationality:'indonesia'}, {usia:{$gte:23}}]} ).pretty()
> db.seller.insert(
... {
... nama:'Ali', address:{
... city:'Cimahi', zipcode:'12345', gps:[
... {latitude: 1234}, {longitude: 5678}
... ]
... }})
WriteResult({ "nInserted" : 1 })
> db.seller.find({nama:'ali'}).pretty()
> db.seller.find({nama:"ali"}).pretty()
> db.seller.find({nama:'caca'}).pretty()
> db.seller.find({name:'caca'}).pretty()
> db.seller.find({name:'Caca'}).pretty()
{
        "_id" : ObjectId("5ddb4fc6590a39ae0553d001"),
        "usia" : 24,
        "nationality" : "Indonesia",
        "name" : "Caca"
}
> db.seller.find({nama:'Ali'}).pretty()
{
        "_id" : ObjectId("5ddb5cd9590a39ae0553d003"),
        "nama" : "Ali",
        "address" : {
                "city" : "Cimahi",
                "zipcode" : "12345",
                "gps" : [
                        {
                                "latitude" : 1234
                        },
                        {
                                "longitude" : 5678
                        }
                ]
        }
}
> db.seller.find().sort({usia:1})
{ "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"), "kota" : "cimahi", "nationality" : "Indonesia", "name" : "Andi" }
{ "_id" : ObjectId("5ddb5cd9590a39ae0553d003"), "nama" : "Ali", "address" : { "city" : "Cimahi", "zipcode" : "12345", "gps" : [ { "latitude" : 1234 }, { "longitude" : 5678 } ] } }
{ "_id" : ObjectId("5ddb4fc6590a39ae0553d000"), "usia" : 23, "nationality" : "Indonesia", "name" : "Budi" }
{ "_id" : ObjectId("5ddb4fc6590a39ae0553d001"), "usia" : 24, "nationality" : "Indonesia", "name" : "Caca" }
> db.seller.find().sort({usia:-1})
{ "_id" : ObjectId("5ddb4fc6590a39ae0553d001"), "usia" : 24, "nationality" : "Indonesia", "name" : "Caca" }
{ "_id" : ObjectId("5ddb4fc6590a39ae0553d000"), "usia" : 23, "nationality" : "Indonesia", "name" : "Budi" }
{ "_id" : ObjectId("5ddb4f6c590a39ae0553cfff"), "kota" : "cimahi", "nationality" : "Indonesia", "name" : "Andi" }
{ "_id" : ObjectId("5ddb5cd9590a39ae0553d003"), "nama" : "Ali", "address" : { "city" : "Cimahi", "zipcode" : "12345", "gps" : [ { "latitude" : 1234 }, { "longitude" : 5678 } ] } }
>




C:\Program Files\MongoDB\Server\4.2\bin>mongoimport --db resto --collection resto --file restaurants.json --jsonArray
2019-11-25T12:28:30.490+0700    connected to: mongodb://localhost/
2019-11-25T12:28:30.492+0700    Failed: error reading separator after document #1: bad JSON array format - found no opening bracket '[' in input source
2019-11-25T12:28:30.492+0700    0 document(s) imported successfully. 0 document(s) failed to import.

C:\Program Files\MongoDB\Server\4.2\bin>mongoimport --db resto --collection resto --file restaurants.json --jsonArrayMicrosoft Windows [Version 10.0.18363.476]
2019-11-25T12:29:51.344+0700    error parsing command line options: unknown option "jsonArrayMicrosoft"
2019-11-25T12:29:51.345+0700    try 'mongoimport --help' for more information

C:\Program Files\MongoDB\Server\4.2\bin>(c) 2019 Microsoft Corporation. All rights reserved.
2019 was unexpected at this time.

C:\Program Files\MongoDB\Server\4.2\bin>
C:\Program Files\MongoDB\Server\4.2\bin>C:\Users\ADAM-PC>cd C:\Program Files\MongoDB\Server\4.2\bin
Access is denied.

C:\Program Files\MongoDB\Server\4.2\bin>
C:\Program Files\MongoDB\Server\4.2\bin>C:\Program Files\MongoDB\Server\4.2\bin>mongod --dbpath C:\data\db
