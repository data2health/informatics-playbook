const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../basicstrap/templates/basicstrap/static/vue"),
  assetsDir: "./",
  pages: {
        index: {
          entry: 'src/main.js',
          template: 'src/public/index.html',
          filename: 'index.html',
        },
    },
}
