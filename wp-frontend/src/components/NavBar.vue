<template>
  <div class="relative bg-white">
    <div class="mx-auto max-w-7xl">
      <div class="relative z-10 bg-white pb-5">
        <Popover>
          <div class="relative px-4 pt-6 sm:px-6 lg:px-8">
            <nav
              class="relative flex items-center justify-between sm:h-10 lg:justify-start"
              aria-label="Global"
            >
              <!-- LOGO -->
              <div
                class="flex flex-shrink-0 flex-grow items-center lg:flex-grow-0"
              >
                <div class="flex w-full items-center justify-between md:w-auto">
                  <a href="#">
                    <span class="sr-only">Which Phone</span>
                    <img
                      alt="Which Phone"
                      class="h-8 w-auto sm:h-10"
                      src="../assets/logo_light.svg"
                    />
                  </a>
                  <div class="-mr-2 flex items-center md:hidden">
                    <PopoverButton
                      class="inline-flex items-center justify-center rounded-md bg-white p-2 hover:text-teal-accent-400 hover:bg-gray-100 text-gray-500 focus:outline-none"
                    >
                      <!-- focus:ring-2 focus:ring-inset focus:ring-teal-accent-500 -->
                      <span class="sr-only">Open main menu</span>
                      <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                    </PopoverButton>
                  </div>
                </div>
              </div>
              <!-- NAVIGATION -->
              <div class="hidden md:ml-10 md:block md:space-x-8 md:pr-4 w-full">
                <div class="flex justify-between">
                  <div class="inline-block">
                    <RouterLink
                      v-for="item in navigation"
                      :key="item.name"
                      :to="item.link"
                      :class="[
                        item.current
                          ? 'bg-teal-accent-400 font-medium text-white hover:bg-teal-accent-600 transition duration-200'
                          : 'text-gray-500 hover:text-teal-accent-400',
                        'px-3 py-2 rounded-md text-sm font-medium transition duration-200',
                      ]"
                      :aria-current="item.current ? 'page' : undefined"
                    >
                      {{ item.name }}
                    </RouterLink>
                  </div>
                  <div class="flex inline-block">
                    <!-- THEME SWITCHER -->
                    <!-- <label
                      class="relative swap swap-rotate mr-3 hover:-translate-y-0.5 transform transition ease-in-out duration-200"
                    >
                      <input class="sr-only" type="checkbox" />

                      <svg
                        class="swap-on fill-teal-accent-400 w-7 h-7"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                      >
                        <path
                          d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"
                        />
                      </svg>
                      <svg
                        class="swap-off fill-teal-accent-400 w-7 h-7"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                      >
                        <path
                          d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"
                        />
                      </svg>
                    </label> -->
                    <p
                      v-if="isAuthenticated"
                      class="px-2 py-0 font-bold text-base text-teal-accent-400"
                    >
                      {{ username }}
                    </p>
                    <RouterLink
                      v-if="!isAuthenticated"
                      to="/login"
                      class="font-bold text-teal-accent-400 hover:text-teal-accent-600"
                      >Log in</RouterLink
                    >

                    <MenuHeadless
                      v-if="isAuthenticated"
                      as="div"
                      class="relative ml-3"
                    >
                      <div>
                        <MenuButton
                          class="flex max-w-xs items-center rounded-full text-sm shadow-lg hover:-translate-y-0.5 transform transition ease-in-out duration-200"
                        >
                          <span class="sr-only">Open user menu</span>
                          <img
                            class="h-7 w-7 rounded-full"
                            :src="avatar"
                            alt=""
                          />
                        </MenuButton>
                      </div>
                      <transition
                        enter-active-class="transition ease-out duration-100"
                        enter-from-class="transform opacity-0 scale-95"
                        enter-to-class="transform opacity-100 scale-100"
                        leave-active-class="transition ease-in duration-75"
                        leave-from-class="transform opacity-100 scale-100"
                        leave-to-class="transform opacity-0 scale-95"
                      >
                        <MenuItems
                          class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-2 ring-opacity-10 ring-teal-accent-400 focus:outline-none"
                        >
                          <MenuItem
                            v-for="item in userNavigation"
                            :key="item.name"
                            v-slot="{ active }"
                          >
                            <a
                              v-if="item.name == 'Sign out'"
                              v-on:click="logout"
                              :class="[
                                active ? 'bg-gray-100' : '',
                                'block px-4 py-2 text-sm text-gray-700 cursor-pointer',
                              ]"
                              >{{ item.name }}</a
                            >
                            <RouterLink
                              v-else
                              :to="item.to"
                              :class="[
                                active ? 'bg-gray-100' : '',
                                'block px-4 py-2 text-sm text-gray-700 cursor-pointer',
                              ]"
                              >{{ item.name }}</RouterLink
                            >
                          </MenuItem>
                        </MenuItems>
                      </transition>
                    </MenuHeadless>
                  </div>
                </div>
              </div>
            </nav>
          </div>

          <transition
            enter-active-class="duration-150 ease-out"
            enter-from-class="opacity-0 scale-95"
            enter-to-class="opacity-100 scale-100"
            leave-active-class="duration-100 ease-in"
            leave-from-class="opacity-100 scale-100"
            leave-to-class="opacity-0 scale-95"
          >
            <PopoverPanel
              focus
              class="absolute inset-x-0 top-0 z-10 origin-top-right transform p-2 transition md:hidden"
              v-slot="{ close }"
            >
              <div
                class="overflow-hidden rounded-lg bg-white shadow-md ring-1 ring-black ring-opacity-5"
              >
                <div class="flex items-center justify-between px-5 pt-4">
                  <div>
                    <img class="h-8 w-auto" src="../assets/logo.svg" alt="" />
                  </div>
                  <div class="-mr-2">
                    <PopoverButton
                      class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-500 hover:bg-gray-100 hover:text-teal-accent-400 focus:outline-none"
                    >
                      <!-- focus:ring-2 focus:ring-inset focus:ring-teal-accent-500 -->
                      <span class="sr-only">Close main menu</span>
                      <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                    </PopoverButton>
                  </div>
                </div>
                <div class="space-y-1 px-4 pt-7 pb-3">
                  <RouterLink
                    v-for="item in navigation"
                    :key="item.name"
                    :to="item.link"
                    @click="close()"
                    :class="[
                      item.current
                        ? 'bg-teal-accent-400 font-medium text-white hover:bg-teal-accent-600 '
                        : 'text-gray-500 hover:text-teal-accent-400',
                      'px-3 py-2 rounded-md text-sm font-medium',
                    ]"
                    :aria-current="item.current ? 'page' : undefined"
                    >{{ item.name }}</RouterLink
                  >
                </div>

                <RouterLink
                  v-if="!isAuthenticated"
                  to="/login"
                  class="block w-full bg-gray-50 px-5 py-3 text-center font-medium text-teal-accent-400 hover:bg-gray-100"
                  >Log in</RouterLink
                >
                <a
                  v-if="isAuthenticated"
                  v-on:click="logout"
                  class="block w-full bg-gray-50 px-5 py-3 text-center font-medium text-teal-accent-600 hover:bg-gray-100 cursor-pointer"
                >
                  Log out
                </a>
              </div>
            </PopoverPanel>
          </transition>
        </Popover>
      </div>
    </div>
  </div>
