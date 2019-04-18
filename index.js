const Bot = require('./bot');
const Crawler = require('./crawler');
const config = require('./config.json');
const crawlMethods = require('./crawl-methods');

const bot = new Bot(config.irc);

console.log('hi');
bot.connect().then(() => {
  const crawlers = config.crawlers.map(options => {
    try {
      const crawlerOptions = options.crawler || {};
      const postOptions = options.post || {};
      return new Crawler(
        options.name,
        crawlMethods[crawlerOptions.methodName],
        generateSender(postOptions)(bot),
        crawlerOptions
      );
    } catch (err) {
      console.error(`${options.name}: ${err.message}`)
    }
  }).filter(_ => _);

  crawlers.map(crawler => crawler.run());
}).catch(console.error);

function generateSender(options) {
  return function (bot) {
    return function (item) {
      const message = `${options.prefix}| ${item.title} ${item.link} (${item.date})`;
      options.channels.map(channel => {
        bot.send(channel, message);
      });
      console.log(`${new Date()}:: ${message}`);
    }
  }
}
