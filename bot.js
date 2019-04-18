const tls = require('tls');

process.env['NODE_TLS_REJECT_UNAUTHORIZED'] = '0';

const ops = {
  ping() {
    return 'PONG :pingis\n';
  },
  sendmsg(chan, msg) {
    return `PRIVMSG ${chan} :${msg}\n`;
  },
  joinchan(chan) {
    return `JOIN ${chan}\n`;
  },
  partchan(chan) {
    return `PART ${chan}`;
  },
  giveop(chan, nick) {
    return `MODE ${chan} +o ${nick}\n`;
  }
};

function Waaai(chan) {
  return ops.sendmsg(chan, '와ㅡ이!');
}

function Bot(config) {
  this._config = config;
};

Bot.prototype.connect = async function () {
  return new Promise((resolve, reject) => {
    this._socket = tls.connect({
      host: this._config.server,
      port: this._config.port
    }, () => {
      this._socket.write(`USER ${this._config.botname} ${this._config.botname} ${this._config.botname} :${this._config.botname}\n`);
      this._socket.write(`NICK ${this._config.botnick}\n`);
      this._config.channels.map(chan => this._socket.write(ops.joinchan(chan)));

      resolve();
    });

    this._socket.setEncoding('utf8');
    this._socket.on('data', async (data) => {
      if (data.includes('PING :')) {
        return this._socket.write(ops.ping());
      }
    });
  });
}

Bot.prototype.send = function (channel, message) {
  this._socket.write(ops.sendmsg(channel, message));
};

module.exports = Bot;
