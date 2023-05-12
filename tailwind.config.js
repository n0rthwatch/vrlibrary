const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./librarySite/templates/**/*.{html,js}"],
  theme: {
    screens: {
      sm: "460px",
      md: "750px",
      lg: "992px",
      xl: "1200px",
      "2xl": "1520px",
    },
    container: {
      padding: "1rem",
      animation: defaultTheme,
    },
    extend: {
      colors: {
        main: "#EAEAEA",
        accent: "#333333",
        "sec-accent": "#FFA500",
      },
      fontFamily: {
        sans: ["Bitter", ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [],
};
