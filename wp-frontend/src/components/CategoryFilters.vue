<template>
  <div class="bg-white">
    <div>
      <!-- Mobile filter dialog -->
      <TransitionRoot as="template" :show="mobileFiltersOpen">
        <HeadlessDialog
          as="div"
          class="relative z-40 lg:hidden"
          @close="mobileFiltersOpen = false"
        >
          <TransitionChild
            as="template"
            enter="transition-opacity ease-linear duration-300"
            enter-from="opacity-0"
            enter-to="opacity-100"
            leave="transition-opacity ease-linear duration-300"
            leave-from="opacity-100"
            leave-to="opacity-0"
          >
            <div class="fixed inset-0 bg-black bg-opacity-25" />
          </TransitionChild>

          <div class="fixed inset-0 z-40 flex">
            <TransitionChild
              as="template"
              enter="transition ease-in-out duration-300 transform"
              enter-from="translate-x-full"
              enter-to="translate-x-0"
              leave="transition ease-in-out duration-300 transform"
              leave-from="translate-x-0"
              leave-to="translate-x-full"
            >
              <DialogPanel
                class="relative ml-auto flex h-full w-full max-w-xs flex-col overflow-y-auto bg-white py-4 pb-12 shadow-xl"
              >
                <div class="flex items-center justify-between px-4">
                  <h2 class="text-lg font-medium text-gray-900">Filters</h2>
                  <button
                    type="button"
                    class="-mr-2 flex h-10 w-10 items-center justify-center rounded-md bg-white p-2 text-gray-400"
                    @click="mobileFiltersOpen = false"
                  >
                    <span class="sr-only">Close menu</span>
                    <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>

                <!-- Filters -->
                <form class="mt-4 border-t border-gray-200">
                  <Disclosure
                    as="div"
                    v-for="section in filters"
                    :key="section.id"
                    class="border-t border-gray-200 px-4 py-6"
                    v-slot="{ open }"
                  >
                    <h3 class="-mx-2 -my-3 flow-root">
                      <DisclosureButton
                        class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500"
                      >
                        <span class="font-medium text-gray-900">{{
                          section.name
                        }}</span>
                        <span class="ml-6 flex items-center">
                          <PlusIcon
                            v-if="!open"
                            class="h-5 w-5"
                            aria-hidden="true"
                          />
                          <MinusIcon
                            v-else
                            class="h-5 w-5"
                            aria-hidden="true"
                          />
                        </span>
                      </DisclosureButton>
                    </h3>
                    <DisclosurePanel class="pt-6">
                      <div class="space-y-6">
                        <div
                          v-for="(option, optionIdx) in section.options"
                          :key="option.value"
                          class="flex items-center"
                        >
                          <input
                            :id="`filter-mobile-${section.id}-${optionIdx}`"
                            :name="`${section.id}[]`"
                            :value="option.value"
                            type="checkbox"
                            :checked="option.checked"
                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"
                          />
                          <label
                            :for="`filter-mobile-${section.id}-${optionIdx}`"
                            class="ml-3 min-w-0 flex-1 text-gray-500"
                            >{{ option.label }}</label
                          >
                        </div>
                      </div>
                    </DisclosurePanel>
                  </Disclosure>
                </form>
              </DialogPanel>
            </TransitionChild>
          </div>
        </HeadlessDialog>
      </TransitionRoot>

      <main
        v-if="dataDevices.length > 0"
        class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8"
      >
        <div
          class="flex items-baseline justify-between border-b border-gray-200 xs:pt-1 sm:pt-18 pb-6"
        >
          <h1
            class="xs:text-2xl sm:text-4xl font-bold tracking-tight text-gray-900"
          >
            Results
          </h1>

          <div class="flex items-center">
            <div
              :class="{
                'flex items-center text-teal-accent-400 mr-5 cursor-pointer hover:text-teal-accent-700':
                  sortActive,
                'flex items-center text-gray-500 mr-5 cursor-pointer hover:text-gray-700':
                  !sortActive,
              }"
              @click="toggleSortActive"
            >
              <font-awesome-icon
                icon="fa-solid fa-filter-circle-dollar"
                class="mr-2"
              />
              Price:
            </div>

            <label
              class="relative swap swap-rotate text-gray-500 mr-3 hover:-translate-y-0.5 transform transition ease-in-out duration-200"
            >
              <input
                :disabled="!sortActive"
                @click="toggleSort"
                :checked="sortOrder"
                ref="sortInput"
                v-model="sortOrder"
                class="sr-only"
                type="checkbox"
              />
              <font-awesome-icon
                icon="fa-solid fa-arrow-down-wide-short "
                class="swap-on w-5 h-5"
              ></font-awesome-icon>
              <font-awesome-icon
                icon="fa-solid fa-arrow-up-short-wide"
                class="swap-off w-5 h-5"
              ></font-awesome-icon>
            </label>

            <button
              type="button"
              class="-m-2 ml-4 p-2 text-gray-400 hover:text-gray-500 sm:ml-6 lg:hidden"
              @click="mobileFiltersOpen = true"
            >
              <span class="sr-only">Filters</span>
              <FunnelIcon class="h-5 w-5" aria-hidden="true" />
            </button>
          </div>
        </div>

        <section aria-labelledby="products-heading" class="pt-6 pb-24">
          <!-- <h2 id="products-heading" class="sr-only">Products</h2> -->

          <div class="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-4">
            <!-- Filters -->
            <form class="hidden lg:block">
              <h3 class="sr-only">Categories</h3>
              <div
                v-for="section in filters"
                :key="section.id"
                class="border-b border-gray-200 py-6"
              >
                <h3 class="-my-3 flow-root">
                  <div
                    class="flex w-full items-center justify-between bg-white py-3 text-sm text-gray-400 hover:text-gray-500"
                    @click="section.open = !section.open"
                  >
                    <span class="font-medium text-gray-900">{{
                      section.name
                    }}</span>
                    <span class="ml-6 flex items-center">
                      <PlusIcon
                        v-if="!section.open"
                        class="h-5 w-5"
                        aria-hidden="true"
                      />
                      <MinusIcon v-else class="h-5 w-5" aria-hidden="true" />
                    </span>
                  </div>
                </h3>
                <div v-if="section.open" class="collapse pt-6">
                  <div class="space-y-4">
                    <input
                      type="range"
                      v-model="section.value"
                      :min="section.options.min"
                      :max="section.options.max"
                      class="range range-xs range-success"
                      :step="section.options.step"
                      :change="updateFilters(section.id, section.value)"
                    />
                  </div>
                  <div class="text-xs text-gray-600">
                    {{ section.value }} {{ section.options.units }}
                  </div>
                </div>
              </div>
            </form>

            <!-- Product grid -->
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div
                v-if="dataDevices.length > 0"
                class="lg:col-span-3 grid xs:grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-x-24 px-12"
              >
                <div
                  v-for="item of itemsOnCurrentPage"
                  :key="item.id"
                  class="flex flex-col justify-center items-center max-w-xs mx-auto my-4"
                >
                  <PhoneCard
                    :device_id="item.id"
                    :name="item.name"
                    :price="item.price"
                    :thumbnail="item.thumbnail"
                    :summary="item.summary"
                    :battery="item.battery"
                    :camera="item.rear_camera"
                    :screen="item.screen_size"
                    :ram="item.ram"
                    :storage="item.storage"
                    :selfie="item.front_camera"
                    :musicplay="item.music_time"
                    :talktime="item.talk_time"
                    :standby="item.standby_time"
                    :inWishlist="inWishlist(item.id)"
                  />
                </div>
              </div>
            </transition>
          </div>
          <div class="grid grid-cols-7 mt-14">
            <div
              class="btn-group grid xs:col-start-2 xs:col-span-5 grid-cols-3 sm:col-start-4 sm:col-span-3 xs:text-sm sm:text-base"
              data-theme="dark"
            >
              <button
                class="btn btn-outline btn-success"
                v-on:click="previousPage"
                :disabled="currentPage === 1"
              >
                Previous
              </button>
              <button class="btn disabled">
                Page {{ currentPage }} of {{ totalPages }}
              </button>
              <button class="btn btn-outline btn-success" v-on:click="nextPage">
                Next
              </button>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script>
