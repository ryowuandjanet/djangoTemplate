/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../**/templates/*.html',
    '../**/templates/**/*.html'
  ],
  theme: {
    fontFamily: {
      nototc: ['Noto Sans TC'],
      roboto: ['Roboto'],
    },
    extend: {},
  },
  plugins: [],
}
