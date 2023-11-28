/**
 * @module 0-redis_client.js
 */
import redis from 'redis';
import { createClient } from "redis";

async function createRedisClient() {
  try {
    const client = createClient()
    await client.connect();

    console.log('Redis client connected to the server');
    await client.hSet('HolbertonSchools', 'Portland', 50, redis.print);
    await client.hSet('HolbertonSchools', 'Seattle', 80, redis.print);
    await client.hSet('HolbertonSchools', 'New York', 20, redis.print);
    await client.hSet('HolbertonSchools', 'Bogota', 20, redis.print);
    await client.hSet('HolbertonSchools', 'Cali', 40, redis.print);
    await client.hSet('HolbertonSchools', 'Paris', 2, redis.print);
    console.log(await client.hGetAll('HolbertonSchools'));
  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}

createRedisClient();
