<template>
  <div
    class="px-4 py-0 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-0"
  >
    <div class="stat-container grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
      <div v-for="item in stats" :key="item.id" class="text-center stat-item">
        <div
          class="flex items-center justify-center w-30 h-30 mx-auto mb-3 rounded-full bg-green-50 sm:w-12 sm:h-12"
        >
          <font-awesome-icon
            class="w-8 h-8 text-green-400 sm:w-10 sm:h-10"
            :icon="item.icon"
          />
        </div>
        <h6 class="text-4xl font-bold text-green-400">{{ item.count }}</h6>
        <p class="mb-2 font-bold text-md">{{ item.title }}</p>
        <p class="text-gray-700">
          {{ item.description }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { inject } from "vue";

gsap.registerPlugin(ScrollTrigger);
export default {
  name: "ServiceStats",
  mounted() {
    this.$nextTick(() => {
      this.initScrollAnimation();
    });
    this.statsAnimation();
  },
  methods: {
    statsAnimation() {
      ScrollTrigger.create({
        trigger: ".stat-container",
        start: "top 80%",
        end: "bottom 20%",
        scrub: 3,
        onEnter: () => {
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
        },
        onEnterBack: () => {
          gsap.to(".stat-item", {
            duration: 0.5,
            opacity: 1,
            y: 30,
            stagger: 0.2,
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
        },
      });
    },
  },
  setup() {
    const stats = inject("dataENG").stats;
    return {
      stats,
    };
  },
};
</script>
