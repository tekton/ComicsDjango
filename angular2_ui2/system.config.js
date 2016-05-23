(function(global) {
    var map = {
        'app':      'build',
        'rxjs':     'node_modules/rxjs',
        '@angular': 'node_modules/@angular',
        '@angular2-material': 'node_modules/@angular2-material',
        'lodash': 'node_modules/lodash',
        'moment': 'node_modules/moment',
        'angular2-datatable': 'node_modules/angular2-datatable',
        'ng2-bootstrap': 'node_modules/ng2-bootstrap'
    };

    var packages = {
        'app':  { main: 'main.js',  defaultExtension: 'js' },
        'rxjs': { defaultExtension: 'js' },
        'lodash': { main: 'lodash', defaultExtension: 'js' },
        'moment': { main: 'moment', defaultExtension: 'js' },
        'ng2-bootstrap': { defaultExtension: 'js' },
        'angular2-datatable': {main: "datatable", defaultExtension: "js"},
        '@angular2-material/core': {main: "core", defaultExtension: "js"},
        '@angular2-material/button': {main: "button", defaultExtension: "js"},
        '@angular2-material/card': {main: "card", defaultExtension: "js"}
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

