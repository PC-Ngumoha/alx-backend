/**
 * @module 5-subscriber.js
 * @abstract: Creates a very basic redis subscriber client
 */
import { createClient } from "redis";

async function run() {
  try {
    const client = createClient()
    await client.connect();

    console.log('Redis client connected to the server');

    const listener = async (message, channel) => {
      console.log(message);
      if (message === 'KILL_SERVER') {
        await client.unsubscribe();
        await client.quit();
      }
    };
    const channel = 'holberton school channel';
    await client.subscribe(channel, listener);
  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}

run();
