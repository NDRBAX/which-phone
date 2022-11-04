<template>
  <div class="relative overflow-hidden bg-white z-0">
    <div class="mx-auto max-w-7xl">
      <div
        class="relative z-10 pb-8 sm:pb-16 md:pb-20 lg:w-full lg:max-w-2xl lg:pb-28 xl:pb-32"
      >
        <main
          class="mx-auto pt-10 max-w-7xl px-4 sm:pt-12 sm:px-6 md:pt-16 lg:pt-20 lg:px-8 xl:pt-28"
        >
          <div class="sm:text-center lg:text-left box-header">
            <h1
              class="title-header text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl md:text-6xl"
            >
              <span class="block xl:inline">{{ hero.title }}</span>
              {{ " " }}
              <span class="block text-green-600 xl:inline">{{
                hero.subtitle
              }}</span>
            </h1>
            <p
              class="paragraph-header mt-3 text-base text-gray-500 sm:mx-auto sm:mt-5 sm:max-w-xl sm:text-lg md:mt-5 md:text-xl lg:mx-0"
            >
              {{ hero.description }}
            </p>
            <div
              class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start"
            >
              <div class="rounded-md shadow">
                <a
                  href="#"
                  class="flex w-full items-center justify-center rounded-md border border-transparent bg-green-600 px-8 py-3 text-base font-medium text-white hover:bg-green-700 md:py-4 md:px-10 md:text-lg"
                  >{{ hero.firstButton }}</a
                >
              </div>
              <div class="mt-3 sm:mt-0 sm:ml-3">
                <a
                  href="#"
                  class="flex w-full items-center justify-center rounded-md border border-transparent bg-green-100 px-8 py-3 text-base font-medium text-green-700 hover:bg-green-200 md:py-4 md:px-10 md:text-lg"
                  >{{ hero.secondButton }}</a
                >
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
    <div class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/3 cover-header-1">
      <svg
        class="absolute inset-y-0 left-0 hidden h-full w-5z-10 0 translate-x-1/10 transform text-white lg:block"
        fill="currentColor"
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        <polygon points="10,-100 24,0 6,100 -100,100" />
      </svg>

      <img
        class="h-56 w-full object-cover object-right sm:h-72 md:h-96 lg:h-full lg:w-full"
        :src="hero.coverImage"
        alt=""
      />
    </div>

    <div
      class="lg:absolute lg:inset-y-0 lg:left-0 lg:w-1/4 cover-header-2 hidden lg:block"
    >
      <svg
        class="absolute inset-y-0 right-48 hidden h-full w-50 translate-x-1/2 transform text-white lg:block"
        fill="currentColor"
        viewBox="0 0 100 100"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        <polygon points="50 ,-10 100,0 500,100 30,100" />
      </svg>
      <img
        class="h-56 w-full object-cover object-left sm:h-72 md:h-96 lg:h-full lg:w-full"
        :src="hero.coverImage"
        alt=""
      />
    </div>
  </div>
</template>

<script>
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { inject } from "vue";

gsap.registerPlugin(ScrollTrigger);
export default {
  name: "HeroSection",

  mounted: function () {
    this.scrollAnimation();
  },
  methods: {
    scrollAnimation() {
      if (window.innerWidth > 1024) {
        ScrollTrigger.create({
          trigger: ".box-header",
          start: "top 70%",
          end: "bottom 10%",
          scrub: 3,

          onEnter: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: 200,
              opacity: 1,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: -10,
              opacity: 1,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: 10,
              opacity: 1,
            });
            gsap.to(".title-header", {
              duration: 0.5,
              x: -80,
              opacity: 1,
            });
            gsap.to(".paragraph-header", {
              duration: 0.5,
              x: -50,
              opacity: 1,
            });
          },
          onLeave: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: -200,
              opacity: 0,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: 10,
              opacity: 0,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: -10,
              opacity: 0,
            });
            gsap.to(".title-header", {
              duration: 0.5,
              x: 80,
              opacity: 0,
            });
          },

          onEnterBack: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: 200,
              opacity: 1,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: -10,
              opacity: 1,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: 10,
              opacity: 1,
            });
            gsap.to(".title-header", {
              duration: 0.5,
              x: -80,
              opacity: 1,
            });
            gsap.to(".paragraph-header", {
              duration: 0.5,
              x: -50,
              opacity: 1,
            });
          },
          onLeaveBack: () => console.log("leave back"),
          // markers: true,
          // id: "hero",
        });
      } else {
        ScrollTrigger.create({
          trigger: ".box-header",
          start: "top 70%",
          end: "bottom 0%",
          scrub: 3,

          onEnter: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: 0,
              opacity: 1,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
            gsap.to(".title-header", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
            gsap.to(".paragraph-header", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
          },
          onLeave: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: 0,
              opacity: 0,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: 0,
              opacity: 0,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: 0,
              opacity: 0,
            });
          },

          onEnterBack: () => {
            gsap.to(".box-header", {
              duration: 2,
              x: 0,
              opacity: 1,
            });
            gsap.to(".cover-header-1", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
            gsap.to(".cover-header-2", {
              duration: 0.5,
              x: 0,
              opacity: 1,
            });
          },
          onLeaveBack: () => console.log("leave back"),
          // markers: true,
        });
      }
    },
  },
  setup() {
    const hero = inject("dataENG").hero;
    return {
      hero,
    };
  },
};
</script>
