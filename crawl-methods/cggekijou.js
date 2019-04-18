const request = require('request-promise-native');
const cheerio = require('cheerio');

module.exports = async function () {
  const name = 'cggekijou';
  const result = await request('http://cggekijo.blog.fc2.com/?xml');
  const $ = cheerio.load(result, {
    xml: { normalizeWhitespace: true, }
  });
  const items = $('item').map((index, item) => {
    const link = $(item).attr('rdf:about');
    const title = $(item).children('title').first().text().trim();
    const date = $(item).children('dc\\:date').first().text();
    return { name, link, title, date };
  });
  return Array.from(items);
};
