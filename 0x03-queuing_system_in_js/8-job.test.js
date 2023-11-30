/**
 * @module 8-job.test.js
 */
import { expect } from 'chai';
import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('createPushNotificationsJobs', function() {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('Should displays an error message when jobs is not an array', function() {
    const jobs = {};
    expect(createPushNotificationsJobs.bind(jobs, queue)).to.throw('Jobs is not an array');
  });

  it ('Should create three new jobs to the queue', function() {
    const jobs = [
      {
        phoneNumber: '4153818782',
        message: 'This is the code 4321 to verify your account'
      },
      {
        phoneNumber: '4154318781',
        message: 'This is the code 4562 to verify your account'
      },
      {
        phoneNumber: '4151218782',
        message: 'This is the code 4321 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(3);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
