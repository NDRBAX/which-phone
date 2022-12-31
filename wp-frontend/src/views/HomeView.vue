<template>
  <div id="home">
    <!-- BANNER SECTION -->
    <div class="relative overflow-hidden bg-white z-0 mb-12">
      <div
        class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/3 cover-header-1 hidden lg:block"
      >
        <svg
          class="absolute left-[-10px] hidden h-full w-50 translate-x-1/10 transform text-white lg:block"
          fill="currentColor"
          viewBox="0 0 100 100"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <polygon points="10,-100 24,0 6,100 -30,100" />
        </svg>

        <img
          class="h-56 w-full object-cover object-right sm:h-72 md:h-96 lg:h-full lg:w-full"
          :src="hero.coverImage"
          alt=""
        />
      </div>

      <div
        class="lg:absolute lg:inset-y-0 lg:left-0 lg:w-1/3 cover-header-2 hidden lg:block"
      >
        <svg
          class="absolute offset-x-5 offset-y-5 right-[-10px] hidden h-full w-50 translate-x-1/10 transform text-white lg:block"
          fill="currentColor"
          viewBox="0 0 100 100"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <polygon points="50 ,-10 100,0 100,100 30,100" />
        </svg>
        <img
          class="h-56 w-full object-cover object-left sm:h-72 md:h-96 lg:h-full lg:w-full"
          :src="hero.coverImage"
          alt=""
        />
      </div>
      <div class="mx-auto max-w-7xl">
        <div
          class="relative z-10 pb-0 sm:pb-2 md:pb-10 lg:w-full lg:max-w-2xl lg:pb-28 xl:pb-32"
        >
          <div
            class="mx-auto pt-10 max-w-7xl px-4 sm:pt-12 sm:px-6 md:pt-16 lg:pt-20 lg:px-8 xl:pt-28"
          >
            <div class="box-header pt-10 sm:text-center lg:text-left z-0">
              <h1
                class="title-header xs:text-center text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl md:text-6xl"
              >
                <span class="block xl:inline">{{ hero.title }}</span>
                {{ " " }}
                <span class="block text-teal-accent-400 xl:inline sm:pl-12">{{
                  hero.subtitle
                }}</span>
              </h1>
              <p
                class="paragraph-header mt-3 text-base text-gray-500 sm:mx-auto sm:mt-5 sm:max-w-xl sm:text-lg md:mt-5 md:text-xl lg:mx-0 xs:px-5 xs:text-center sm:px-0"
              >
                {{ hero.description }}
              </p>
              <div
                class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start"
              >
                <div>
                  <RouterLink
                    to="/search"
                    class="flex w-full transition duration-200 shadow-md items-center justify-center rounded-md border-2 border-transparent bg-teal-accent-400 px-8 py-3 text-base font-medium text-white hover:bg-teal-accent-600 md:py-4 md:px-10 md:text-lg focus:shadow-outline focus:outline-none tracking-wide"
                    >{{ hero.firstButton }}</RouterLink
                  >
                </div>
                <div class="mt-3 sm:mt-0 sm:ml-3">
                  <RouterLink
                    to="/"
                    class="flex w-full transition duration-200 shadow-md items-center justify-center rounded-md border-2 border-teal-accent-400 bg-white px-8 py-3 text-base font-medium text-teal-accent-400 hover:text-white hover:bg-teal-accent-400 md:py-4 md:px-10 md:text-lg focus:shadow-outline focus:outline-none tracking-wide"
                    >{{ hero.secondButton }}</RouterLink
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- STATS SECTION -->
    <div class="mb-0 stats-container">
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
        class="bg-white h-56 sm:h-72 lg:h-0 md:h-96"
      ></div>
      <div class="relative px-4 sm:px-0">
        <div
          class="stat-card relative lg:mt-0 mx-auto xs:max-w-xl sm:max-w-xl md:max-w-3xl lg:max-w-4xl xl:max-w-7xl xs:px-0 md:px-12 lg:px-8 lg:py-0 xs:bg-white md:bg-transparent xs:rounded-t-md md:rounded-none"
        >
          <div
            class="grid gap-12 md:px-0 py-5 xs:p-12 xs:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 sm:pb-20 justify-center text-center"
          >
            <div v-for="item in stats" :key="item.id" class="stat-item">
              <div
                class="flex items-center justify-center xs:h-12 xs:w-12 md:w-30 md:h-30 mx-auto mb-3 rounded-full bg-gray-100"
              >
                <font-awesome-icon
                  class="xs:w-8 xs:h-8 sm:w-8 sm:h-8 text-teal-accent-400"
                  :icon="item.icon"
                />
              </div>
              <h6 class="xs:text-3xl text-center">
                <AnimatedNumber :value="item.count" :duration="1000" />
              </h6>
              <p class="mb-2 font-bold xs:text-sm sm:text-lg md:text-md">
                {{ item.title }}
              </p>
              <p class="text-gray-700 xs:text-xs sm:text-sm md:text-md">
                {{ item.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ADVANTAGES SECTION -->
    <div
      id="advantages"
      class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div class="grid gap-5 row-gap-8 lg:grid-cols-2">
        <div class="flex flex-col justify-center advantages-content">
          <div class="max-w-xl mb-6">
            <h2
              class="max-w-lg mb-6 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl sm:leading-none"
            >
              {{ advantages.title }}<br class="hidden md:block" />
              {{ advantages.titleTwo }}
              <span class="relative px-1">
                <div
                  class="absolute inset-x-0 bottom-0 h-3 transform -skew-x-12 bg-transparent"
                ></div>
                <span class="relative inline-block text-teal-accent-400">{{
                  advantages.subtitle
                }}</span>
              </span>
            </h2>
            <p class="text-base text-gray-700 md:text-lg">
              {{ advantages.description }}
            </p>
          </div>
          <div class="grid gap-5 row-gap-8 sm:grid-cols-2">
            <div
              v-for="item in advantages.advantages"
              :key="item.id"
              class="duration-300 transform bg-white border-l-4 shadow-sm border-teal-accent-400 hover:-translate-y-2"
            >
              <div class="h-full p-5 border border-l-0 rounded-r">
                <h6 class="mb-2 font-semibold leading-5">
                  {{ item.title }}
                </h6>
                <p class="text-sm text-gray-900" v-html="item.description"></p>
              </div>
            </div>
          </div>
        </div>
        <div>
          <img
            class="object-cover w-full h-56 rounded shadow-lg sm:h-96 advantages-image"
            :src="advantages.image"
            alt=""
          />
        </div>
      </div>
    </div>

    <div
      class="benefits-section px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div
        class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12"
      >
        <div>
          <p
            class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400"
          >
            {{ reasons.subject }}
          </p>
        </div>
        <h2
          class="max-w-lg mb-6 text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto"
        >
          <span class="relative inline-block">
            <svg
              viewBox="0 0 52 24"
              fill="#bdbdbd"
              class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block"
            >
              <defs>
                <pattern
                  id="34f481be-159a-4846-821d-9ca19fb6bcc5"
                  x="0"
                  y="0"
                  width=".135"
                  height=".30"
                >
                  <circle cx="1" cy="1" r=".7"></circle>
                </pattern>
              </defs>
              <rect
                fill="url(#34f481be-159a-4846-821d-9ca19fb6bcc5)"
                width="52"
                height="24"
              ></rect>
            </svg>
            <span class="relative">Buy</span>
          </span>
          {{ reasons.title }}
        </h2>
        <p class="text-base text-gray-700 md:text-lg">
          {{ reasons.description }}
        </p>
      </div>
      <div
        class="grid gap-8 row-gap-5 mb-8 md:row-gap-8 lg:grid-cols-4 sm:grid-cols-2"
      >
        <div
          v-for="item in reasons.reasons"
          :key="item.id"
          class="duration-300 transform bg-white border-l-4 border-teal-accent-400 hover:-translate-y-2"
        >
          <div class="h-full p-5 border border-l-0 rounded-r shadow-sm">
            <h6 class="mb-2 font-semibold leading-5">{{ item.title }}</h6>
            <p class="text-sm text-gray-900">
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- FOR WHO? -->
    <div
      class="public-section px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div
        class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12"
      >
        <div>
          <p
            class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400"
          >
            {{ users.subject }}
          </p>
        </div>
        <h2
          class="max-w-lg mb-6 text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto"
        >
          <span class="relative inline-block">
            <svg
              viewBox="0 0 52 24"
              fill="#bdbdbd"
              class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block"
            >
              <defs>
                <pattern
                  id="2feffae2-9edf-414e-ab8c-f0e6396a0fc1"
                  x="0"
                  y="0"
                  width=".135"
                  height=".30"
                >
                  <circle cx="1" cy="1" r=".7"></circle>
                </pattern>
              </defs>
              <rect
                fill="url(#2feffae2-9edf-414e-ab8c-f0e6396a0fc1)"
                width="52"
                height="24"
              ></rect>
            </svg>
            <span class="relative">Everyone</span>
          </span>
          {{ users.title }}
        </h2>
        <p class="text-base text-gray-700 md:text-lg">
          {{ users.description }}
        </p>
      </div>
      <div class="grid max-w-screen-lg gap-8 lg:grid-cols-2 sm:mx-auto">
        <div class="public-image grid grid-cols-2 gap-5">
          <img
            class="object-cover w-full h-56 col-span-2 rounded shadow-lg"
            :src="users.firstImage"
            alt=""
          />
          <img
            class="object-cover w-full h-48 rounded shadow-lg"
            :src="users.secondImage"
            alt=""
          />
          <img
            class="object-cover w-full h-48 rounded shadow-lg"
            :src="users.thirdImage"
            alt=""
          />
        </div>
        <div class="public-content flex flex-col justify-center">
          <div
            v-for="item in users.users"
            :key="item.id"
            class="pb-4 mb-4 border-b"
          >
            <h6 class="mb-2 font-semibold leading-5">
              {{ item.title }}
            </h6>
            <p class="text-sm text-gray-900">
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- CATEGORIES -->
    <div
      id="categories"
      class="bg-gradient-to-tr from-teal-accent-400 to-blue bg-white mb-20 animated-gradient"
    >
      <div
        class="relative px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
      >
        <div
          class="relative grid gap-5 xs:grid-cols-3 sm:grid-cols-3 lg:grid-cols-6"
        >
          <div
            v-for="item in categories"
            :key="item.id"
            class="px-10 py-20 bg-gray-600 bg-blend-multiply text-center transition duration-300 transform rounded shadow-2xl hover:scale-105 md:shadow-xl hover:shadow-2xl"
            v-bind:style="{
              backgroundImage: 'url(' + item.coverImage + ')',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }"
          >
            <p class="font-semibold text-gray-200 sm:text-lg lg:text-base">
              {{ item.title }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- SERVICES SECTION -->
    <div
      id="services"
      class="content-section relative xs:mt-0 sm:mt-[100px] md:mt-[0px] lg:mt-[-80px] xl:mt-[-90px] px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:py-20"
    >
      <div class="grid gap-10 sm:grid-cols-2">
        <div
          class="left-side flex flex-col justify-center md:pr-8 xl:pr-0 lg:max-w-lg"
        >
          <!-- LOGO -->
          <div
            class="logo-section flex items-center justify-center w-16 h-16 mb-4 rounded-full bg-gray-accent-400"
          >
            <svg class="text-teal-accent-400 w-7 h-7" viewBox="0 0 24 24">
              <polyline
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-miterlimit="10"
                points=" 8,5 8,1 16,1 16,5"
                stroke-linejoin="round"
              ></polyline>
              <polyline
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-miterlimit="10"
                points="9,15 1,15 1,5 23,5 23,15 15,15"
                stroke-linejoin="round"
              ></polyline>
              <polyline
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-miterlimit="10"
                points="22,18 22,23 2,23 2,18"
                stroke-linejoin="round"
              ></polyline>
              <rect
                x="9"
                y="13"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-miterlimit="10"
                width="6"
                height="4"
                stroke-linejoin="round"
              ></rect>
            </svg>
          </div>
          <!-- CONTENT -->
          <div class="text-section max-w-xl mb-6">
            <h2
              class="max-w-lg mb-6 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl sm:leading-none"
            >
              {{ content.title }}
              <span class="inline-block text-teal-accent-400">{{
                content.subtitle
              }}</span>
              ?
            </h2>
            <p class="text-base text-gray-700 md:text-lg">
              {{ content.description }}
            </p>
          </div>
        </div>
        <!-- IMAGES -->
        <div class="flex items-center justify-center -mx-4 lg:pl-8">
          <div class="flex flex-col items-end px-3">
            <img
              class="image-one object-cover mb-6 rounded shadow-lg h-28 sm:h-48 xl:h-56 w-28 sm:w-48 xl:w-56"
              :src="content.imageOne"
              alt=""
            />
            <img
              class="image-two object-cover w-20 h-20 rounded shadow-lg sm:h-32 xl:h-40 sm:w-32 xl:w-40"
              :src="content.imageTwo"
              alt=""
            />
          </div>
          <div class="px-3 image-three">
            <img
              class="object-cover w-40 h-40 rounded shadow-lg sm:h-64 xl:h-80 sm:w-64 xl:w-80"
              :src="content.imageThree"
              alt=""
            />
          </div>
        </div>
        <!-- STEP -->
        <!-- <ul class="steps col-span-2 step-section mt-12">
          <li
            v-for="step in steps"
            :key="step.title"
            :data-content="step.utfIcon"
            class="step md:text-xl"
          >
            <span
              class="mt-2 mb-2 font-bold xs:text-xs sm:text-2sm md:text-2xl"
              >{{ step.title }}</span
            >
            <p class="text-gray-700 xs:text-xs md:text-lg px-5">
              {{ step.description }}
            </p>
          </li>
        </ul> -->
        <div
          class="step-section col-span-2 lg:mt-0 mx-auto xs:max-w-2md sm:max-w-xl md:max-w-5xl lg:max-w-4xl xl:max-w-7xl xs:py-10 md:px-12 lg:px-8 lg:py-0 bg-white mt-12"
        >
          <div
            class="grid xs:gap-2 sm:gap-8 row-gap-0 xs:grid-cols-3 py-12 pl-2"
          >
            <div
              v-for="item in steps"
              :key="item.id"
              class="relative text-center step-item"
            >
              <!-- <div
                class="flex items-center justify-center xs:h-8 xs:w-8 sm:w-30 sm:h-30 mx-auto mb-3 rounded-full bg-gray-100"
              >
                <font-awesome-icon
                  class="xs:w-3 xs:h-3 sm:w-8 sm:h-8 text-teal-accent-400"
                  :icon="item.icon"
                />
              </div> -->
              <div
                class="flex items-center justify-center xs:h-12 xs:w-12 md:w-30 md:h-30 mx-auto mb-3 rounded-full bg-gray-100"
              >
                <font-awesome-icon
                  class="xs:w-8 xs:h-8 sm:w-8 sm:h-8 text-teal-accent-400"
                  :icon="item.icon"
                />
              </div>
              <h6 class="mb-2 font-bold xs:text-xs sm:text-2sm md:text-xl">
                {{ item.title }}
              </h6>
              <p class="text-gray-700 xs:text-xs md:text-lg">
                {{ item.description }}
              </p>

              <div
                class="arrow-icon top-0 right-0 flex items-center justify-center h-24 xs:-mr-8 xs:absolute"
              >
                <svg
                  class="xs:w-3 sm:w-5 md:w-8 lg:w-8 text-gray-700 transform rotate-90 xs:rotate-0"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24"
                >
                  <line
                    fill="none"
                    stroke-miterlimit="10"
                    x1="2"
                    y1="12"
                    x2="22"
                    y2="12"
                  ></line>
                  <polyline
                    fill="none"
                    stroke-miterlimit="10"
                    points="15,5 22,12 15,19 "
                  ></polyline>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SUBSCRIBE TO NEWSLETTER -->
    <div
      id="contact"
      class="flex flex-col items-center justify-center max-w-2xl px-4 pt-16 mx-auto sm:max-w-xl md:max-w-2xl lg:pt-10 md:px-8"
    >
      <div
        class="max-w-xl mb-10 md:mx-auto sm:text-center lg:max-w-2xl md:mb-12"
      >
        <div>
          <p
            class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400"
          >
            {{ newsletter.subject }}
          </p>
        </div>
        <h2
          class="max-w-lg mb-6 text-3xl font-bold leading-none tracking-tight text-gray-900 sm:text-4xl md:mx-auto"
        >
          <span class="relative inline-block">
            <svg
              viewBox="0 0 52 24"
              fill="#bdbdbd"
              class="absolute top-0 left-0 z-0 hidden w-32 -mt-8 -ml-20 text-blue-gray-100 lg:w-32 lg:-ml-28 lg:-mt-10 sm:block"
            >
              <defs>
                <pattern
                  id="9ef1ff62-feb2-41fe-8163-772b4c79de7b"
                  x="0"
                  y="0"
                  width=".135"
                  height=".30"
                >
                  <circle cx="1" cy="1" r=".7"></circle>
                </pattern>
              </defs>
              <rect
                fill="url(#9ef1ff62-feb2-41fe-8163-772b4c79de7b)"
                width="52"
                height="24"
              ></rect>
            </svg>
            <span class="relative">Subscribe</span>
          </span>
          {{ newsletter.title }}
        </h2>
        <p class="text-base text-gray-700 md:text-lg">
          {{ newsletter.description }}
        </p>
      </div>
      <form
        class="flex flex-col items-center w-full mb-4 md:flex-row md:px-16"
        v-on:submit.prevent="subscribeNewsletter"
      >
        <input
          placeholder="Email"
          required=""
          type="text"
          class="flex-grow w-full h-12 px-4 mb-3 transition duration-200 bg-white border border-gray-300 rounded shadow-sm appearance-none md:mr-2 md:mb-0 focus:border-teal-accent-400 focus:ring-teal-accent-400 focus:outline-none focus:shadow-outline"
          v-model="email"
        />
        <button
          type="submit"
          class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md md:w-auto bg-teal-accent-400 hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none"
        >
          Subscribe
        </button>
      </form>
      <p class="max-w-md mb-10 text-xs text-gray-600 sm:text-sm md:text-center">
        Just a friendly reminder every now and then to keep you updated on all
        the best deals and newest models.
      </p>
    </div>
  </div>
</template>

<script>
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { watchEffect, ref, inject, onMounted } from "vue";
import AnimatedNumber from "../components/AnimatedNumber.vue";
import axios from "axios";
gsap.registerPlugin(ScrollTrigger);

export default {
  name: "HomeView",
  components: {
    AnimatedNumber,
  },
  data() {
    return {
      hero: inject("dataENG").hero,
      stats: inject("dataENG").stats,
      content: inject("dataENG").content,
      categories: inject("dataENG").categories,
      steps: inject("dataENG").steps,
      advantages: inject("dataENG").advantages,
      reasons: inject("dataENG").reasons,
      users: inject("dataENG").users,
      newsletter: inject("dataENG").newsletter,
      email: "",
    };
  },
  methods: {
    async subscribeNewsletter() {
      let url = "/wphone/subscribe_newsletter";
      let data = {
        email: this.email,
      };
      await axios.post(url, data).then((response) => {
        if (response) {
          console.log(response.data);
          this.email = "";
          alert(`${response.data}`);
        }
      });
    },
  },

  setup() {
    const width = ref(window.innerWidth);

    const updateWidth = () => {
      width.value = window.innerWidth;
    };

    watchEffect(() => {
      window.addEventListener("resize", updateWidth);
      return () => window.removeEventListener("resize", updateWidth);
    });

    onMounted(() => {
      // remove last arrow icon
      const arrowIcons = document.querySelectorAll(".arrow-icon");
      arrowIcons[arrowIcons.length - 1].remove();

      // remove last border bottom
      const borderBottom = document.querySelectorAll(".border-b");
      borderBottom[borderBottom.length - 1].classList.remove("border-b");

      let responsive = gsap.matchMedia();

      let desktopBreakPoint = 1024;
      let tabletBreakPoint = 768;
      let mobileBreakPoint = 640;

      responsive.add(
        {
          isSmallMobile: `screen and (max-width: ${mobileBreakPoint}px)`,
          isMobile: `(max-width: ${tabletBreakPoint - 1}px) and (min-width: ${
            mobileBreakPoint + 1
          }px) and (prefers-reduced-motion: no-preference)`,
          isTablet: `(max-width: ${desktopBreakPoint - 1}px) and (min-width: ${
            tabletBreakPoint + 1
          }px) and (prefers-reduced-motion: no-preference)`,
          isDesktop: `(min-width: ${desktopBreakPoint}px) and (prefers-reduced-motion: no-preference)`,
        },
        (context) => {
          let { isSmallMobile, isMobile, isTablet, isDesktop } =
            context.conditions;

          // BANNER
          ScrollTrigger.create({
            trigger: ".box-header",
            start: "top 70%",
            end: "bottom 10%",
            scrub: 3,
            // markers: true,
            onEnter: () => {
              gsap.to(".box-header", {
                duration: 2,
                x: isDesktop ? 180 : 0,
                y: isMobile || isTablet ? -25 : -30,
                opacity: 1,
              });
              gsap.from(".cover-header-1", {
                duration: 1,
                x: isDesktop ? -10 : 0,
                opacity: 1,
              });
              gsap.from(".cover-header-2", {
                duration: 1,
                x: isDesktop ? 10 : 0,
                opacity: 1,
              });
              gsap.to(".title-header", {
                duration: 2,
                x: isDesktop ? 5 : 0,
                opacity: 1,
              });
              gsap.to(".paragraph-header", {
                duration: 2,
                x: isDesktop ? -50 : 0,
                opacity: 1,
              });
            },
            onLeave: () => {
              gsap.to(".box-header", {
                duration: 0.5,
                x: isDesktop ? -150 : 0,
                y: isMobile || isTablet ? 25 : 0,
                opacity: 0,
              });
              gsap.to(".cover-header-1", {
                duration: 0.5,
                x: isDesktop ? 40 : 0,
                opacity: 0,
              });
              gsap.to(".cover-header-2", {
                duration: 0.5,
                x: isDesktop ? -40 : 0,
                opacity: 0,
              });
              gsap.to(".title-header", {
                duration: 0.5,
                x: isDesktop ? 80 : 0,
                opacity: 0,
              });
              gsap.to(".paragraph-header", {
                duration: 0.5,
                x: isDesktop ? 50 : 0,
                opacity: 0,
              });
            },
            onEnterBack: () => {
              gsap.to(".box-header", {
                duration: 2,
                x: isDesktop ? 180 : 0,
                y: isMobile || isTablet ? -25 : -30,
                opacity: 1,
              });
              gsap.to(".cover-header-1", {
                duration: 1,
                x: isDesktop ? 0 : 0,
                opacity: 1,
              });
              gsap.to(".cover-header-2", {
                duration: 1,
                x: isDesktop ? 0 : 0,
                opacity: 1,
              });
              gsap.to(".title-header", {
                duration: 2,
                x: isDesktop ? 5 : 0,
                opacity: 1,
              });
              gsap.to(".paragraph-header", {
                duration: 2,
                x: isDesktop ? -50 : 0,
                opacity: 1,
              });
            },
            onLeaveBack: () => {
              gsap.to(".box-header", {
                duration: 0.5,
                x: isDesktop ? -150 : 0,
                y: isMobile || isTablet ? 25 : 0,
                opacity: 0,
              });
              gsap.to(".cover-header-1", {
                duration: 0.5,
                x: isDesktop ? 5 : 0,
                opacity: 0,
              });
              gsap.to(".cover-header-2", {
                duration: 0.5,
                x: isDesktop ? -5 : 0,
                opacity: 0,
              });
              gsap.to(".title-header", {
                duration: 0.5,
                x: isDesktop ? 80 : 0,
                opacity: 0,
              });
              gsap.to(".paragraph-header", {
                duration: 0.5,
                x: isDesktop ? 50 : 0,
                opacity: 0,
              });
            },
          });

          // STATS
          ScrollTrigger.create({
            trigger: ".stat-card",
            start: "top 80%",
            end: "bottom 20%",
            scrub: 3,
            onEnter: () => {
              gsap.from("#stats-section", {
                duration: 3,
                opacity: 1,
                y: isSmallMobile ? 100 : 80,
                ease: "power4.out",
              });
              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 1,
                y: isSmallMobile
                  ? -25
                  : isMobile
                  ? -20
                  : isTablet
                  ? -30
                  : isDesktop
                  ? -70
                  : 0,
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
              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                ease: "power4.out",
              });
              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.2,
                ease: "power4.out",
              });
            },
            onEnterBack: () => {
              gsap.from("#stats-section", {
                duration: 3,
                opacity: 1,
                y: isSmallMobile ? 0 : 80,
                ease: "power4.out",
              });
              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 1,
                y: isSmallMobile
                  ? -30
                  : isMobile
                  ? -20
                  : isTablet
                  ? -30
                  : isDesktop
                  ? -70
                  : 10,
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
            onLeaveBack: () => {
              gsap.to(".stats-section", {
                duration: 0.5,
                opacity: 0,
                y: 80,
                ease: "power4.out",
              });
              gsap.to(".stat-card", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                ease: "power4.out",
              });
              gsap.to(".stat-item", {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.2,
                ease: "power4.out",
              });
            },
          });

          // ADVANTAGES
          gsap
            .timeline({
              scrollTrigger: {
                trigger: "#advantages",
                start: isSmallMobile
                  ? "top 100%"
                  : isDesktop
                  ? "top 80%"
                  : "top 100%",
                end: isSmallMobile
                  ? "bottom 5%"
                  : isDesktop
                  ? "bottom 20%"
                  : "bottom 10%",
                scrub: 3,
              },
            })
            .add("start")
            .from(
              ".advantages-content",
              {
                duration: 1,
                opacity: 0,
                x: innerWidth * -1,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".advantages-image",
              {
                duration: 1,
                opacity: 0,
                x: innerWidth * 1,
                ease: "power4.out",
              },
              "start"
            );

          // BENEFTIS
          gsap
            .timeline({
              scrollTrigger: {
                trigger: ".benefits-section",
                start: "top 80%",
                end: "bottom 20%",
                scrub: 3,
              },
            })
            .to(".benefits-section", {
              duration: 3,
              opacity: 1,
              y: -100,
              ease: "power4.out",
            });

          // PUBLIC
          gsap
            .timeline({
              scrollTrigger: {
                trigger: ".public-section",
                start: "top 80%",
                end: "bottom 20%",
                scrub: 3,
              },
            })
            .add("start")
            .to(".public-section", {
              duration: 3,
              opacity: 1,
              y: -200,
              ease: "power4.out",
            })
            .from(
              ".public-image",
              {
                duration: 1,
                opacity: 0,
                x: innerWidth * -1,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".public-content",
              {
                duration: 1,
                opacity: 0,
                x: innerWidth * 1,
                ease: "power4.out",
              },
              "start"
            );

          // ABOUT
          gsap
            .timeline({
              scrollTrigger: {
                trigger: ".content-section",
                start: isSmallMobile ? "top 100%" : "top 70%",
                end: isSmallMobile ? "top 100%" : "bottom 50%",
                scrub: 3,
              },
            })
            .add("start")
            .to(
              ".content-section",
              {
                duration: 3,
                opacity: 1,
                y: isSmallMobile ? -410 : 0,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".content-section",
              {
                duration: 2,
                opacity: 0,

                x: innerWidth * 1,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".image-one",
              {
                duration: 2,
                opacity: 0,
                y: -100,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".image-two",
              {
                duration: 2,
                opacity: 0,
                y: 100,
                ease: "power4.out",
              },
              "start"
            )
            .from(
              ".image-three",
              {
                duration: 2,
                opacity: 0,
                x: 100,
                ease: "power4.out",
              },
              "start"
            );

          // CATEGORIES
          gsap
            .timeline({
              scrollTrigger: {
                trigger: "#categories",
                start: "top 80%",
                end: "bottom 20%",
                scrub: 3,
              },
            })
            .to("#categories", {
              duration: 0.5,
              opacity: 1,
              y: isSmallMobile
                ? -320
                : isMobile
                ? -120
                : isTablet
                ? -290
                : isDesktop
                ? -160
                : 0,
              ease: "power4.out",
            });
          gsap
            .timeline({
              scrollTrigger: {
                trigger: ".step-section",
                start: "top 80%",
                end: "bottom 20%",
                scrub: 3,
              },
            })
            .add("start")
            .from(".step-section", {
              duration: 0.5,
              opacity: 0,
              y: 50,
              ease: "power4.out",
            })
            .from(".step-item", {
              duration: 0.5,
              opacity: 0,
              y: 20,
              stagger: 0.2,
              ease: "power4.out",
            });
        }
      );
      return () => {
        responsive.remove();
      };
    });

    return {
      width,
    };
  },
};
</script>

<style>
.animated-gradient {
  background-size: 400%;

  -webkit-animation: AnimatedGradient 15s ease infinite;
  -moz-animation: AnimatedGradient 15s ease infinite;
  animation: AnimatedGradient 15s ease infinite;
}

@-webkit-keyframes AnimatedGradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@-moz-keyframes AnimatedGradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
@keyframes AnimatedGradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
