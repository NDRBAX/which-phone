// NAVIGATION
const navigation = [
  { name: "Guid", link: "/", current: true },
  { name: "Pricing", link: "/pricing", current: false },
  { name: "About", link: "/about", current: false },
];

// HERO
const hero = {
  title: "Buy smart, love it",
  subtitle: "keep it",
  description:
    "Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.",
  firstButton: "Get Started",
  firstLink: "/pricing",
  secondButton: "Live Demo",
  secondLink: "https://guid-demo.netlify.app/",
  coverImage:
    "https://images.unsplash.com/photo-1496287956732-7522d174a1ba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
};

// SERVICES STATS
const stats = [
  {
    title: "Shops",
    icon: "fa-solid fa-shop",
    count: "25",
    description:
      "It’s something that’s many of the wisest people in history have kept in mind.",
  },
  {
    title: "Happy Consummers",
    icon: "fa-solid fa-users",
    count: "1.3K",
    description:
      "For many men, the acquisition of wealth does not end their troubles, it only changes them. ",
  },
  {
    title: "Smartphone Models",
    icon: "fa-solid fa-mobile-screen-button",
    count: "2.5K",
    description:
      "It's a helluva start, being able to recognize what makes you happy today, in this moment.",
  },
  {
    title: "Best price",
    icon: "fa-solid fa-comments-dollar",
    count: "52",
    description:
      "Happiness is when what you think, what you say, and what you do are in harmony.",
  },
];

// CATEGORIES SECTION
const categories = [
  {
    title: "Gamer",
    coverImage:
      "https://images.unsplash.com/photo-1626240130051-68871c71de47?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1332&q=80",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    link: "/gamer",
  },
  {
    title: "Business",
    coverImage:
      "https://images.unsplash.com/photo-1517940001917-1c03b8b1b85b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1157&q=80",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    link: "/business",
  },
  {
    title: "Student",
    coverImage:
      "https://images.unsplash.com/photo-1520333789090-1afc82db536a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    link: "/student",
  },
  {
    title: "Traveler",
    coverImage:
      "https://images.unsplash.com/photo-1469384016477-880d0bb46a51?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1132&q=80",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    link: "/traveler",
  },
];

export default { navigation, stats, hero, categories };
