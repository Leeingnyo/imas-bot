const request = require('request-promise-native');
const cheerio = require('cheerio');

module.exports = async function ({ keywords, badwords, minorName } = {}) {
  keywords = keywords || [];
  badwords = badwords || [];
  const baseUrl = `http://gall.dcinside.com/${minorName}/`;
  const result = await request.get({
    url: `http://gall.dcinside.com/mgallery/board/lists/?id=${minorName}&page=1&exception_mode=recommend`,
    headers: { 'User-Agent': '' }
  });
  const $ = cheerio.load(result);
  const items = $('tbody .ub-content').filter((index, item) => {
    return $(item).children('.gall_num').first().text() !== '설문'
        && $(item).children('.gall_subject').first().text() !== '공지'
        && $(item).children('.icon_notice').length === 0
        && $(item).data('no');
  }).map((index, item) => {
    const link = `${baseUrl}${$(item).data('no')}`;
    const title = $(item).children('.gall_tit').children('a').first().text();
    const date = $(item).children('.gall_date').first().text();
    return { link, title, date };
  }).filter((index, item) => {
    return (!keywords.length || keywords.find(keyword => item.title.includes(keyword)))
        && (!badwords.length || !badwords.find(keyword => item.title.includes(keyword)));
  });
  return Array.from(items);
};


