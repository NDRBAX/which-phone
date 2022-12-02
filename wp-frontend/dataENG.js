// NAVIGATION
const navigation = [
  { name: "Home", link: "/", current: true },
  // { name: "Advantages", link: "/#advantages", current: false },
  // { name: "Services", link: "/#services", current: false },
  // { name: "Categories", link: "/#categories", current: false },
  // { name: "Contact", link: "/#contact", current: false },
  { name: "Search", link: "/search", current: false },
];

// HERO
const hero = {
  title: "Buy smart, love it",
  subtitle: "keep it",
  description:
    "Find the right smartphone for your needs in a few clicks, and extend its life by keeping it longer",
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
    title: "Consummers",
    icon: "fa-solid fa-users",
    count: "1.3K",
    description:
      "For many men, the acquisition of wealth does not end their troubles, it only changes them. ",
  },
  {
    title: "Models",
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
      "https://images.unsplash.com/photo-1544725121-be3bf52e2dc8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1167&q=80",
    // "https://images.unsplash.com/photo-1517940001917-1c03b8b1b85b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1157&q=80",

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
      // "https://images.unsplash.com/photo-1469384016477-880d0bb46a51?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1132&q=80",
      // "https://images.unsplash.com/photo-1537242892475-cf01eb002083?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80",
      "https://images.unsplash.com/photo-1565623190092-322d2c2a2439?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=765&q=80",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    link: "/traveler",
  },
  {
    title: "Child",
    coverImage:
      "https://images.unsplash.com/photo-1527863280617-15596f92e5c8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
  },
  {
    title: "Grandparents",
    coverImage:
      "https://images.unsplash.com/photo-1626668011660-051379e9b211?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
  },
];

