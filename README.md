#  RedisDB

## Overview

It is a wrapper for a Redis Server.


## Installing RedisDB and Supported Versions

RedisDB is available on PyPI:

`$ python -m pip install wrapper-redis-client`

RedisDB officially supports Python 3.8+.

## Cloning the repository

`$ git clone https://github.com/tatianno/wrapper-redis-client.git`

## Example


```
from wrapper_redis_client import RedisDB

# We set Online: as the default prefix for keys that will be used to persist data.
redis_db = RedisDB(key_prefix='Online:') 

# Clearing previously persisted data.
#
# Obs.: Only data persisted with the keys that have the prefix informed during the instance of the class will be erased.
redis_db.flushall()

# Persisting data with the Online:Test key
redis_db.save('Online:Test', {'test': 1234})

# Retrieving data with the Online:Test key
data = redis_db.get('Online:Test')

# Getting list of keys with prefix informed during class instance
keys_list = redis_db.get_all_keys()

# Erasing data with the Online:Test key
redis.delete('Online:Test')
```