var gulp = require('gulp'),
    concat = require('gulp-concat'),

    tsc = require('gulp-typescript'),
    mocha = require('gulp-mocha'),
    jsMinify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),

    scssLint = require('gulp-scss-lint'),
    sass = require('gulp-sass'),
    cssPrefixer = require('gulp-autoprefixer'),
    cssMinify = require('gulp-cssnano'),

    del = require('del'),
    merge = require('merge-stream'),
    SystemBuilder = require('systemjs-builder');

var appProd = '../static/app';
var assetsProd = '../static/src';

gulp.task('clean', ['clean-assets'], function() {
    return del(appProd);
});

gulp.task("clean-assets", function(){
    return del(assetsProd);
});

gulp.task('shims', function() {
    return gulp.src([
            "node_modules/systemjs/dist/system-polyfills.js",
            "node_modules/systemjs/dist/system.src.js",
            'node_modules/zone.js/dist/zone.js',
            'node_modules/reflect-metadata/Reflect.js',
            "node_modules/es6-shim/es6-shim.min.js"
        ])
        .pipe(concat('shims.js'))
        .pipe(gulp.dest(assetsProd+'/js/'));
});

gulp.task('system-build', [ 'tsc' ], function() {
    var builder = new SystemBuilder();

    return builder.loadConfig('system.config.js')
        .then(function() {builder.buildStatic('app', assetsProd+'/js/bundle.js')});
        // .then(function() {del('build')});
});

gulp.task('tsc', function() {
    var tsProject = tsc.createProject('tsconfig.json'),
        tsResult = tsProject.src().pipe(tsc(tsProject));

    return tsResult.js.pipe(gulp.dest(appProd));
});

gulp.task('html', function() {
    return gulp.src('app/**/**.html')
        .pipe(gulp.dest(appProd));
});

gulp.task('css', function() {
    return gulp.src('assets/**/**.css')
        .pipe(gulp.dest(assetsProd+"/css/"));
});

gulp.task('images', function() {
    return gulp.src('assets/images/**/*.*')
        .pipe(imagemin())
        .pipe(gulp.dest(assetsProd+'/images/'));
});

gulp.task('lintScss', function() {
    return gulp.src('assets/scss/**/*.scss')
        .pipe(scssLint({ config: 'lint.yml' }));
});

gulp.task('scss', function() {
    return gulp.src('assets/scss/main.scss')
        .pipe(sass({
            precision: 10,
            includePaths: 'node_modules/node-normalize-scss'
        }))
        .pipe(concat('styles.css'))
        .pipe(cssPrefixer())
        .pipe(gulp.dest(assetsProd+'/css/'));
});

gulp.task('test-tsc', function() {
    var tsProject = tsc.createProject('tsconfig.json');

    return tsProject.src()
        .pipe(tsc(tsProject))
        .pipe(gulp.dest('test/js/'));
});

gulp.task('test-run', [ 'test-tsc' ], function() {
    return gulp.src('test/**/*.spec.js')
        .pipe(mocha());
});

gulp.task('test', [ 'test-run' ], function() {
    return del('test/js');
});

gulp.task('minify', function() {
    var js = gulp.src(assetsProd+'/js/bundle.js')
        .pipe(jsMinify())
        .pipe(gulp.dest(assetsProd+'/js/'));

    var css = gulp.src(assetsProd+'/css/styles.css')
        .pipe(cssMinify())
        .pipe(gulp.dest(assetsProd+'/css/'));
    return merge(js, css);
});

gulp.task('watch', function() {
    var watchTs = gulp.watch('app/**/**.ts', [ 'system-build' ]),
        watchScss = gulp.watch('assets/**/*.scss', [ 'lintScss', 'scss' ]),
        watchHtml = gulp.watch('app/**/*.html', [ 'html' ]),
        watchCss = gulp.watch('assets/**/**.css', [ 'css' ]);
    // watchImages = gulp.watch('src/images/**/*.*', [ 'images' ]),

    onChanged = function(event) {
        console.log('File ' + event.path + ' was ' + event.type + '. Running tasks...');
    };

    watchTs.on('change', onChanged);
    watchScss.on('change', onChanged);
    watchHtml.on('change', onChanged);
    // watchImages.on('change', onChanged);
    watchCss.on('change', onChanged);
});

gulp.task('watchtests', function() {
    var watchTs = gulp.watch('app/**/**.ts', [ 'test-run' ]),
        watchTests = gulp.watch('test/**/*.spec.js', [ 'test-run' ]),

    onChanged = function(event) {
        console.log('File ' + event.path + ' was ' + event.type + '. Running tasks...');
    };

    watchTs.on('change', onChanged);
    watchTests.on('change', onChanged);
});

gulp.task('default', [
    'shims',
    'system-build',
    'html',
    'images',
    'lintScss',
    'scss',
    'css'
]);
