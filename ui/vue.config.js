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
  /*chainWebpack: config => {
      const types = ['vue-modules', 'vue', 'normal-modules', 'normal']
      types.forEach(type => addStyleResource(config.module.rule('stylus').oneOf(type)))
    },
  }

  function addStyleResource (rule) {
    rule.use('style-resource')
      .loader('style-resources-loader')
      .options({
        patterns: [
          path.resolve(__dirname, './src/styles/imports.styl'),
      ],
    })
  */
}
