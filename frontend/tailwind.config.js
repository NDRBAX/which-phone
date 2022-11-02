/* eslint-env node */
/** @type {import('tailwindcss').Config} */

// const defaultTheme = require("tailwindcss/defaultTheme");
module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },

  content: ["./src/**/*.{html,js,vue}", "./public/**/*.html"],
  // theme: {
  //   fontFamily: {
  //     sans: ["Inter", ...defaultTheme.fontFamily.sans],
  //   },
  // },
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
    },
    colors: {
      blue: "#1fb6ff",
      white: "#ffffff",
      purple: "#7e5bef",
      pink: "#ff49db",
      orange: "#ff7849",
      green: "#0be881",
      yellow: "#ffc82c",
      "gray-dark": "#273444",
      gray: {
        DEFAULT: "#8492a6",
        100: "#f5f7fa",
        200: "#e4e7eb",
        300: "#cbd2d9",
        400: "#9aa5b1",
        500: "#7b8794",
        600: "#616e7c",
        700: "#3e4c59",
        800: "#323f4b",
        900: "#1f2933",
      },
      "gray-light": "#d3dce6",
    },
    fontFamily: {
      sans: ["Graphik", "sans-serif"],
      serif: ["Merriweather", "serif"],
    },
    extend: {
      spacing: {
        "8xl": "96rem",
        "9xl": "128rem",
      },
      borderRadius: {
        "4xl": "2rem",
      },
    },
  },
  variants: {},
  plugins: [],
};
