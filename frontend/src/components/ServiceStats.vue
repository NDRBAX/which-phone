<template>
  <div
    id="stats-section"
    v-bind:style="[
      width < 1024
        ? {
            'background-image': 'url(' + hero.coverImage + ')',
            'background-size': 'cover',
            'background-position': 'center',
          }
        : { 'background-image': 'none' },
    ]"
    class="relative w-full h-56 w-full sm:h-72 md:h-96 flex justify-center"
  >
    <div
      class="stat-card absolute md:mt-12 lg:mt-0 mx-auto xs:max-w-md sm:max-w-xl md:max-w-3xl lg:max-w-4xl xl:max-w-7xl md:px-24 lg:px-8 lg:py-0 bg-white rounded shadow-xl"
    >
      <div
        class="grid gap-12 md:px-0 py-5 xs:px-12 xs:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 pb-20"
      >
        <div v-for="item in stats" :key="item.id" class="text-center stat-item">
          <div
            class="flex items-center justify-center xs:w-8 xs:w-8 md:w-30 md:h-30 mx-auto mb-3 rounded-full bg-green-50"
          >
            <font-awesome-icon
              class="xs:w-8 xs:w-8 sm:w-8 sm:h-8 text-green-400"
              :icon="item.icon"
            />
          </div>
          <h6 class="sm:text-3xl md:text-4xl font-bold text-green-400">
            {{ item.count }}
          </h6>
          <p class="mb-2 font-bold sm:text-sm md:text-md">{{ item.title }}</p>
          <p class="text-gray-700 xs:text-sm md:text-md">
            {{ item.description }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { watchEffect, ref, inject } from "vue";

gsap.registerPlugin(ScrollTrigger);
export default {
  name: "ServiceStats",
  mounted() {
    this.statsAnimation();
  },
  methods: {
    statsAnimation() {
      let responsive = gsap.matchMedia();
      let desktopBreakPoint = 1024;
      let mobileBreakPoint = 640;

      responsive.add(
        {
          isMobile: `screen and (max-width: ${mobileBreakPoint}px)`,
          isTablet: `(max-width: ${desktopBreakPoint - 1}px) and (min-width: ${
            mobileBreakPoint + 1
          }px) and (prefers-reduced-motion: no-preference)`,
          isDesktop: `(min-width: ${desktopBreakPoint}px) and (prefers-reduced-motion: no-preference)`,
        },
        (context) => {
          let { isDesktop, isTablet, isMobile } = context.conditions;

          ScrollTrigger.create({
            trigger: ".stat-card",
            start: "top 80%",
            end: "bottom 20%",
            scrub: 3,
            onEnter: () => {
              gsap.from("#stats-section", {
                duration: 3,
                opacity: 1,
                y: 80,
                ease: "power4.out",
              });

              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 1,
                y: isTablet ? 250 : isMobile ? 180 : isDesktop ? 20 : 10,
                ease: "power4.out",
              });

              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 1,
                y: 30,
                stagger: 0.2,
                ease: "power4.out",
              });
            },
            onLeave: () => {
              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.2,
                ease: "power4.out",
              });

              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                ease: "power4.out",
              });
            },
            onEnterBack: () => {
              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 1,
                y: 30,
                stagger: 0.2,
                ease: "power4.out",
              });

              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 1,
                y: isTablet ? 280 : 20,
                ease: "power4.out",
              });
            },
            onLeaveBack: () => {
              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.2,
                ease: "power4.out",
              });

              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                ease: "power4.out",
              });
            },
          });
        }
      );
      return () => {
        responsive.remove();
      };
    },
  },
  setup() {
    const stats = inject("dataENG").stats;
    const hero = inject("dataENG").hero;

    const width = ref(window.innerWidth);

    const updateWidth = () => {
      width.value = window.innerWidth;
    };

    watchEffect(() => {
      window.addEventListener("resize", updateWidth);
      return () => window.removeEventListener("resize", updateWidth);
    });

    return {
      stats,
      hero,
      width,
    };
  },
};
</script>
