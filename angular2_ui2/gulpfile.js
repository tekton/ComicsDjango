var gulp = require('gulp');
var sass = require('gulp-sass');
var bower = require('gulp-bower');

var bowerDir = './bower_components';

var assetsDev = 'assets/';
var assetsProd = '../static/src/';

var appDev = 'app/';
var appProd = '../static/app/';
var templatesProd = '../static/app';

/* Mixed */
var ext_replace = require('gulp-ext-replace');

/* CSS */
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');
var precss = require('precss');
var cssnano = require('cssnano');

/* JS & TS */
var jsuglify = require('gulp-uglify');
var typescript = require('gulp-typescript');

/* Images */
var imagemin = require('gulp-imagemin');

var tsProject = typescript.createProject('tsconfig.json');

gulp.task('build-css', function () {
    return gulp.src(assetsDev + 'scss/*.scss')
        .pipe(sass({
            includePaths: [bowerDir + '/bootstrap-sass/assets/stylesheets']
        }))
        .pipe(sourcemaps.init())
        .pipe(postcss([precss, autoprefixer, cssnano]))
        .pipe(sourcemaps.write())
        .pipe(ext_replace('.css'))
        .pipe(gulp.dest(assetsProd + 'css/'));
});

gulp.task('build-ts', function () {
    return gulp.src(appDev + '**/*.ts')
        .pipe(sourcemaps.init())
        .pipe(typescript(tsProject))
        .pipe(sourcemaps.write())
        //.pipe(jsuglify())
        .pipe(gulp.dest(appProd));
});

gulp.task('build-img', function () {
    return gulp.src(assetsDev + 'img/**/*')
        .pipe(imagemin({
            progressive: true
        }))
        .pipe(gulp.dest(assetsProd + 'img/'));
});

gulp.task('build-html', function () {
    return gulp.src(appDev + '**/*.html')
        .pipe(gulp.dest(templatesProd));
});

// don'pt want to have to build node on deploys
gulp.task('copy-libs', function() {
    return gulp.src([
            "node_modules/es6-shim/es6-shim.min.js",
            "node_modules/systemjs/dist/system-polyfills.js",
            "node_modules/angular2/es6/dev/src/testing/shims_for_IE.js",
            "node_modules/angular2/bundles/angular2-polyfills.js",
            "node_modules/systemjs/dist/system.src.js",
            "node_modules/rxjs/bundles/Rx.js",
            "node_modules/angular2/bundles/angular2.js",
            "node_modules/angular2/bundles/router.dev.js",
            "node_modules/angular2/bundles/http.js",
            "node_modules/ng2-bootstrap/bundles/ng2-bootstrap.min.js",
            "node_modules/moment/moment.js"
        ])
        .pipe(gulp.dest(assetsProd + 'js/'))
});

gulp.task('copy-lib-css', function() {
    return gulp.src([
            "node_modules/nvd3/build/*.css",
            "assets/*.css"
        ])
        .pipe(gulp.dest(assetsProd + 'css/'))
});

gulp.task('watch', function () {
    gulp.watch(appDev + '**/*.ts', ['build-ts']);
    gulp.watch(assetsDev + 'scss/**/*.scss', ['build-css']);
    gulp.watch(assetsDev + 'img/*', ['build-img']);
    gulp.watch(appDev + '**/*.html', ['build-html']);
    gulp.watch('assets/*.css', ['copy-lib-css']);
});

gulp.task('default', ['watch', 'build-ts', 'build-css',
    'build-html', 'copy-libs', 'copy-lib-css']);