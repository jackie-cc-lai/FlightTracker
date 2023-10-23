/** @type {import('tailwindcss').Config} */

const sizings = {
  "5px": "5px",
  "10px": "10px",
  "20px": "20px",
  "50px": "50px",
  "60px": "60px",
  "80px": "80px",
};
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      spacing: sizings,
    },
    width: {
      full: "100%",
      content: "1024px",
      sidebar: "400px",
    },
  },
  plugins: [],
};
