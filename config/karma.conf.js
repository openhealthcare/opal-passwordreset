module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;
  var karmaDefaults = require(opalPath + '/opal/tests/js_config/karma_defaults.js');
  var baseDir = __dirname + '/..';
  var coverageFiles = [
    __dirname+'/../passwordreset/static/js/passwordreset/**/*.js',
  ];
    var includedFiles = [
      __dirname+'/../passwordreset/static/js/passwordreset/**/*.js',
      __dirname+'/../passwordreset/static/js/test/**/*.js',
  ];

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};