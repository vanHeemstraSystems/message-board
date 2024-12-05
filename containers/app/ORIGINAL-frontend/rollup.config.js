import svelte from 'rollup-plugin-svelte'
import resolve from '@rollup/plugin-node-resolve'
import commonjs from '@rollup/plugin-commonjs'
import { terser } from '@rollup/plugin-terser'
import css from 'rollup-plugin-css-only'
import postcss from 'rollup-plugin-postcss'
import livereload from 'rollup-plugin-livereload'
import serve from 'rollup-plugin-serve'

const production = !process.env.ROLLUP_WATCH

export default {
  input: 'src/main.js',
  output: {
    sourcemap: true,
    format: 'iife', // Immediately Invoked Function Expression — suitable for <script> tags
    name: 'app',
    file: 'public/build/bundle.js'
  },
  plugins: [
    svelte({
      // enable run-time checks when not in production
      dev: !production,
      // extract CSS into a separate file (optional)
      css: css => {
        css.write('public/build/bundle.css')
      }
    }),

    // PostCSS for Tailwind CSS
    postcss({
      extract: true,
      minimize: production
    }),

    // resolve allows you to import modules from node_modules
    resolve({
      browser: true,
      dedupe: ['svelte']
    }),
    commonjs(),

    // In dev mode, call `rollup-plugin-livereload` to refresh the page on changes
    !production && livereload('public'),

    // Serve the app in development
    !production &&
      serve({
        open: true,
        contentBase: 'public',
        historyApiFallback: true,
        port: 5000
      }),

    // Minify the bundle in production
    production && terser()
  ],
  watch: {
    clearScreen: false
  }
}
