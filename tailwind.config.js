/** @type {import('tailwindcss').Config} */
module.exports = {
  content:  [
      "newproject/templates/**/*.{html,js}" ,
      "newproject/templates/component/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

