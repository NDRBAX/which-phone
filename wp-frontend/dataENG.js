// NAVIGATION
const navigation = [
  { name: "Home", link: "/", current: true },
  { name: "Search", link: "/search", current: false },
  { name: "Categories", link: "/categories", current: false },
  { name: "Wishlist", link: "/wishlist", current: false },

  // { name: "Contact", link: "/contact", current: false },
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
    title: "Brands",
    icon: "fa-solid fa-industry",
    count: 120,
    description:
      "A wide selection of different smartphone brands to choose from.",
  },
  {
    title: "Models",
    icon: "fa-solid fa-mobile-screen-button",
    count: 11500,
    description: "Find the perfect smartphone model for your needs.",
  },
  {
    title: "Visitors",
    icon: "fa-solid fa-users",
    count: 1500,
    description:
      "Helping people compare smartphone specs and prices every day. ",
  },
  {
    title: "Stores Compared",
    icon: "fa-solid fa-comments-dollar",
    count: 15,
    description: "Guaranteed best prices from different online stores.",
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
    utfIcon: "✓",
    title: "Fill the form",
    description: "Quick and easy form to find your perfect smartphone match.",
  },
  {
    icon: "fa-solid fa-brain",
    utfIcon: "?",
    title: "Algorithm analysis",
    description: "Our powerful algorithm searches for the best match for you.",
  },
  {
    icon: "fa-solid fa-hand-holding-dollar",
    utfIcon: "$",
    title: "Results at best price",
    description: "Get the best deals and prices on your dream smartphone.",
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
    "Join our community and stay in the know with the latest smartphone news and deals! But don't worry – we promise not to spam you. Subscribe to our newsletter today and never miss out on a thing!",
  subject: "Newsletter",
  subtitle: "Subscribe",
};

const multiStepFormData = [
  {
    index: 0,
    title: "Step 1",
    active: true,
    questions: [
      {
        label:
          "Average <span class='text-teal-accent-400'>daily screen time</span> on my smartphone",
        type: "radio",
        step: "Screen Activity",
        choices: [
          { value: "less_than_1_hour", label: "Below a hour" },
          { value: "1_2_hours", label: "About 2 hours" },
          { value: "2_3_hours", label: "Around 3 hours" },
          { value: "more_than_3_hours", label: "Over 3 hours" },
        ],
      },
    ],
  },
  {
    index: 1,
    title: "Step 2",
    active: false,
    questions: [
      {
        label:
          "As an integral part of my daily routine, my main <span class='text-teal-accent-400'>smartphone usage</span> will be for",
        type: "checkbox",
        step: "Smartphone Usage",
        choices: [
          {
            value: "calls_messaging_and_mails",
            label: "Communication",
          },
          {
            value: "multimedia_music_videos_photos",
            label: "Multimedia",
          },

          { value: "social_networks", label: "Social Media" },
          { value: "web_browsing", label: "Web browsing" },
          {
            value: "news_weather_and_gps",
            label: "News and navigation",
          },
          { value: "gaming", label: "Gaming" },
        ],
      },
    ],
  },
  {
    index: 2,
    title: "Step 3",
    active: false,
    questions: [
      {
        label:
          "In order to accommodate all of my data, my <span class='text-teal-accent-400'>smartphone storage</span> must be",
        type: "radio",
        step: "Storage Space",
        choices: [
          { value: "decent_storage", label: "Decent" },
          { value: "average_storage", label: "Average" },
          { value: "generous_storage", label: "Generous" },
        ],
      },
    ],
  },
  {
    index: 3,
    title: "Step 4",
    active: false,
    questions: [
      {
        label:
          "The <span class='text-teal-accent-400'>screen size</span> might be my main concern, and I'm comfortable with",
        type: "radio",
        step: "Screen Size",
        choices: [
          { value: "small_screen", label: "Small phones" },
          { value: "medium_screen", label: "Medium phones" },
          { value: "large_phones", label: "Large phones" },
        ],
      },
    ],
  },
  {
    index: 4,
    title: "Step 5",
    active: false,
    questions: [
      {
        label:
          "<span class='text-teal-accent-400'>Additional features</span> that I consider essential to meet my needs are",
        type: "checkbox",
        step: "Key features",
        choices: [
          // {
          //   value: "fast_processor",
          //   label: "Fast Processor",
          // },
          {
            value: "quick_charging",
            label: "Quick charging",
          },
          { value: "large_battery", label: "Large battery" },
          // { value: "large_display", label: "Large Display" },
          {
            value: "high_quality_camera",
            label: "Premium Camera",
          },
          {
            value: "long_range_connectivity",
            label: "5G Connectivity",
          },
          { value: "dual_sim", label: "Dual SIM" },

          // {
          //   value: "plenty_of_storage_space",
          //   label: "Ample Storage",
          // },
          { value: "removable_storage", label: "Expandable Storage" },
          { value: "audio_jack", label: "Audio Jack" },
        ],
      },
    ],
  },
  // {
  //   title: "Step 6",
  //   active: false,
  //   questions: [
  //     {
  //       label:
  //         "You need a smartphone with <span class='text-teal-accent-400'>particular features</span>",
  //       type: "checkbox",
  //       step: "Fourth step",
  //       choices: [
  //         {
  //           value: "age_appropriate_content",
  //           label: "Age-appropriate content",
  //         },
  //         { value: "parental_controls", label: "Parental controls" },
  //         {
  //           value: "simple__user_interface",
  //           label: "Simple user interface",
  //         },
  //         {
  //           value: "easy_to_press_buttons",
  //           label: "Large, easy-to-press buttons",
  //         },
  //         {
  //           value: "aid_compatibility",
  //           label: "Hearing aid compatibility mode",
  //         },
  //       ],
  //     },
  //   ],
  // },
  {
    index: 5,
    title: "Step 6",
    active: false,
    questions: [
      {
        label:
          "I'd like to find a smartphone that meets my <span class='text-teal-accent-400'>budget requirements</span>",
        type: "radio",
        step: "Budget Range",
        choices: [
          { value: "under_200", label: "Under $200" },
          { value: "200_600", label: "$200 - $600" },
          // { value: "600_900", label: "$600 - $900" },
          // { value: "600_900", label: "$600 - $900" },
          { value: "over_600", label: "Over $600" },
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
  multiStepFormData,
};
