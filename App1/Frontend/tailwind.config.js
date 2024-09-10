/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    
    container: {
      center: true,
      padding: '15px',
   
    },
    fontFamily: {
      
    },
    textColor: {
      white: '#fff',
      blue:
      {
        DEFAULT: '#3877f5',
        500: '#6698fa',
      },
      primrary : "#141f33",
      transparent : 'transparent',
      red : '#f55656'
    },
    screens: {
      sm: '640px',
      md: '768px',
      lg: '960px',
      xl: '1200px',
    },
    colors: { 
      primrary : "#141f33",
      secondary : "#1e1e24",
      white: "rgba(255, 255, 255, 0.121)",
      transparent : 'transparent',
      blue:
      {
        DEFAULT: '#3877f5',
        500: '#6698fa',
      } ,
      black : '#000000',
    },

  },
  plugins: [],

}