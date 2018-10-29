
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
