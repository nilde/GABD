
db.TEST.drop()
db.createCollection('TEST')

db.TEST.insert([
	{
		campo1:'test_1',
		campo2:1
	},
	{
		campo1:'test_2',
		campo2:2
	}
	]
   )

use admin
db.createUser(
   {
     user: 'testR', pwd: 'testR',
     roles: [
       { role: 'read', db: 'TEST' }
     ]
   }
);
db.createUser(
   {
     user: 'testRW', pwd: 'testRW',
     roles: [
       { role: 'readWrite', db: 'TEST' }
     ]
   }
);
db.createUser(
   {
     user: 'testA', pwd: 'testA',
     roles: [
       { role: 'userAdmin', db: 'TEST' }
     ]
   }
)
use TEST
db.auth( 'testR', 'testR' )
db.TEST.find()
db.TEST.insertOne( {campo1: "test_3", campo2: 3 } );
db.createCollection("test_ABLE")

use TEST
db.auth( 'testRW', 'testRW' )
db.TEST.find()
db.TEST.insertOne( {campo1: "test_4", campo2: 4 } );
db.createCollection("test_ABLE")

use TEST
db.auth( 'testA', 'testA' )
db.TEST.find()
db.TEST.insertOne( {campo1: "test_5", campo2: 5 } );
db.createCollection("test_ABLE")