</template>

<script>
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Menu as MenuHeadless,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue";
import { Bars3Icon, XMarkIcon } from "@heroicons/vue/24/outline";
import { RouterLink } from "vue-router";
import { computed, inject } from "vue";
import { useAuthStore } from "../stores/auth";
import { useWishlistStore } from "../stores/checked";

export default {
  name: "NavBar",
  // props: {
  //   username: String,
  // },
  data() {
    return {
      userNavigation: [
        { name: "Settings", to: "/settings" },
        { name: "Sign out" },
      ],
      navigation: inject("dataENG").navigation,
    };
  },

  components: {
    Popover,
    PopoverButton,
    PopoverPanel,
    Bars3Icon,
    XMarkIcon,
    RouterLink,
    MenuHeadless,
    MenuButton,
    MenuItem,
    MenuItems,
  },

  methods: {
    logout() {
      let wishList = useWishlistStore();
      let authStore = useAuthStore();
      authStore.setRemoveAccess();
      wishList.clearWishlist();
      this.$router.push("/");
    },
    route() {
      this.navigation.forEach((item) => {
        if (item.link === this.$route.path) {
          item.current = true;
        } else {
          item.current = false;
        }
        // console.log(item.current, item.name);
        // console.log(this.$route.path);
      });
    },
  },

  watch: {
    $route: {
      handler: "route",
      immediate: true,
    },
  },

  setup() {
    return {
      isAuthenticated: computed(() => useAuthStore().access),
      avatar: computed(() => useAuthStore().getAvatar),
      username: computed(() => useAuthStore().getUser),
    };
  },
};
</script>
