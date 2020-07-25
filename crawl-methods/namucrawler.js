const request = require('request-promise-native');
const cheerio = require('cheerio');

module.exports = async function ({ keywords, badwords, banned, name } = {}) {
  keywords = keywords || [];
  badwords = badwords || [];
  banned = banned || [];
  const baseUrl = `https://namu.live`;
  const result = await request.get({
    url: `https://namu.live/b/${name}/?mode=best`,
    // headers: { 'User-Agent': '' }
  });
  const $ = cheerio.load(result);
  const items = $('.list-table a.vrow:not(.notice)').filter((index, item) => {
    return true;
    /*
    return $(item).children('.gall_num').first().text() !== '설문'
        && $(item).children('.gall_num').first().text() !== '공지'
        && $(item).children('.icon_notice').length === 0
        && $(item).data('no');
    */
  }).map((index, item) => {
    const link = `${baseUrl}${item.attribs.href}`;
    const title = $(item).find('.title').first().text();
    const date = $(item).find('time').first().text();
    const writer = $(item).find('.user-info').first().text().trim();
    return { link, title, date, writer };
  }).filter((index, item) => {
    return (!keywords.length || keywords.find(keyword => item.title.includes(keyword)))
        && (!badwords.length || !badwords.find(keyword => item.title.includes(keyword)))
        && (!banned.length || !banned.find(keyword => item.writer === keyword));
  });
  return Array.from(items);
};
