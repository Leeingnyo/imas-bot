const request = require('request-promise-native');
const cheerio = require('cheerio');

module.exports = async function ({ keywords, badwords, banned, name } = {}) {
  keywords = keywords || [];
  badwords = badwords || [];
  banned = banned || [];
  const baseUrl = `https://gall.dcinside.com/${name}/`;
  const result = await request.get({
    url: `https://gall.dcinside.com/board/lists/?id=${name}&page=1&exception_mode=recommend`,
    headers: { 'User-Agent': '' }
  });
  const $ = cheerio.load(result);
  const items = $('tbody .ub-content').filter((index, item) => {
    return $(item).children('.gall_num').first().text() !== '설문'
        && $(item).children('.gall_num').first().text() !== '공지'
        && $(item).children('.icon_notice').length === 0
        && $(item).data('no');
  }).map((index, item) => {
    const link = `${baseUrl}${$(item).data('no')}`;
    const title = $(item).children('.gall_tit').children('a').first().text();
    const date = $(item).children('.gall_date').first().text();
    const writer = $(item).children('.gall_writer').children('.nickname').first().text();
    return { link, title, date, writer };
  }).filter((index, item) => {
    return (!keywords.length || keywords.find(keyword => item.title.includes(keyword)))
        && (!badwords.length || !badwords.find(keyword => item.title.includes(keyword)))
        && (!banned.length || !banned.find(keyword => item.writer === keyword));
  });
  return Array.from(items);
};

