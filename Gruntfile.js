var browserifyOptions = {
  browserifyOptions: {
    paths: ['./node_modules', './js']
  },
  watch: true
};

var browserifyConfigs = {
  all: {
      files: {
        'static/js/bundle.js': ['./js/index.js']
      },
      options: browserifyOptions
  }
};

module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      dynamic_mappings: {
        files: [
          {
            expand: true,
            cwd: 'js/',
            src: '*.js',
            dest: 'static/js/'
          }
        ]
      }
    },
    bower: {
      install: {
         options: {
           cleanup: true,
           targetDir: 'static/components'
         }
      }
    },
    django_cmd: 'python manage.py',
    shell: {
        collectstatic: {
            command: '<%= django_cmd %> collectstatic --noinput'
        }
    },
    jshint: {
      options: {
        jshintrc: './.jshint.rc'
      },
      all: {
        src: ['Gruntfile.js', 'js/**/*.js']
      }
    },
    watch: {
      jshint: {
        files: ['js/**/*.js'],
        tasks: ['newer:jshint:all']
      },
      scripts: {
        files: ['js/**/*.js'],
        tasks: ['uglify']
      },
    },
    browserify: browserifyConfigs
  });

  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-bower-task');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // Default task(s).
  grunt.registerTask('default', ['bower:install', 'uglify',
                                 'shell:collectstatic', 'browserify']);

  grunt.registerTask('jslint', ['jshint']);
  grunt.registerTask('heroku:production', ['bower:install', 'uglify', 'browserify']);

};
