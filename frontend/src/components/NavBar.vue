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
              <div
                class="flex flex-shrink-0 flex-grow items-center lg:flex-grow-0"
              >
                <div class="flex w-full items-center justify-between md:w-auto">
                  <a href="#">
                    <span class="sr-only">Which Phone</span>
                    <img
                      alt="Which Phone"
                      class="h-8 w-auto sm:h-10"
                      src="../assets/logo.svg"
                    />
                  </a>
                  <div class="-mr-2 flex items-center md:hidden">
                    <PopoverButton
                      class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-green-500"
                    >
                      <span class="sr-only">Open main menu</span>
                      <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                    </PopoverButton>
                  </div>
                </div>
              </div>
              <div class="hidden md:ml-10 md:block md:space-x-8 md:pr-4">
                <RouterLink
                  v-for="item in navigation"
                  :key="item.name"
                  :to="item.link"
                  :class="[
                    item.current
                      ? 'bg-green-600 font-medium text-white hover:bg-green-700'
                      : 'text-gray-300 hover:text-green-600 hover:text-green-600',
                    'px-3 py-2 rounded-md text-sm font-medium',
                  ]"
                  :aria-current="item.current ? 'page' : undefined"
                >
                  {{ item.name }}
                </RouterLink>
                <RouterLink
                  to="/login"
                  class="font-medium text-green-600 hover:text-green-500"
                  >Log in</RouterLink
                >
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
                      class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-green-500"
                    >
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
                        ? 'bg-green-600 font-medium text-white hover:bg-green-700 '
                        : 'text-gray-300 hover:text-green-600 hover:text-white',
                      'px-3 py-2 rounded-md text-sm font-medium',
                    ]"
                    :aria-current="item.current ? 'page' : undefined"
                    >{{ item.name }}</RouterLink
                  >
                </div>
                <a
                  href="#"
                  class="block w-full bg-gray-50 px-5 py-3 text-center font-medium text-green-600 hover:bg-gray-100"
                  >Log in</a
                >
              </div>
            </PopoverPanel>
          </transition>
        </Popover>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { Bars3Icon, XMarkIcon } from "@heroicons/vue/24/outline";
import { RouterLink } from "vue-router";
import { inject } from "vue";

const navigation = inject("dataENG").navigation;

// const navigation = [
//   { name: "Guid", link: "/", current: true },
//   { name: "Pricing", link: "/pricing", current: false },
//   { name: "About", link: "/about", current: false },
// ];
</script>
