(function(global) {
    var map = {
        'app':      'build',
        'rxjs':     'node_modules/rxjs',
        '@angular': 'node_modules/@angular',
        'lodash': 'node_modules/lodash',
        'angular2-datatable': 'node_modules/angular2-datatable'
    };

    var packages = {
        'app':  { main: 'main.js',  defaultExtension: 'js' },
        'rxjs': { defaultExtension: 'js' },
        'lodash': { main: 'lodash', defaultExtension: 'js' },
        'angular2-datatable':  {main: "datatable", defaultExtension: "js"}
    };

    var angularPackages = [
        '@angular/common',
        '@angular/compiler',
        '@angular/core',
        '@angular/http',
        '@angular/platform-browser',
        '@angular/platform-browser-dynamic',
        '@angular/router',
        '@angular/router-deprecated'
    ];

    angularPackages.forEach(function(pkgName) {
        packages[pkgName] = {
            main: 'index.js', defaultExtension: 'js'
        };
    });

    var config = {
        map: map,
        packages: packages
    };

    System.config(config);

})(this);

