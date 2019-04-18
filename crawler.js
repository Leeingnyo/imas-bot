function Crawler(name, process, postprocess, options) {
  if (!name) throw Error('Crawler must have name');
  this._name = name;
  if (typeof process !== 'function') throw Error('Crawler must have process method');
  this._method = process;

  this._options = options || {};
  this._options.period = this._options.period || 60;
  this._options.maximum = this._options.maximum || 50;

  this._postprocess = typeof postprocess === 'function' ? postprocess : console.log;

  this._backup = [];
}

Crawler.prototype.crawl = async function () {
  const recentItems = await this._method(this._options);
  if (this._backup.length === 0) {
    // initialize
    this._backup.push(...recentItems);
    return;
  }
  const newItems = recentItems.filter(item => !this._backup.find(backup => backup.link === item.link));

  newItems.slice().reverse().map(item => {
    this._postprocess(item);
  });

  this._backup.unshift(...newItems);
  while (this._backup.length > this._options.maximum) this._backup.pop();
}

Crawler.prototype.run = function () {
  console.log(`${this._name} starts`);
  try {
    this.crawl();
  } catch (err) {
    console.error(err);
  }
  return setInterval(() => {
    try {
      this.crawl();
    } catch (err) {
      console.error(err);
    }
  }, this._options.period * 1000);
}

module.exports = Crawler;
