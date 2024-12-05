/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    alias: {
      // this will match a file
      'my-file': 'path/to/my-file.js',

      // this will match a directory and its contents
      // (`my-directory/x` resolves to `path/to/my-directory/x`)
      'my-directory': 'path/to/my-directory',

      // an alias ending /* will only match
      // the contents of a directory, not the directory itself
      'my-directory/*': 'path/to/my-directory/*'
    }
  }
}
