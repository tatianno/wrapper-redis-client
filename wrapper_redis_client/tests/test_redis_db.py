from unittest import TestCase
from wrapper_redis_client import RedisDB
from wrapper_redis_client.exceptions import InvalidKey




class RedisDBTestCase(TestCase):

    def setUp(self) -> None:
        self.redis_db = RedisDB('Online:')
        self.redis_db.flushall()
        return super().setUp()
    
    def test_validate_key(self):
        self.assertTrue(self.redis_db.validate_key('Online:Teste'))
        
        with self.assertRaises(InvalidKey):
            self.redis_db.validate_key('Teste:')
    
    def test_crud_redis(self):
        self.redis_db.save('Online:Teste', {'teste': 'teste'})
        self.assertTrue(self.redis_db.exists('Online:Teste'))
        self.assertDictEqual(
            {'teste': 'teste'},
            self.redis_db.get('Online:Teste')
        )
        self.redis_db.delete('Online:Teste')
        self.assertFalse(self.redis_db.exists('Online:Teste'))
    
    def test_get_all_keys(self):
        self.assertEqual(len(self.redis_db.get_all_keys()), 0)
        self.redis_db.save('Online:Teste1', {'teste': 'teste'})
        self.redis_db.save('Online:Teste2', {'teste': 'teste'})
        self.assertEqual(len(self.redis_db.get_all_keys()), 2)
        self.redis_db.flushall()
        self.assertEqual(len(self.redis_db.get_all_keys()), 0)