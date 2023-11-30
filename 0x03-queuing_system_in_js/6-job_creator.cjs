/**
 * @module 6-job_creator.cjs
 */
const kue = require('kue');

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '+2347089699162',
  message: 'This is my main phone number, you can use it to call me',
});

job.save(err => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