import {
  Dialog as HeadlessDialog,
  DialogPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { XMarkIcon } from "@heroicons/vue/24/outline";
import { FunnelIcon, MinusIcon, PlusIcon } from "@heroicons/vue/20/solid";

import PhoneCard from "@/components/PhoneCard.vue";
import { useDataStore, useWishlistStore } from "../stores/checked";
export default {
  components: {
    HeadlessDialog,
    DialogPanel,
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    TransitionChild,
    TransitionRoot,
    XMarkIcon,
    FunnelIcon,
    MinusIcon,
    PlusIcon,
    PhoneCard,
  },
  data() {
    return {
      newFilterValue: null,
      sortActive: false,
      sortOrder: false,
      dataDevices: [],
      mobileFiltersOpen: false,
      dataStore: useDataStore(),
      useWishlistStore: useWishlistStore(),
      filters: [
        {
          id: "battery",
          name: "Battery",
          options: { min: 0, max: 5000, step: 200, units: "mAh" },
          value: 0,
        },
        {
          id: "screen_size",
          name: "Screen Size",
          options: { min: 5, max: 10, step: 0.5, units: "inches" },
          value: 5,
        },
        {
          id: "storage",
          name: "Storage",
          options: {
            min: 0,
            max: 512,
            step: 4,
            units: "GB",
          },
          value: 0,
        },
        {
          id: "ram",
          name: "RAM",
          options: {
            min: 0,
            max: 15,
            step: 1,
            units: "GB",
          },
          value: 0,
        },
        {
          id: "rear_camera",
          name: "Camera",
          options: {
            min: 0,
            max: 100,
            step: 1,
            units: "MP",
          },
          value: 0,
        },
        {
          id: "front_camera",
          name: "Selfie Camera",
          options: {
            min: 0,
            max: 100,
            step: 1,
            units: "MP",
          },
          value: 0,
        },
        {
          id: "price",
          name: "Price",
          options: {
            min: 0,
            max: 1000,
            step: 10,
            units: "$",
          },
          value: 0,
        },
      ],
      currentPage: 1,
      itemsPerPage: 9,
      devicesNotFound: true,
    };
  },
  props: {
    data: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    hasData() {
      return this.data.length > 0;
    },
    hasToken() {
      return localStorage.getItem("access");
    },
    clearData() {
      return this.dataStore.getData;
    },
    totalPages() {
      return Math.ceil(this.dataDevices.length / this.itemsPerPage);
    },
    itemsOnCurrentPage() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      return this.dataDevices.slice(startIndex, startIndex + this.itemsPerPage);
    },
    currentFilter() {
      return this.filters.find((item) => item.id === this.currentFilterId);
    },
    inWishlist() {
      return (id) => this.useWishlistStore.getIdWishlist.includes(id);
    },
  },
  watch: {
    hasData(hasData) {
      this.dataDevices = hasData
        ? [...this.data]
        : [] && this.devicesNotFound === true;
      if (!hasData) {
        this.filters.forEach((item) => {
          item.value = item.options.min;
        });
      }
    },
    clearData(clearData) {
      if (!clearData) {
        this.dataDevices = [];
      }
    },
    newFilterValue(newValue) {
      this.currentFilter.value = newValue;
    },
  },

  methods: {
    sortData() {
      if (this.sortActive) {
        console.log("sort is active");
        if (this.sortOrder) {
          this.dataDevices.sort((a, b) => b.price - a.price);
          console.log("data sorted in descending order");
        } else {
          this.dataDevices.sort((a, b) => a.price - b.price);
          console.log("data sorted in ascending order");
        }
      } else {
        this.dataDevices = [...this.data];
        console.log("sort is not active");
      }
    },
    toggleSort() {
      this.sortOrder = !this.sortOrder;
      this.sortData();
    },
    toggleSortActive() {
      if (this.hasData) {
        this.sortActive = !this.sortActive;
        this.sortData();
      } else {
        console.log("no data available");
      }
    },
    filterData() {
      this.dataDevices = this.data.filter((item) => {
        let valid = true;
        this.filters.forEach((filter) => {
          if (item[filter.id] < filter.value) {
            valid = false;
          }
        });
        return valid;
      });
    },
    updateFilters(id, value) {
      this.filters.forEach((item) => {
        if (item.id === id) {
          item.value = value;
        }
      });
      this.filterData();
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
  created() {
    if (this.hasToken) {
      this.useWishlistStore.initializeWishlist();
    }
  },
  beforeUnmount() {
    this.useWishlistStore.saveToDB();
    this.useWishlistStore.clearWishlist();
    console.log("data cleared");
  },
};
</script>
