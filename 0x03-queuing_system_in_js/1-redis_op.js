/**
 * @module 0-redis_client.js
 */
import redis from 'redis';
import { createClient } from "redis";

async function createRedisClient() {
  try {
    const client = createClient()
    await client.connect();

    const setNewSchool = async (schoolName, value) => {
      await client.set(schoolName, value, redis.print);
    }

    const displaySchoolValue = async (schoolName) => {
      console.log(await client.get(schoolName));
    }

    console.log('Redis client connected to the server');
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}

createRedisClient();