// STEPS SECTION
const steps = [
  {
    icon: "fa-solid fa-check",
    title: "Fill the form",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    icon: "fa-solid fa-brain",
    title: "Algorithm analysis",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    icon: "fa-solid fa-hand-holding-dollar",
    title: "Results at best price",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
];

// CONTENT SECTION
const content = {
  title: "How it",
  subtitle: "works",
  description:
    "Once ou have fill out the quick interactive form, our algorithm will provide you the best smartphone that fits your needs, and you will be able to order it in a few clicks at the best price",
  imageOne:
    "https://images.unsplash.com/photo-1523726491678-bf852e717f6a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
  imageTwo:
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80",
  imageThree:
    "https://images.unsplash.com/photo-1529119368496-2dfda6ec2804?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
};

// ADVANTAGES SECTION
const advantages = {
  title: "To make the usage",
  titleTwo: "of smartphones",
  subtitle: "sustainable",
  description:
    "The smartphone you use (and, probably, are using right now) has a significant impact on the environment. Not just the phone you have, but every smartphone that has ever been produced",
  advantages: [
    {
      title: "Over-consumption",
      description:
        "<strong>62 distinct metals and metalloids</strong> are used to create a single smartphone. In order to make the <strong>1.4 billion cellphones that were shipped worldwide in 2018</strong>, 34 billion kg of ore, 100 billion liters of water, and 20.5 million kg of cyanide had to be mined",
    },

    {
      title: "e-Waste",
      description:
        "<strong>50 million tonnes of electronic and electrical trash</strong> were generated last year, with just a fifth of that material being legally recycled. It's estimated that <strong>millions of people labor irregular hours recycling these materials</strong>, frequently in hazardous conditions",
    },
  ],
  image:
    "https://cdn.pixabay.com/photo/2018/10/09/09/59/mobile-phone-3734545_960_720.jpg",
};

// REASONS SECTION
const reasons = {
  subject: "Benefits",
  title: "responsibly and make a difference",
  description:
    "Smartphones's CO2 emissions are equivalent to the emissions of 50 million cars. The average smartphone user in the EU uses their phone for 2.5 years before replacing it. If we all kept our phones for 5 years, we could save 1.5 million tonnes of CO2e per year",

  reasons: [
    {
      title: "Reduce your carbon footprint",
      description:
        "Buy once, use for a long time. The more you use your phone, the less you need to buy new ones",
    },
    {
      title: "Understand your needs",
      description:
        "Tell us what you need and we will help you find the best device for you",
    },
    {
      title: "Save your time",
      description:
        "You don't have to spend hours looking for the right device, reading reviews and comparing prices",
    },
    {
      title: "Save money",
      description: "Your smartphone will last longer and you will save money",
    },
  ],
};

// PUBLIC SECTION
const users = {
  subject: "Users",
  title: "need help to make the right choice",
  description:
    "We have a wide range of devices for everyone, from children to grandparents, from travelers to students",
  firstImage:
    "https://images.unsplash.com/photo-1617560611911-85e1055544cd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
  secondImage:
    "https://images.unsplash.com/photo-1534120045191-89e4963980a7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1226&q=80",
  thirdImage:
    "https://images.unsplash.com/photo-1503164592308-0b42e96735c7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1173&q=80",
  users: [
    {
      title: "Students",
      description:
        "Social media, online shopping, streaming, gaming, and more. Students need a phone that can handle it all. But they also need a phone that can handle the bumps and bruises of everyday life",
    },
    {
      title: "Business",
      description:
        "Your smartphone goes everywhere with you. Through the day, you use it to check emails, make calls, and send texts. At night, you use it to watch videos, play games, and browse the web. You need a phone that can keep up with you",
    },
    {
      title: "Parents",
      description:
        "You use it to stay connected to your family, friends, and coworkers. You need a phone that can keep up with you. Or you need help to find the right phone for your child",
    },

    {
      title: "Seniors",
      description:
        "You don't need a phone that can handle the latest games and apps. You need a phone that's easy to use and can help you stay connected to the people you care about",
    },
  ],
};

// NEWSLETTER SECTION
const newsletter = {
  title: "to our newsletter",
  description:
    "Don't miss out on the latest news and offers. We promise not to spam you or sell your email address",
  subject: "Newsletter",
  subtitle: "Subscribe",
};

// FORM DATA
const formData = [
  {
    title: "Step 1",
    active: true,
    questions: [
      {
        type: "radio",
        label: "For whom are you looking to buy a phone ?",
        choices: [
          {
            label: "Choice 1",
            title: "A child",
          },
          {
            label: "Choice 2",
            title: "An adult",
          },
          {
            label: "Choice 3",
            title: "A senior",
          },
        ],
      },
    ],
  },
  {
    title: "Step 2",
    active: false,
    questions: [
      {
        type: "radio",
        label: "How much time do you spend on your phone ?",

        choices: [
          {
            label: "Choice 1",
            title: "Less than 1 hour",
          },
          {
            label: "Choice 2",
            title: "1-2 hours",
          },
          {
            label: "Choice 3",
            title: "2-3 hours",
          },
          {
            label: "Choice 4",
            title: "More than 3 hours",
          },
        ],
      },
    ],
  },
  {
    title: "Step 3",
    active: false,
    questions: [
      {
        type: "checkbox",
        label: "What do you use your phone for ?",
        choices: [
          {
            label: "Choice 1",
            title: "Social media",
          },
          {
            label: "Choice 2",
            title: "Gaming",
          },
          {
            label: "Choice 3",
            title: "Online Video",
          },
          {
            label: "Choice 4",
            title: "Taking photos",
          },
          {
            label: "Choice 5",
            title: "Music",
          },

          {
            label: "Choice 6",
            title: "Reading",
          },
          {
            label: "Choice 7",
            title: "Communicating (email, text, phone)",
          },
          {
            label: "Choice 8",
            title: "Web browsing",
          },
        ],
      },
    ],
  },
];

export default {
  navigation,
  stats,
  hero,
  categories,
  advantages,
  reasons,
  newsletter,
  content,
  users,
  steps,
  formData,
};
