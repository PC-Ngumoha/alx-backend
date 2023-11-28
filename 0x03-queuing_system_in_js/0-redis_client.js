/**
 * @module 0-redis_client.js
 */
import { createClient } from "redis";

async function createRedisClient() {
  try {
    const client = createClient()
    await client.connect();

    console.log('Redis client connected to the server');
  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}

createRedisClient();
