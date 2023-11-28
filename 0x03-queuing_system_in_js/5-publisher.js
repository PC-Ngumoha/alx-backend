/**
 * @module 5-publisher.js
 * @abstract: Creates a very basic redis publisher client
 */
import { createClient } from "redis";

async function run() {
  try {
    const client = createClient()
    await client.connect();

    console.log('Redis client connected to the server');

    const publishMessage = (message, time) => {
      const channel = 'holberton school channel';
      setTimeout(async () => {
        console.log(`About to send ${message}`);
        await client.publish(channel, message);
      }, time);
    };

    publishMessage("Holberton Student #1 starts course", 100);
    publishMessage("Holberton Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("Holberton Student #3 starts course", 400);
  } catch (err) {
    console.log(`Redis client not connected to the server: ${err}`);
  }
}

run();
